from pytesseract import image_to_string 
from PIL import Image
from requests import get
from io import BytesIO

response = get("http://13.127.3.3/wp-content/uploads/image-1.png") 
 
img = Image.open(BytesIO(response.content))

text = image_to_string(img)

if(text[1]=='+'): print(int(text[0])+int(text[2]))
if(text[1]=='-'): print(int(text[0])-int(text[2]))
if(text[1]=='*'): print(int(text[0])*int(text[2]))
if(text[1]=='/'): print(int(text[0])/int(text[2]))
