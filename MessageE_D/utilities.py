import string
class Utilities():
    """ Used throught the ciphers to aid in the process """
# Creates Alphabet when called all uppercase to look nice
    def key_word_help(self, type=None):
        if type is None or type == "string":
            alpha = string.ascii_uppercase
        elif type == "list":
            alpha = list(string.ascii_uppercase)
        return alpha

# Checks to make sure letters dont repeat
    def dont_repeat(self, text):
        letters = []
        for letter in text:
            if letter not in letters:
                letters.append(letter)

        return letters

# Polybius needs a table to encrypt, this creates that table        
    def poly_help(self):
        alpha = self.key_word_help()
        x = 1
        y = 1
        polybius = {}

        for letter in alpha:
            polybius[letter] = [x, y]
            if not letter == "I":
                x += 1
            if x > 5:
                x = 1
                y += 1

        return polybius
