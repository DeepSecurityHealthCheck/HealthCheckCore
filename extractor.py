import pickle
import lzma
import lib.data_loader as dl
from cryptography.hazmat.primitives import serialization
from cryptography.hazmat.primitives.asymmetric import padding as ass_padding
import base64
import getpass
import time
from cryptography.fernet import Fernet
from cryptography.hazmat.backends import default_backend

from cryptography.hazmat.primitives.kdf.pbkdf2 import PBKDF2HMAC
from cryptography.hazmat.primitives.ciphers import Cipher, algorithms, modes
from cryptography.hazmat.primitives import hashes, hmac
from cryptography.hazmat.primitives import padding

import requests
import sys
import json
from base64 import b64encode
import random
import argparse
from colorama import init, Fore

import traceback
init(autoreset=True)

from tqdm import tqdm

import os, sys
from sys import exit
import json

import lib.constants as constants

path = "keys/"
#DShc api url
api_url = "https://deepsecurityhealthcheck.com/{}"




def get_key_data(key_class, fixed_key=None):
    if fixed_key is not None:
        key = fixed_key
    else:
        key = input("Enter the public key file name (Default: {}_key.pem): ".format(key_class))

    if not key:
        key = path + '{}_key.pem'.format(key_class)
    else:
        key = path + key

    if not os.path.exists(key):
        print(Fore.RED + "Invalid key {} in {} directory! aborting...".format(key, path))
        exit(1)

    with open(key, "rb") as key_file:
        key_data = key_file.read()

    if key_data is None or key_data == "":
        print(Fore.RED + "Invalid key {}! aborting...".format(key))
        exit(-1)
        
    return key_data


def get_filename(output=False):
    pack_name = input("Enter the output file name (Default: DATA_PACK): ")
    if not pack_name:
        pack_name = "DATA_PACK.dat"
    else:
        end = pack_name[:-4]
        if end.lower() != ".dat":
            pack_name += ".dat"

    if not os.path.exists(pack_name) and not output:
        print(Fore.RED + "Data pack is not in the directory! aborting... ({})".format(pack_name))
        exit(-1)
    elif os.path.exists(pack_name) and output:
        print(Fore.RED + "Data pack already exists... ({})".format(pack_name))
        exit(-1)

    return pack_name


def generate_unencrypted(data_pack,output_name):
    print(Fore.LIGHTRED_EX + "Generating an UNENCRYPTED Data Package - (DO NOT SEND IT - for YOUR REVIEW ONLY)")
    with open(output_name+".json",'w') as raw_json:
        temp = data_pack.pop('host')
        data_pack.pop('customer_info')
        # Host will break this loop, because it is a string.
        for key in data_pack.keys():
            json_objects = []
            if isinstance(data_pack[key], list):
                for obj in list(data_pack[key]):
                    json_objects.append(obj.to_dict())
            elif isinstance(data_pack[key],dict):
                json_objects.append(data_pack[key])
            else:
                json_objects.append(data_pack[key].to_dict())
                
            data_pack[key] = json_objects
        
        data_pack['host'] = temp
        raw_json.write(json.dumps(data_pack,indent=4,sort_keys=True))


