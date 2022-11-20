# AES 256 encryption/decryption using pycryptodome library
# source: https://qvault.io/cryptography/aes-256-cipher-python-cryptography-examples/

from base64 import b64encode, b64decode
import hashlib
from Cryptodome.Cipher import AES
import os
from Cryptodome.Random import get_random_bytes
import random
import string


def encrypt(plain_text, password):
    # generate a random salt
    salt = get_random_bytes(AES.block_size)

    # use the Scrypt KDF to get a private key from the password
    private_key = hashlib.scrypt(
        password.encode(), salt=salt, n=2 ** 14, r=8, p=1, dklen=32)

    cipher_config = AES.new(private_key, AES.MODE_GCM)

    # return a dictionary with the encrypted text
    cipher_text, tag = cipher_config.encrypt_and_digest(bytes(plain_text, 'utf-8'))
    return {
        'cipher_text': b64encode(cipher_text).decode('utf-8'),
        'salt': b64encode(salt).decode('utf-8'),
        'nonce': b64encode(cipher_config.nonce).decode('utf-8'),
        'tag': b64encode(tag).decode('utf-8')
    }


def decrypt(enc_dict, password):
    # decode the dictionary entries from base64
    salt = b64decode(enc_dict['salt'])
    cipher_text = b64decode(enc_dict['cipher_text'])
    nonce = b64decode(enc_dict['nonce'])
    tag = b64decode(enc_dict['tag'])

    # generate the private key from the password and salt
    private_key = hashlib.scrypt(
        password.encode(), salt=salt, n=2 ** 14, r=8, p=1, dklen=32)

    # create the cipher config
    cipher = AES.new(private_key, AES.MODE_GCM, nonce=nonce)

    # decrypt the cipher text
    decrypted = cipher.decrypt_and_verify(cipher_text, tag)

    return decrypted.decode()


def main():
    for i in range(1):
        password = ''.join(random.choices(string.ascii_uppercase + string.digits, k=16))
        # password = input("Password: ")
        # First let us encrypt secret message
        encrypted = encrypt("Abhisaran", password)
        if '.' in str(encrypted):
            print("TRUEE")

        print(encrypted)
        # when storing to database dictionary will be converted to string automatically
        encrypted_str = encrypted._str_()
        print(encrypted_str)
        # Using eval is very unsafe
        print(decrypt(eval(encrypted_str), password))

        # Let us decrypt using our original password
        # decrypted = decrypt(encrypted, password)
        # print(bytes.decode(decrypted))

main()

# from pm-security.fernet import Fernet
#
# key = Fernet.generate_key()
#
# def encryption():
#
#
#
#
# def decryption():