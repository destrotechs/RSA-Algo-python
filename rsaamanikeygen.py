import rabin1

class RSA:

    def __init__(self, numberOfBits):
        self.numberOfBits = numberOfBits
        self.calculateN()
        self.calculateE()
        self.calculatePrivateKey()

    def getPrimeNumber(self):
        prime_number = rabin1.returnPrimeNumber(self.numberOfBits)
        return prime_number
    
    def calculateN(self):
        self.p = self.getPrimeNumber()
        self.q = self.getPrimeNumber()
        self.n = self.p * self.q
        print(f"P: {self.p}")
        print(f"Q: {self.q}")
        print(f"N: {self.n}")

    
    def calculateE(self):
         #calculating (p-1)(q-1)
        self.limit_e = (self.p - 1) * (self.q - 1)     
        # calculating 1<e<limit_e
        self.e =self.getValueOfE(self.limit_e)
        self.public_key = (self.n, self.e)

        #p(q-1)
    
    def calculatePrivateKey(self):
        # e mod (p-1)(q-1)
        temp_rem = self.e % self.limit_e
        self.d = 1 / temp_rem
        self.private_key = (self.n, self.d)
        print(f"Private key: {self.private_key}")

    def getValueOfE(self, n):
        new_limit_e =len('{:b}'.format(n))-1
        self.numberOfBits=new_limit_e
        prime_number = self.getPrimeNumber()

        print("New Prime number, value e: ",prime_number)
        return prime_number