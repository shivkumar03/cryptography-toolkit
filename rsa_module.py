from Crypto.PublicKey import RSA
from Crypto.Cipher import PKCS1_OAEP
import base64

class RSAHandler:
    def __init__(self):
        self.key = RSA.generate(2048)
        self.public_key = self.key.publickey()
        self.cipher = PKCS1_OAEP.new(self.public_key)
        self.decipher = PKCS1_OAEP.new(self.key)

    def encrypt(self, plaintext):
        encrypted = self.cipher.encrypt(plaintext.encode())
        return base64.b64encode(encrypted).decode()

    def decrypt(self, ciphertext):
        decrypted = self.decipher.decrypt(base64.b64decode(ciphertext))
        return decrypted.decode()