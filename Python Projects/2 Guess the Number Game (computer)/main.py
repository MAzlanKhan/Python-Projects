import random

def RandomNum(x):
    random_number = random.randint(1, x)    # Generate a random integer between 1 and 100
    # print(random_number)
    guess = 0
    while guess != random_number:
        guess = int(input("Guess the Number: "))
        if guess > random_number:
            print("Sorry, Guess Again. Too High...")
        elif guess < random_number:
            print("Sorry, Guess Again. Too Low...")
        else: 
            print(f"Congrats, You Guess a Number {random_number}")

Number = int(input("Enter a Limit number"))
RandomNum(Number)