import binascii
import logging as log
import base64
from cryptography.hazmat.backends import default_backend

from cryptography.hazmat.primitives.kdf.pbkdf2 import PBKDF2HMAC
from cryptography.hazmat.primitives.ciphers import Cipher, algorithms, modes
from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.primitives import padding

import os
import json


def gen_aes_key():
    key = os.urandom(16)  # 16 bytes / 128 bits

    processed_key = binascii.hexlify(key)
    return {"key": processed_key}

# criar senha e colocar em B64 na chave "key"
# pegar data_to_cypt (json data dsm) e criptografar com um IV e salt
# criar Json com IV (iv), SALT (s) e cyphertext em b64 (ct) gerar b64 de tudo

def pack_data(crypt_data, aes_key=None):
    data = crypt_data
    
    if aes_key is not None:
        processed_key = aes_key['key']
    else:
        key = os.urandom(16)
        processed_key = binascii.hexlify(key)
    
    iv = os.urandom(16)
    processed_iv = binascii.hexlify(iv)

    padder = padding.PKCS7(128).padder()
    data_padded = padder.update(data)
    data_padded += padder.finalize()

    cipher_aes = Cipher(algorithms.AES(processed_key), modes.CBC(iv), backend=default_backend())
    encryptor_aes = cipher_aes.encryptor()
    cypher = encryptor_aes.update(data_padded) + encryptor_aes.finalize()

    b64_data = base64.b64encode(cypher)

    json_data = dict()
    json_data["ct"] = b64_data.decode("UTF-8")
    json_data["iv"] = processed_iv.decode("UTF-8")

    json_data64 = base64.b64encode(json.dumps(json_data).encode("UTF-8"))

    outer_json = dict()
    # outer_json["key"] = processed_key.decode("UTF-8")
    outer_json["encrypted_data"] = json_data64.decode("UTF-8")

    ready = json.dumps(outer_json)

    return ready
    '''
    with open("bpg_data.json", "wt+") as out:
        out.write(ready)

    log.info("Done!")



test = dict()
test["blabla"] = "blabla"
test["ebleeble"] = "bluble"
pack_data(json.dumps(test))
'''
