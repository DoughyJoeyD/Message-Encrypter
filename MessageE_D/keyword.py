from ciphers import Cipher
from utilities import Utilities
import string


class KeyWord(Cipher):
    """
    The KeyWord Cipher class can encrypt or decrypt a message given a
    chosen keyword, hence the name. This is the class for said cipher
    """
    def __init__(self):
        self.utilities = Utilities()


    def __key(self, keyword, action):
        encryption_key = {}
        plain = self.utilities.key_word_help("list")
        ciphertext = self.utilities.key_word_help("list")
        keyword_stripped = self.utilities.dont_repeat(keyword)
        for i in range(len(keyword_stripped)):
            ciphertext.remove(keyword_stripped[i])
        ciphertext = keyword_stripped + ciphertext
        if action == "encrypt":
            # generate encryption key
            for i in range(len(plain)):
                encryption_key[plain[i]] = ciphertext[i]
        elif action == "decrypt":
            # generate decryption key
            for i in range(len(plain)):
                encryption_key[ciphertext[i]] = plain[i]
        else:
            raise ValueError("How?")

        return encryption_key

    def __runit(self, cipher_key, message):
        output = []
        for letter in message:
            if letter not in cipher_key:
                output.append(letter)
            else:
                output.append(cipher_key[letter])

        return ''.join(output)

    def encrypt(self, user_input):
        message = user_input[0]
        keyword = user_input[1]
        cipher_key = self.__key(keyword, action="encrypt")
        return self.__runit(cipher_key, message)


    def decrypt(self, user_input):
        message = user_input[0]
        keyword = user_input[1]
        cipher_key = self.__key(keyword, action="decrypt")
        return self.__runit(cipher_key, message)
