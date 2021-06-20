from Crypto.PublicKey import RSA
from Crypto.Cipher import PKCS1_OAEP
import binascii
import os

class Keys:
    def __init__(self,key_size):
        key_size = int(key_size)
        self.keyPair = RSA.generate(key_size)
        self.getPublicKey()
# print(keyPair)
    def getPublicKey(self):
        self.pubKey = self.keyPair.publickey()
# print(f"Public key:  (n={hex(pubKey.n)}, e={hex(pubKey.e)})")
        # self.getPubPem()
    def getPubPem(self):
        self.pubKeyPEM = self.pubKey.exportKey()
        print(self.pubKeyPEM.decode('ascii'))
        print("\n")
        file = open("public.pem", "wb")
        file.write(self.pubKeyPEM)
        file.close

        # print(f"Private key: (n={hex(pubKey.n)}, d={hex(keyPair.d)})")
        self.privKeyPEM = self.keyPair.exportKey()
        print(self.privKeyPEM.decode('ascii'))
        print("\n")
        file = open("private.pem", "wb")
        file.write(self.privKeyPEM)
        file.close()
    def encryptText(self, message_plain):
        # encryptor = PKCS1_OAEP.new(self.pubKey)
        # message_encrypted = encryptor.encrypt(message_plain)
        # ciphertext =binascii.hexlify(message_encrypted)
        # print("Encrypted:",ciphertext)
        # print("\n")
        # ciphertext = ciphertext.decode("utf-8")
        # return ciphertext
        recipient_key = RSA.import_key(open("public.pem").read())
        cipher_rsa = PKCS1_OAEP.new(recipient_key)
        enc_mes = cipher_rsa.encrypt(message_plain)
        ciphertext =binascii.hexlify(enc_mes)
        ciphertext = ciphertext.decode("utf-8")
        return ciphertext
    def decryptCipher(self,cipher):
        # print(cipher)
        # private_key = RSA.import_key(open("private.pem").read())
        # decryptor = PKCS1_OAEP.new(private_key)
        # message_decrypted = decryptor.decrypt(cipher)
        # message_decrypted = message_decrypted.decode("utf-8")
        # print("Decrypted:", message_decrypted)
        # return message_decrypted
        private_key = RSA.import_key(open("private.pem").read())
        cipher_rsa = PKCS1_OAEP.new(private_key)
        plaintext = cipher_rsa.decrypt(cipher)
        plaintext = plaintext.decode("utf-8")
        return plaintext