def pack_data(data_migrate=None, send_now=True, unencrypted=False):
    print(constants.EXTRACTOR_WIZARD_HEADER)
    
    #Used in case automatic submission fails
    output_name = str("data_pack_"+str(time.time())).replace(".","")
    
    public_key = serialization.load_pem_public_key(
        get_key_data("PUBLIC"),
        backend=default_backend()
    )
    print(constants.EXTRACTOR_HELP_STRING)
    if not public_key:
        print(Fore.RED + "Could not load the public key")
        exit(667)

    data_pack = {}
    if data_migrate is not None:
        data_pack = data_migrate
    else:
        try:
            print("{}Please fill these infos precisely, they will appear on the report".format(Fore.LIGHTCYAN_EX))
            data_pack = dl.get_info(include_am_configs=True, include_fw_configs=True)
        except Exception as e:
            print(Fore.RED + "--------------Error while getting the data-------------- \n"
             + Fore.LIGHTWHITE_EX + str(e)  + "\n" + Fore.RED + "--------------Error while getting the data--------------")

    # Used to populate the HTTP request's JSON body
    generation_data = data_pack.get("customer_info")

    data = pickle.dumps(data_pack)
    
    if unencrypted:
        generate_unencrypted(data_pack,output_name)

    with tqdm(total=3) as pbar:
        pbar.set_description("Compressing data...")
        compressed = lzma.compress(data, preset=9 | lzma.PRESET_EXTREME)

        pbar.update(1)
        pbar.set_description("Crypto 1/2...")

        key_password = os.urandom(32) # 32 bytes / 256 bits

        # Padding
        padder = padding.PKCS7(256).padder()
        compressed_padded = padder.update(compressed)
        compressed_padded += padder.finalize()

        # Salt
        digest = hashes.Hash(hashes.SHAKE128(16), backend=default_backend())
        digest.update(key_password)
        salt = digest.finalize()

        # IV, NONCE, HMAC_KEY values generated from PBKDF2 using a single use key
        # Create real key from a given "key password"
        kdf_kp = PBKDF2HMAC(algorithm = hashes.SHA512(),
                         length = 32,
                         salt = salt,
                         iterations = 1000,
                         backend = default_backend())

        key = kdf_kp.derive(key_password)

        kdf_n = PBKDF2HMAC(algorithm = hashes.SHA256(),
                         length = 16,
                         salt = salt,
                         iterations = 200,
                         backend = default_backend())

        nonce = kdf_n.derive(key)

        kdf_iv = PBKDF2HMAC(algorithm=hashes.SHA256(),
                         length=16,
                         salt=salt,
                         iterations=200,
                         backend=default_backend())

        iv = kdf_iv.derive(nonce + key)

        kdf_hmac = PBKDF2HMAC(algorithm=hashes.SHA256(),
                         length=32,
                         salt=salt,
                         iterations=200,
                         backend=default_backend())

        hmac_key = kdf_hmac.derive(iv + key)

        # Chacha
        chacha_alg = algorithms.ChaCha20(key, nonce)
        cipher_chacha = Cipher(chacha_alg, mode=None, backend=default_backend())
        encryptor_chacha = cipher_chacha.encryptor()
        chacha_cipher = encryptor_chacha.update(compressed_padded)

        pbar.update(1)
        pbar.set_description("Crypto 2/2...")

        # Aes
        cipher_aes = Cipher(algorithms.AES(key), modes.CBC(iv), backend=default_backend())
        encryptor_aes = cipher_aes.encryptor()
        aes_cipher = encryptor_aes.update(chacha_cipher) + encryptor_aes.finalize()

        # HMAC
        h = hmac.HMAC(hmac_key, hashes.SHA512(), backend=default_backend())
        h.update(aes_cipher)
        hmac_bytes = h.finalize()

        # RSA
        # Encrypt the key with an 8192 RSA pub Key
        encrypted_password = public_key.encrypt(
            key_password,
            ass_padding.OAEP(
                mgf=ass_padding.MGF1(algorithm=hashes.SHA512()),
                algorithm=hashes.SHA512(),
                label=None
            )
        )
        pbar.update(1)
        pbar.set_description("Done!")

    aes_cipher += encrypted_password
    aes_cipher += hmac_bytes

    if send_now:

        if not upload(aes_cipher, generation_data):
            try:
                with open(output_name+".dat","wb") as out:
                    out.write(aes_cipher)
            except Exception as e:
                print(str(e)+"\nCould not save to disk! (permissions?)")
                exit(-1)

            print("{}Probably connection issues due to Firewall or no internet connection, please use this tool\n"
            " to resubmit the packege on a network with internet access using the command {}--send ".format(Fore.LIGHTYELLOW_EX,Fore.LIGHTRED_EX))

            print("{}To do it copy/send the new {}{}{} file created on this folder to other machine with internet\n" 
            "access. the file is extremelly secure it can be manipulated anywere".format(Fore.LIGHTCYAN_EX,
            Fore.LIGHTYELLOW_EX,output_name,Fore.LIGHTCYAN_EX))


            print(Fore.LIGHTGREEN_EX + "Package was saved successfully as {} !".format(output_name))
        else:
            print(Fore.YELLOW + "The report was successfully generated, the data packet was not saved locally")
    
    else:
            try:
                with open(output_name+".dat","wb") as out:
                    out.write(aes_cipher)
            except Exception as e:
                print(str(e)+"\nCould not save to disk! (permissions?)")
                exit(-1)

            print(Fore.LIGHTYELLOW_EX+"The package was not sent for processing, you will have to use the command --send to send another time.")

            print("{}To do it copy/send the new {}{}{} file created on this folder to another machine with internet\n" 
            "access. the file is very secure and it can be sent/stored anywere.".format(Fore.LIGHTCYAN_EX,
            Fore.LIGHTYELLOW_EX,output_name,Fore.LIGHTCYAN_EX))

            print(Fore.LIGHTGREEN_EX + "Package was saved successfully as {} !".format(output_name))
            

