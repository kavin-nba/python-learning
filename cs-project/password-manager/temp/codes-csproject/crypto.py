from crypto.cipher import AES
import hashlib

password = "mypassword".encode()
key = hashlib.sha224(password).digest()
mode = AES.MODE_CBC
IV = "this is an IV456"

def pad_message():
    while len(message) % 16 != 0:
         message = message + " "
    return message

cipher = AES.new(key, mode, IV)

message = "this message is secret"
padded_message = pad_message(message)

encrypted_message = cipher.encrypt(padded_message)
