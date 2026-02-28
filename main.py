from aes_module import AESHandler
from rsa_module import RSAHandler
from sha_module import sha256_hash

aes = AESHandler()
rsa = RSAHandler()

while True:
    print("\n--- Cryptography Toolkit ---")
    print("1. AES Encrypt")
    print("2. AES Decrypt")
    print("3. RSA Encrypt")
    print("4. RSA Decrypt")
    print("5. SHA-256 Hash")
    print("6. Exit")

    choice = input("Choose option: ")

    if choice == "1":
        text = input("Enter text: ")
        print("Encrypted:", aes.encrypt(text))

    elif choice == "2":
        text = input("Enter ciphertext: ")
        print("Decrypted:", aes.decrypt(text))

    elif choice == "3":
        text = input("Enter text: ")
        print("Encrypted:", rsa.encrypt(text))

    elif choice == "4":
        text = input("Enter ciphertext: ")
        print("Decrypted:", rsa.decrypt(text))

    elif choice == "5":
        text = input("Enter text: ")
        print("SHA-256:", sha256_hash(text))

    elif choice == "6":
        break

    else:
        print("Invalid option")