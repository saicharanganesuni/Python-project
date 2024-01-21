import random
import string

def generate_password(length=12):
    characters = string.ascii_letters + string.digits + string.punctuation
    password = ''.join(random.choice(characters) for _ in range(length))
    return password

def generate_multiple_passwords(num_passwords=1, length=12):
    passwords = [generate_password(length) for _ in range(num_passwords)]
    return passwords

if __name__ == "__main__":
    try:
        # Get user input for password length and quantity
        password_length = int(input("Enter the desired password length: "))
        num_passwords = int(input("Enter the number of passwords to generate: "))

        # Generate and display passwords
        passwords = generate_multiple_passwords(num_passwords, password_length)
        print("\nGenerated Passwords:")
        for i, password in enumerate(passwords, start=1):
            print(f"Password {i}: {password}")

    except ValueError as e:
        print("Error: Please enter valid numeric values for password length and quantity.")
'''
in this code, we define a function generate_password() that generates a random password of a specified length.
genearted passwords are stored in a list passwords and are displayed using a for loop.
generated_mutilple_passwords() function takes two arguments: num_passwords and length and prints required number of passwords.
The above passwords consists of alphabets, digits, and special characters.
'''