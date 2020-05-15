import cv2

try:
    from PIL import Image, ImageEnhance, ImageFilter
except ImportError:
    import Image
from pytesseract import image_to_string, pytesseract

pytesseract.tesseract_cmd = r'C:\\Program Files\\Tesseract-OCR\\tesseract.exe'
print(pytesseract.image_to_string(Image.open('C:\\Users\\fitim\\IdeaProjects\\PythonProject\\PythonProject\\testcases\\images\\image.png')))


def ocr_core():
    """
    This function will handle the core OCR processing of images.
    """
    '''
    # Grayscale, Gaussian blur, Otsu's threshold
    image = cv2.imread('C:\\Users\\fitim\\IdeaProjects\\PythonProject\\PythonProject\\testcases\\images\\demoshot0.png')
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    blur = cv2.GaussianBlur(gray, (3,3), 0)
    thresh = cv2.threshold(blur, 0, 255, cv2.THRESH_BINARY_INV + cv2.THRESH_OTSU)[1]

    # Morph open to remove noise and invert image
    kernel = cv2.getStructuringElement(cv2.MORPH_RECT, (3,3))
    opening = cv2.morphologyEx(thresh, cv2.MORPH_OPEN, kernel, iterations=1)
    invert = 255 - opening
    '''
    image = cv2.imread('C:\\Users\\fitim\\IdeaProjects\\PythonProject\\PythonProject\\testcases\\images\\demoshot0.png')
    image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    cv2.imwrite('C:\\Users\\fitim\\IdeaProjects\\PythonProject\\PythonProject\\testcases\\images\\temp2.jpg', image)
    image = Image.open('C:\\Users\\fitim\\IdeaProjects\\PythonProject\\PythonProject\\testcases\\images\\temp2.jpg')
    text = image_to_string(image)
    print(text)
    return text

print(ocr_core())