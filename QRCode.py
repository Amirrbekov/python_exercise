import pyqrcode
import png
link = "https://www.linkedin.com/in/valeh-amirbekov-24b2a7246/"
qr_code = pyqrcode.create(link)
qr_code.png("linkedin.png", scale=5)