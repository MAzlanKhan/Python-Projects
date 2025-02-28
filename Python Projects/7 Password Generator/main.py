import random

length = 10
chars = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ~`!@#$%^&*()_-+;:\|,.0123456789'
password = ""
print("Generate Your Password")

UserChoice = input("Do you want to generate a Random Password? (Yes or No):  ").lower().strip()
if UserChoice in ["yes", "y"]:
    for pwd in range(length):
        password += random.choice(chars)
    print("Generated Password:", password, end="\r")

else:
    print("Okay!")