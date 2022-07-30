#After installing the qrcode with pip, import qr code
import qrcode

#A qrcode for my github profilr was created 
img = qrcode.make("https://github.com/AEedriz")
img.save("team59.png")

 