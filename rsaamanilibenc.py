from Crypto.PublicKey import RSA
from Crypto.Cipher import PKCS1_OAEP
import binascii


keyPair = RSA.generate(1025)
# print(keyPair)

pubKey = keyPair.publickey()
# print(f"Public key:  (n={hex(pubKey.n)}, e={hex(pubKey.e)})")

pubKeyPEM = pubKey.exportKey()
print(pubKeyPEM.decode('ascii'))
print("\n")
file = open("public.pem", "wb")
file.write(pubKeyPEM)
file.close

# print(f"Private key: (n={hex(pubKey.n)}, d={hex(keyPair.d)})")
privKeyPEM = keyPair.exportKey()
print(privKeyPEM.decode('ascii'))
print("\n")
file = open("private.pem", "wb")
file.write(privKeyPEM)
file.close()

message_plain = bytes(str("Enter text to encode: "), "utf-8")
encryptor = PKCS1_OAEP.new(pubKey)
message_encrypted = encryptor.encrypt(message_plain)
print("Encrypted:", binascii.hexlify(message_encrypted))
print("\n")

private_key = RSA.import_key(open("private.pem").read())
decryptor = PKCS1_OAEP.new(private_key)
message_decrypted = decryptor.decrypt(message_encrypted)
print("Decrypted:", binascii.hexlify(message_decrypted))
# print("\n")