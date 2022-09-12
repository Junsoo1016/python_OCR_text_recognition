import pytesseract
from PIL import Image

pytesseract.pytesseract.tesseract_cmd = r"/opt/homebrew/Cellar/tesseract/5.2.0/bin/tesseract"

receipt1 = Image.open('receipt.jpg')
res = pytesseract.image_to_string(receipt1)

print(res)
