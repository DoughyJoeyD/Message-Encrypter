from ciphers import Cipher
from utilities import Utilities
import string

class AtBash(Cipher):
    """
    This is the AtBash Class for the Atbash cipher
    its functions are to Encrypt and Decrypt a message given by the user
    """

    def __init__(self):
        self.utilities = Utilities()

#The Encryption Function
    def encrypt(self, text):
        key1 = {}
        alphab = self.utilities.keyword_help()
        backalphab = self.utilities.keyword_help()[::-1]
        message_atbash = []

        for x in range(len(alphab)):
            key1[alphab[x]] = backalphab[x]

        for letter in text:
            if letter in key1:
                message_atbash.append(key1[letter])
            else:
                message_atbash.append(letter)


        return ''.join(message_atbash)
#The Decrypt Function
    def decrypt(self, text):

        key2 = {}
        message_atbash = []
        alphab = self.utilites.keyword_help()
        backalphab = self.utilites.keyword_help()[::-1]

        for x in range(len(alphab)):
            key2[backalphab[x]] = alphab[x]

        for letter in text:
            if letter not in key2:
                message_atbash.append(letter)
            else:
                message_atbash.append(key2[letter])

        return ''.join(message_atbash)
