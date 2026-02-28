from Crypto.Cipher import AES
from Crypto.Util.Padding import pad, unpad
from Crypto.Random import get_random_bytes
import base64

class AESHandler:
    def __init__(self):
        self.key = get_random_bytes(16)  # 128-bit key

    def encrypt(self, plaintext):
        cipher = AES.new(self.key, AES.MODE_CBC)
        ct_bytes = cipher.encrypt(pad(plaintext.encode(), AES.block_size))
        return base64.b64encode(cipher.iv + ct_bytes).decode()

    def decrypt(self, ciphertext):
        raw = base64.b64decode(ciphertext)
        iv = raw[:16]
        ct = raw[16:]
        cipher = AES.new(self.key, AES.MODE_CBC, iv)
        return unpad(cipher.decrypt(ct), AES.block_size).decode()