def unpack_data(file_name, private_key_path=None, key_password=None):

    print(Fore.LIGHTMAGENTA_EX + "\n\n# ------------------------------------------------------\n"
          "# Warning the extractor module is not secure against erroneous or\n"
          "# maliciously constructed data. Never unpack data received from an\n"
          "# untrusted or unauthenticated source.\n"
          "# ------------------------------------------------------\n\n")

    enc_key = base64.b85decode(get_key_data("PRIVATE", private_key_path))
    if key_password:
        password = key_password
    else:
        password = getpass.getpass("Insert the key's password: ").encode()

    dec_key = None
    try:
        f = Fernet(password)
        dec_key = f.decrypt(enc_key)
    except Exception as e:
        print(Fore.RED + "Decryption failed - Check if the key's password is correct: \n" + str(e))
        exit(668)

    private_key = serialization.load_pem_private_key(
        dec_key,
        password=None,
        backend=default_backend()
    )

    if not private_key:
        print(Fore.RED + "Could not load the public key")
        exit(667)

    with open(file_name,"rb") as file:
        encrypted = file.read()

        hmac_hash = encrypted[-64:]
        encrypted_password = (encrypted[:-64])[-1024:]

        key_password = private_key.decrypt(
            encrypted_password,
            ass_padding.OAEP(
                mgf=ass_padding.MGF1(algorithm=hashes.SHA512()),
                algorithm=hashes.SHA512(),
                label=None
            )
        )

        cipher_text = encrypted[:-1088]

        digest = hashes.Hash(hashes.SHAKE128(16), backend=default_backend())
        digest.update(key_password)
        salt = digest.finalize()

        # Real key digested from the key_password
        kdf_kp = PBKDF2HMAC(algorithm = hashes.SHA512(),
                         length = 32,
                         salt = salt,
                         iterations = 1000,
                         backend = default_backend())

        key = kdf_kp.derive(key_password)


        # ChaCha20 Nonce
        kdf_n = PBKDF2HMAC(algorithm = hashes.SHA256(),
                         length = 16,
                         salt = salt,
                         iterations = 200,
                         backend = default_backend())

        nonce = kdf_n.derive(key)

        # AES CBC Init vector
        kdf_iv = PBKDF2HMAC(algorithm=hashes.SHA256(),
                         length=16,
                         salt=salt,
                         iterations=200,
                         backend=default_backend())

        iv = kdf_iv.derive(nonce + key)

        # HMAC Derivated key
        kdf_hmac = PBKDF2HMAC(algorithm=hashes.SHA256(),
                         length=32,
                         salt=salt,
                         iterations=200,
                         backend=default_backend())

        hmac_key = kdf_hmac.derive(iv + key)

        try:
            h = hmac.HMAC(hmac_key, hashes.SHA512(), backend=default_backend())
            h.update(cipher_text)
            h.verify(hmac_hash)
        except:
            print(Fore.RED + "Could not authenticate data pack")
            exit(667)

        print(Fore.GREEN + "Valid data")

        # AES
        cipher_aes = Cipher(algorithms.AES(key), modes.CBC(iv), backend=default_backend())
        decryptor = cipher_aes.decryptor()
        chacha_encrypted = decryptor.update(cipher_text) + decryptor.finalize()

        # CHACHA
        chacha_alg = algorithms.ChaCha20(key, nonce)
        cipher_chacha = Cipher(chacha_alg, mode=None, backend=default_backend())
        decryptor = cipher_chacha.decryptor()
        compressed_padded = decryptor.update(chacha_encrypted)

        # PKCS7 padding
        unpadder = padding.PKCS7(256).unpadder()
        data = unpadder.update(compressed_padded)
        compressed = data + unpadder.finalize()
        ## =====


        try:
            data = lzma.decompress(compressed)
        except Exception as e:
            var = traceback.format_exc()
            raise Exception("Decompress A {} \n {}".format(str(var), str(e)))

    print("Done!")
    data = b""
    try:
        data = pickle.loads(data)
    except Exception as e:
        print(Fore.RED + "Error while unserializing")
        var = traceback.format_exc()
        raise Exception("Unpack Serial {} \n {}".format(str(var), str(e)))

    return data


