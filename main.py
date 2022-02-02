from vignere import *

if __name__ == "__main__":
    print("""Hey, it is Vigenère cipher!
Use only alphabetic letters!""")
    while True:
        decision = input("Do you want to encrypt or decrypt? ")
        while decision not in ["encrypt", "decrypt"]:
            print("Your input is incorrect! Let's try again.")
            decision = input("Do you want to encrypt or decrypt? ")
        else:
            phrase = input(f"Write what are you going to {decision}: ")
            key_word = input("What is your key word: ")

        if decision == "encrypt":
            encrypted = encrypt(phrase, key_word)
            print(f"Your data is {decision}ed, it is: {encrypted}")
        elif decision == "decrypt":
            decrypted = decrypt(phrase, key_word)
            print(f"Your data is {decision}ed, it is: {decrypted}")

        cont = input("Do you want to try more?(Y/N) ")
        if cont != "Y":
            print("Good bye!")
            break
