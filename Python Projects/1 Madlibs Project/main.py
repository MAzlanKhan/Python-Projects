# Taking Inputs
name = input("Enter your Name: ").strip()
location = input("Enter your City: ").strip()
classEdu = input("Enter your Class: ").strip()
subject = input("Enter your Favourite Subject: ").strip()
teacher = input("Enter your Favourite Teacher: ").strip()
marks = input("Enter your Marks: ").strip()
DreamLocation = input("Enter your Dream Country or City: ").strip()
DreamCar = input("Enter your Dream Car: ").strip()
profession = input("What is your Profession: ").strip()

# Using 'f' String 
MySelf = f"My name is {name}. I live in {location}. I study in Class {classEdu}. {subject} is my favorite subject. {teacher} teaches us {subject}.\nI scored {marks} in Class {classEdu}. I want to go to {DreamLocation}. {DreamCar} is my dream car.\nI aspire to become a {profession}."

# Output
print(MySelf)