def migrate_package():
    print("[*] This process will migrate the current keys of a data package to another keypair ")
    name = get_filename(False)
    input("[*] You will now decrypt {} Using the OLD Keypair [press Enter to continue]".format(name))
    data = unpack_data(name)
    input("[*] You will now encrypt {} Using the NEW Keypair [press Enter to continue]".format(name))
    pack_data(data)



def upload(data_pack, generation_data):
    connected = False

    for i in range(10):
        try:
            req = requests.get(api_url.format("retrieve?generation_id=0"))
            if req.status_code == 404:
                connected = True
                break
        except Exception as e:
            print(Fore.LIGHTRED_EX + "Exception while trying to connect to the internet\n")
            break


    if not connected:
        print(Fore.LIGHTRED_EX + "No internet connection, manually submit the datapacked created on the script folder")
        return False
    else:
        print(Fore.GREEN + "Connected to the internet")

    #Data pack data
    binary_blob = b''
    try:
        binary_blob = base64.b64encode(data_pack).decode('utf-8') + '==='
    except Exception as e:
        print(Fore.LIGHTRED_EX + "Error while tring to encode data" + str(e))
        return False

    req = {
        "timestamp": time.ctime(),
        "customer_name": generation_data["customer_name"],
        "customer_contacts" : generation_data["customer_contacts"],
        "partner_contacts": generation_data["partner_contacts"],
        "partner_name": generation_data["partner_name"],
        "trend_contacts": generation_data["trend_contacts"],
        "modules": generation_data["modules"], # lembrar de colocar todos
        "language":generation_data["language"],
        "data_pack": binary_blob,
        "msg_checksum": "not-used"
    }
    try:
        res = requests.post(api_url.format("generate"), data=json.dumps(req))
    except:
        print(Fore.LIGHTRED_EX + "Connection lost, try again later!")
        return False

    json_res = json.loads(res.content.decode())
    generation_id = json_res.get('generation_id', None)
    print(Fore.LIGHTBLUE_EX + "Data pack sent to the Cloud for processing!")
    
    return get_report(generation_id,False)

    
def get_report(generation_id, check_connection=True):
    connected = False

    if check_connection:
        for i in range(10):
            req = requests.get(api_url.format("retrieve?generation_id=0"))
            if req.status_code == 404:
                connected = True
                break

        if not connected:
            print(Fore.LIGHTRED_EX + "No internet connection, manually submit the datapacked created on the script folder")
            return False
        else:
            print(Fore.GREEN + "Connected to the internet")

    if generation_id != None:
        print("Waiting for {}".format(generation_id))
        for i in range(100):
            time.sleep(10)

            try:
                req = requests.get(api_url.format("retrieve?generation_id=" + generation_id))
            except:
                print("Connection error, trying again...")
                continue

            if req.status_code == 404:
                #Not ready
                print(".", end='')
                continue
            
            try:
                url = req.content.decode('utf-8')
            except:
                print(Fore.LIGHTRED_EX + "Malformed URL try again later")
                return False

            print(Fore.GREEN + "\nReport is ready!")
            print(Fore.LIGHTGREEN_EX + "Downloading the report!")
            name = "report-{}.zip".format(random.randint(0,999))
            with open(name, 'wb') as r:
                try:
                    report = requests.get(url)
                except:
                    print("Error while downloading, trying again...")
                    continue
                
                if report.status_code == 200:
                    try:
                        r.write(report.content)
                    except Exception as e:
                        print(Fore.LIGHTRED_EX + "Error while tring to write to file " + str(e))
                        return False
                        
                    print(Fore.LIGHTMAGENTA_EX + "Saved your new report as {}!".format(name))
                    return True
                else:
                    print(Fore.LIGHTRED_EX + "Error on request {} \n\n".format(url))
                    print(Fore.LIGHTCYAN_EX + "This may happen, try getting the results again in one minute with the command --get with this id: {}".format(generation_id))
                    with open("GENERATION_ID.txt","w+") as file:
                        file.write(str(generation_id))
                    return False
            break
        
        if not check_connection:
            print(Fore.LIGHTRED_EX + "Report generation timed out after 16 minutes, probably firewall or internet issue")
            print(Fore.LIGHTRED_EX + "You may try to parse only the report later using ./extractor --get " + str(generation_id))
            print(Fore.LIGHTCYAN_EX + "Try again later using this ID (save this value) {}".format(generation_id))

            with open("GENERATION_ID.txt","w+") as file:
                file.write(str(generation_id))
        else:
            print(Fore.LIGHTRED_EX + "Report generation timed out after 16 minutes, probably firewall or internet issue")
            print(Fore.LIGHTRED_EX + "If you tried more than one time and the report did not get ready, it may had some issues,\n"
            "Please reach us at alloflardsbpg@trendmicro.com")
        return False
    print(Fore.LIGHTRED_EX + "Error while trying to connect to remote service")
    return False
                

