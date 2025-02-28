import qrcode
import os

# Taking Data 
name = input("Enter Your Name: ")
RollNum = input("Enter your Roll Number: ")
phone = input("Enter your Phone Number: ")
address = input("Enter your Address: ")


# Joining Data as a String 
data = name + " " + RollNum + " " + phone + " " + address
# print(type(data))

qr = qrcode.QRCode(version=1, box_size=10, border=5)
qr.add_data(data)
qr.make(fit=True)
img= qr.make_image(fill_color="Black", back_color = "White")

# Increment file names
directory = 'C:/Python/Compulsory Project Q1/QRCode/QRCodes/'
file_number = 1
while os.path.exists(f"{directory}myqr{file_number}.png"):
    file_number += 1

img.save(f"{directory}myqr{file_number}.png")