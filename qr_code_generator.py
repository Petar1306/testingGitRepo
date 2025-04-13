import pyqrcode
import png
from pyqrcode import QRCode

address = ('https://www.instagram.com/bozhankovsport/')
url = pyqrcode.create(address)
url.png('bozhankovsport.png', scale=8)