def manual_submit(file_name):
    if not os.path.exists(file_name):
        print(Fore.LIGHTRED_EX + "The file does not exists")
        exit(-1)

    with open(file_name,"rb") as file:
        data = file.read()
        print("{}Due to the packed being encrypted we cannot access the customer information to aid generation,\n"
        "{}Please fill these infos precisely, they will appear on the report".format(Fore.LIGHTCYAN_EX, Fore.LIGHTRED_EX))
        generation_data = dl.get_customer_info()     

        if not upload(data, generation_data):
            print("Could not generate")
            print(Fore.LIGHTRED_EX + "If you tried more than one time and the report did not get ready, some issues might had happened,\n"
            "Please reach us at alloflardsbpg@trendmicro.com with your .dat file")
            exit(-1)
    

if __name__ == '__main__':
    # if len(sys.argv) > 1 :
    #     if str(sys.argv[1]) != "":
    #         print(Fore.LIGHTBLUE_EX + "Checking if the report " + str(sys.argv[1]) + " is ready!")
    #         print(Fore.YELLOW + "If the ID is wrong it will timeout after 16 minutes")
    #         get_report(str(sys.argv[1]))

    parser = argparse.ArgumentParser(prog="extractor", formatter_class=argparse.RawDescriptionHelpFormatter ,epilog=constants.EXTRACTOR_HELP_STRING )
    #parser.add_argument('--silent','-s', action='store_true', help="Run without interactive prompt")
    parser.add_argument('--get', '-g', help="Attempts to download a report of an already submitted pack using the ID")
    parser.add_argument('--send', '-p', help="Submit a data pack file for report generation, recieves ID")
    parser.add_argument('--notsend', '-n', action='store_false', help="Do not send for remote processing, just generate .dat")
    parser.add_argument('--unencrypted', '-u', action='store_true', help="Generate an UNENCRYPTED version of the Datapack as a json file")
    #parser.add_argument('--key', '-k', help="Path to the public key")
    parser.add_argument('--version', '-v',action='store_true', help='Print version and exit')
    args = parser.parse_args()
    print(Fore.LIGHTMAGENTA_EX + "Aways check if you are running the latest version, current: {}!".format(str(constants.EXTRACTOR_VERSION)))
    if args.version:
        print(constants.EXTRACTOR_VERSION)
        input("--[Press enter to exit]--")
        exit(0)
    if args.get is not None:
        get_report(args.get)
        input("--[Press enter to exit]--")
        exit(0)    
    if args.send is not None:
        manual_submit(args.send)
        input("--[Press enter to exit]--")
        exit(0)    
    '''
    if args.silent is not None:
        print("{}Not Yet implemented, Expected on Extractor 1.8.1".format(Fore.LIGHTRED_EX))
        raise NotImplementedError
    if args.key is not None:
        print("{}Not Yet implemented, Expected on Extractor 1.8.1".format(Fore.LIGHTRED_EX))
        raise NotImplementedError
    '''    
    #TODO No-wizard / silent mode
    pack_data(unencrypted=args.unencrypted,send_now=args.notsend)
    input("--[Press enter to exit]--")
