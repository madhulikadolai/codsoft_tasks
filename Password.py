import random
import string

print("===== PASSWORD GENERATOR =====")

length = int(input("Enter password length: "))

characters = (
    string.ascii_letters +
    string.digits +
    string.punctuation
)

if length <= 0:
    print("Password length must be greater than 0.")

else:
    password = ""

    for i in range(length):
        password += random.choice(characters)

    print("\nGenerated Password:")
    print(password)
