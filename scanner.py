from PIL import Image
import PIL.Image

from pytesseract import image_to_string
import pytesseract

output = pytesseract.image_to_string(PIL.Image.open('apodixi2.png'), lang='ell')
print(output)
