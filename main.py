# Anthony Roig
def encoder(word):
    encoded_word = ""
    # for loop for encoding each digit in string
    for char in word:
        encoded_word = encoded_word + str((int(char) + 3) % 10)  # shifting 3 digit
    print("Your password has been encoded and stored!")
    return encoded_word

def decoder(word):
    pass

def main():
    while True:
        print("Menu")
        print("-------------")
        print("1. Encode")
        print("2. Decode")
        print("3. Quit")
        menu_var = input("Please enter an option: ")
        if menu_var == "1":
            password = input("Please enter your password to encode: ")
            encoder(password)
        elif menu_var == "2":
            decoder(password)
        elif menu_var == "3":
            break
        else:
            print("Invalid input")


if __name__ == '__main__':
    main()

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
