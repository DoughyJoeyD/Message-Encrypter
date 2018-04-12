from ciphers import Cipher
from caesar import Caesar
import string

encrypt = 0
decrypt = 0
def start():
    global encrypt
    global decrypt
    start2 = raw_input("Would You like to Encrypt or Decrypt?: ").lower()
    if start2 == 'encrypt':
        encrypt +=1
    if start2 == 'decrypt':
        decrypt +=1
    if start2 == 'encrypt' or 'decrypt':
        print("Not what i asked for mate... Try again!")
    print start2.lower()
start()
