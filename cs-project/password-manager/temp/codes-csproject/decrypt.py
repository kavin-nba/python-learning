from crypto.cipher import AES
import hashlib

password = "mypassword".encode()
key = hashlib.sha224(password).digest()
mode = AES.MODE_CBC
IV = "this is an IV456"

cipher = AES.new(key, mode, IV)

decrypt_text = cipher.decrypt()

decrypt_text_pad = decrypt_text.strip().decode()

print(decrypt_text_pad)