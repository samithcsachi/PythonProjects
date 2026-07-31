import random
import string


def generate_password():
    length = input("Enter the desired password length: ").strip()
    if not length.isdigit() or int(length) <= 0:
        print("Please enter a valid positive integer for the password length.")
        return
    length = int(length)
    include_uppercase = input("Include uppercase letters? (y/n): ").strip().lower()
    include_digits = input("Include digits? (y/n): ").strip().lower()
    include_special = input("Include special characters? (y/n): ").strip().lower()

    if length < 4:
        print("Password length should be at least 4 characters.")
        return
    lower = string.ascii_lowercase
    upper = string.ascii_uppercase if include_uppercase == "y" else ""
    special = string.punctuation if include_special == "y" else ""
    digits = string.digits if include_digits == "y" else ""
    all_characters = lower + upper + special + digits 

    required_characters = []
    if include_uppercase == 'y':
        required_characters.append(random.choice(upper)) 
    if include_special == 'y':
        required_characters.append(random.choice(special))
    if include_digits == 'y':
        required_characters.append(random.choice(digits))

    remaining_length = length - len(required_characters)
    password = required_characters

    for _ in range (remaining_length):
       character=  random.choice(all_characters) 
       password.append(character)
    random.shuffle(password)

    str_password = "".join(password)

    return str_password




def main():
    print("Hello from random-password-generator!")
    password = generate_password()
    print(password)


if __name__ == "__main__":
    main()
