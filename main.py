import random
import string

def generate_password(min_length, numbers=True, special_characters=True):
    letters = string.ascii_letters
    digits = string.digits
    special = string.punctuation

    characters = letters
    if numbers:
        characters += digits
    if special_characters:
        characters += special

    pwd = ''
    has_number = False
    has_special = False

    while True:
        new_char = random.choice(characters)
        pwd += new_char

        if new_char in digits:
            has_number = True
        if new_char in special:
            has_special = True

        meets_criteria = len(pwd) >= min_length
        if numbers:
            meets_criteria = meets_criteria and has_number
        if special_characters:
            meets_criteria = meets_criteria and has_special

        if meets_criteria:
            break

    return pwd


min_length = int(input("Enter minimum password length: "))
has_numbers = input("Include numbers? (y/n): ").lower() == 'y'
has_specials = input("Include special characters? (y/n): ").lower() == 'y'

pwd= generate_password(min_length, has_numbers, has_specials)
#print("Generated password:", pwd)

if __name__ == "__main__":
    print('Generated password:', pwd)
