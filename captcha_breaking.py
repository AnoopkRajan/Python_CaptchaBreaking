from pytesseract import image_to_string
from PIL import Image
from requests import get
from io import BytesIO

#this is used to get the image from the provided link.
response = get("http://13.127.3.3/wp-content/uploads/image-1.png")

#Opens the image.
img = Image.open(BytesIO(response.content))

#Converts image to string using Pytesseract.
text = image_to_string(img)

#Prints Text.
print(text)

#Does the mathematical operations corresponding to the image.
if (text[1]=="+"):
    print(int(text[0])+int(text[2]))
elif (text[1]=="-"):
    print(int(text[0])-int(text[2]))
elif (text[1]=="*"):
    print(int(text[0])*int(text[2]))
elif (text[1]=="/"):
    print(int(text[0])/int(text[2]))
