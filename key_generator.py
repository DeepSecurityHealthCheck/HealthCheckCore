# o
from cryptography.hazmat.backends import default_backend
from cryptography.hazmat.primitives.asymmetric import rsa
from cryptography.hazmat.primitives import serialization
from cryptography.fernet import Fernet
import base64
import os
import hashlib
def generate_keys():

    print("[*] Generating key Pairs...")

    private_key = rsa.generate_private_key(
        public_exponent=65537,
        key_size=8192,
        backend=default_backend()
    )
    public_key = private_key.public_key()


    pem = private_key.private_bytes(
        encoding=serialization.Encoding.PEM,
        format=serialization.PrivateFormat.PKCS8,
        encryption_algorithm=serialization.NoEncryption()
    )

    key = Fernet.generate_key()

    print("======>>>> YOUR PRIVATE KEY PASSWORD IS <<<<======\n")
    print(key.decode())
    print("\n=======>>>> COPY SOMEWERE SAFE <<<<=======")
    input("[*] Press enter to continue")

    f = Fernet(key)
    token = f.encrypt(pem)
    token = base64.b85encode(token)
    
    pem = public_key.public_bytes(
        encoding=serialization.Encoding.PEM,
        format=serialization.PublicFormat.SubjectPublicKeyInfo
    )


    if not os.path.exists("keys"):
        os.makedirs("keys")
    
    private_key_filename="PRIVATE_key.pem"
    public_key_filename="PUBLIC_key.pem"

    private_key_path="keys/"+private_key_filename
    public_key_path = "keys/"+public_key_filename


    if os.path.exists(private_key_path) or os.path.exists(public_key_path):
        print("[!] WARNING: Found Existing Key Files\n")
        hash = hashlib.md5(str(token).encode('utf-8')).hexdigest()
        private_key_path="keys/"+hash[0:4]+"_"+private_key_filename
        public_key_path="keys/"+hash[0:4]+"_"+public_key_filename
        print("[*] The new pair will be created as:\n\t{}\n\t{}\n".format(private_key_path,public_key_path))

    with open(private_key_path, 'wb') as f:
        f.write(token)
    with open(public_key_path, 'wb') as f:
        f.write(pem)
    print("=======>>>> DO NOT SHARE YOUR PRIVATE KEY! <<<<=======")
    print("[*] Done.")
