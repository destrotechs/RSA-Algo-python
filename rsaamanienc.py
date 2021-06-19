from decimal import Decimal

class Encrypt:

    def __init__(self, plaintext = "",n=0,e=0.0):
        self.plaintext = plaintext
        self.n = n
        self.e = Decimal(e)

        

        
    
    def convert_string_to_bin(self, text):
        binary = ''.join(format(ord(x), 'b') for x in text)
        print(f"Plaintext: {text}\nBinary: {binary}")
        return binary

    # def convert_binary_to_string(self, binary_string):
    #     ascii_string = "".join([chr(int(binary, 2)) for binary in binary_string.split(" ")])
    #     print(asc)

    def binaryToDecimal(self, binary):
        # print(binary)
        # binary =str(binary)
        # print(binary)
        # decimal, i, n = 0, 0, 0
        # while(binary != 0):
        #     dec = binary % 10
        #     decimal = decimal + dec * pow(2, i)
        #     binary = binary//10
        #     i += 1
        decimal = 0
        binary = str(binary)
        for digit in binary:
            decimal = decimal * 2 + int(digit)
        
        print(f"Binary: {binary}\nDecimal: {decimal}")

        return decimal
    
    def decimalToBinary(self, n): 
        binary = "{0:b}".format(n)
        print(f"Decimal: {n}\nBinary: {binary}")
        return 
    
    def convert_string_to_binary(self, inputString):
        # This method converts characters to binary form
        binary = bin(int.from_bytes(inputString.encode(), 'big'))[2:]
        print("\n{} in binary: {}\n".format(inputString, binary))
        return binary

    def convert_binary_to_string(self, binary):
        # This method converts a binary to characters
        binary = str(binary)
        final = ""
        for i in range(0, len(binary), 8):
            bytes = binary[i:i+7]
            decstring = int(bytes, 2)
            final += chr(decstring)

        print("\n{} to string: {}\n".format(binary, final))
        return final
    def calculate_cipher_text(self, message_decimal):
        print("message decimal : ",message_decimal)
        print("self.e ",self.e)
        print("self.n : ",self.n)
        self.ciphertext = (pow(message_decimal,self.e))%int(self.n)
        return self.ciphertext
    def cipher_to_hex(self,n):
        print("=======cipher to hex=====")
        print("cipher text : ",n)

        x = ''.join(format(ord(x), 'b') for x in str(n))

        print("cipher to binary : ",x)

        x = int(x)
        x=hex(x)
        print("Cipher to hexadecimal : ",x)
        x = ''.join(format(ord(x), 'b') for x in str(x))
        print("Hex Cipher to binary back : ",x)

        




rec_key = str(input("Enter the recipient's public key, [TWO VALUES SEPERATED BY COMMA (,)] \n"))
n = rec_key.split(",")[0]
e =rec_key.split(",")[1]

# recipient_pub_key = (n,e)

plaintext = str(input("Enter text to encrypt : \n"))


enc = Encrypt(plaintext,n,e)
message_binary = enc.convert_string_to_binary(plaintext)


message_decimal = enc.binaryToDecimal(message_binary)

cipher_text = enc.calculate_cipher_text(message_decimal)

print("CIPHER TEXT :" ,cipher_text)
enc.cipher_to_hex(cipher_text)
