from ciphers import Cipher
from utilities import Utilities
import re


class Polybius(Cipher):
    def __init__(self):
        self.utilities = Utilities()

    def encrypt(self, message):
        output = []
        polybius = self.utilities.poly_help()

        for character in message:
            if str.isalpha(character):
                pair = polybius[character]
                for char in pair:
                    output.append(str(char))
            elif character == " ":
                output.append(character)

        return ''.join(output)

    def decrypt(self, message):
        polybius = self.helpers.polybius_square()
        output = []
        convert_spaces = re.sub("[ ]", "::", message)
        n = 2
        pairs_list = [convert_spaces[i:i + 2] for i in range(0, len(convert_spaces), 2)]
        for pair in pairs_list:
            if pair == "::":
                output.append(" ")
            else:
                value_to_match = [int(x) for x in pair]
                for key, value in polybius.items():
                    if value == value_to_match:
                        output.append(key)

        return ''.join(output)
