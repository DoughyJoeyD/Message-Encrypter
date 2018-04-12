import os
import sys
import time
import caesar
import keyword
import atbash
import polybius
import utilities
import string

# Clear Screen Function does what its called
def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

#displays welcome message
def start():
    clear_screen()
    print("Welcome to Cipher Generator 1.0")
    time.sleep(2)
    # clear screen again
    clear_screen()


# this is the end fuction which tells the user its closing and says Goodbye
def end():
    clear_screen()
    count = 3
    while count:
        clear_screen()
        sys.stdout.write(
            "This program will close in {:2d} seconds...".format(
                count))
        sys.stdout.flush()
        time.sleep(1)
        count -= 1
    clear_screen()

# The meat of the program
def the_program():
    available_ciphers = {
    1: "Caesar",
    2: "KeyWord",
    3: 'AtBash',
    4: 'Polybius',
    0: 'Quit(NOT CIPHER)'
    }
    program_running = True
    leader = "-"

    while program_running:

        print("Available Ciphers: ")

        for option, cipher in available_ciphers.items():
            print("{}: {}".format(option, cipher))

        print("Pick a Cipher by choosing a number!\n"
              "Enter 0 to quit.\n")

        user_input = input("Enter Number: ")

        if user_input == 0:
            break

        if user_input in available_ciphers:
            execute = True
            clear_screen()
            selected_cipher = available_ciphers[user_input]

            while execute:
                options = {
                    1: "Encrypt",
                    2: "Decrypt"
                    }
                print("Thanks, You selected {}!\n"
                      "Will you be Encrypting or decrypting?".format(str.capitalize(selected_cipher)))
                time.sleep(3)
                clear_screen()
                print("Encrypt=1 - Decrypt=2")
                time.sleep(2)
                encdec = input()
                clear_screen()
                action = options[encdec]
                print("--Enter Your Message--")
                text_to_use = str.upper(raw_input(selected_cipher + "-" + options[encdec]+ ": "))

                if selected_cipher.upper() == "CAESAR":
                    instance = caesar.Caesar()
                elif selected_cipher.upper() == "KEYWORD":
                    instance = keyword.KeyWord()
                    cipher_keyword = str.upper(raw_input("Enter Keyword: "))
                    text_to_use = [text_to_use, cipher_keyword]
                elif selected_cipher.upper() == "ATBASH":
                    instance = atbash.AtBash()
                elif selected_cipher.upper() == "POLYBIUS":
                    instance = polybius.Polybius()
                #Wont Work Until above commands create instances
                if action == "Encrypt":
                    clear_screen()
                    print("Heres your Message")
                    print(instance.encrypt(text_to_use))
                else:
                    print(instance.decrypt(text_to_use))
                programPause = raw_input("Press the <ENTER> key to continue...")
                clear_screen()
                execute = False
        program_running = False
    again()

# Asks the user if they want to encrypt more
def again():
    yes = {'yes','y', 'ye', ''}
    no = {'no','n'}
    print("Encrypt/Decrypt More?: ")
    choice = raw_input("Enter Yes or No: ").lower()
    if choice in yes:
        clear_screen()
        the_program()
    elif choice in no:
        clear_screen()
        print("Thanks for Using Chipher Generator 1.0")
        time.sleep(2)
    else:
        sys.stdout.write("Please respond with 'yes' or 'no'")
        clear_screen()
        again()
        
# Allows us to import without executing
if __name__ == '__main__':
    start()
    the_program()
    end()
