import random

"""
Stone = 0
Paper = 1
Scissor = 2
"""

# Random Function 
def generate_random_number():
  return random.randint(0, 2)

# user input 
user = input("Enter your choice: ").lower().strip()     # converting into lower and using strip
userDict = {"stone": 0 , "paper": 1 , "scissor": 2}     # User Dictionary

# generating random numbers
computer = generate_random_number()
compReverse_Dict = {0 : "stone" , 1 : "paper" , 2 : "scissor"}    # Computer Dictionary
# print(f"You choosed {user} and Computer choosed {compReverse_Dict[computer]}")

# Comparing both 
if compReverse_Dict[computer] == user:
    print(f"Match is Draw.\nYou choosed {user} and Computer also Choosed {compReverse_Dict[computer]}")
else:
    if computer == 0 and userDict[user] == 1:
        print(f"You Won!\nYou choosed {user} and Computer Choosed {compReverse_Dict[computer]}")
    elif computer == 0 and userDict[user] == 2:
        print(f"You Lose!\nYou choosed {user} and Computer Choosed {compReverse_Dict[computer]}")
    elif computer == 1 and userDict[user] == 0:
        print(f"You Lose!\nYou choosed {user} and Computer Choosed {compReverse_Dict[computer]}")
    elif computer == 1 and userDict[user] == 2:
        print(f"You Won!\nYou choosed {user} and Computer Choosed {compReverse_Dict[computer]}")
    elif computer == 2 and userDict[user] == 0:
        print(f"You Won!\nYou choosed {user} and Computer Choosed {compReverse_Dict[computer]}")
    elif computer == 2 and userDict[user] == 1:
        print(f"You Lose!\nYou choosed {user} and Computer Choosed {compReverse_Dict[computer]}")
    else:
        print("Something went Wrong...")