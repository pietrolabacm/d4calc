import PIL
import pytesseract
#ATTENTION                                   I
#You must insert your tesseract path bellow  V
pytesseract.pytesseract.tesseract_cmd = r'C:\Users\pietro.menezes\AppData\Local\Programs\Tesseract-OCR\tesseract'

def readJpeg(jpegPath):
    jpegText = pytesseract.image_to_string(PIL.Image.open(jpegPath))
    return jpegText