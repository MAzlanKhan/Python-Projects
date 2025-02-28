from pyzbar.pyzbar import decode
from PIL import Image

img = Image.open('C:/Python/Compulsory Project Q1/QRCode/QRCodes/myqr1.png')
result = decode(img)
print(result)

