#After installing the qrcode with pip, import qr code
import qrcode

# Creating an instance of QRCode class
img = qrcode. QRCode(version=1, box_size=30, border=3)

#Here i'm using the url of my github profile  
img = qrcode.make("https://github.com/AEedriz")
img.save("team59.png")

#install Pillow using pip, import Image with PIL 
from PIL import Image
# the png qr code converted to jpg 
img_png = Image.open("team59.png")
img_jpg = img_png.convert("RGB")
img_jpg.save("team59.jpg") 

#converting the png file to pdf
img_pdf = img_png.convert("RGB")
img_pdf.save("team59.pdf")
