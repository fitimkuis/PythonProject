import cv2
import numpy as np

try:
    from PIL import Image, ImageEnhance, ImageFilter
except ImportError:
    import Image
from pytesseract import image_to_string, pytesseract

dict = {'ADMIN': {'name': 'admin', 'pass': '123pass'}, 'USER': {'name': 'bobby', 'pass': 'aowiejf'}}
print(type(dict))
print(dict['ADMIN']['name'])
print(dict['ADMIN']['pass'])


pytesseract.tesseract_cmd = r'C:\\Program Files\\Tesseract-OCR\\tesseract.exe'
print(pytesseract.image_to_string(Image.open('C:\\Users\\fitim\\IdeaProjects\\PythonProject\\PythonProject\\testcases\\images\\image.png')))


def ocr_core():

    image = cv2.imread('C:\\Users\\fitim\\IdeaProjects\\PythonProject\\PythonProject\\testcases\\images\\demoshot0.png')
    image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    #image = cv2.GaussianBlur(image, (3,3), 0)
    cv2.imwrite('C:\\Users\\fitim\\IdeaProjects\\PythonProject\\PythonProject\\testcases\\images\\temp2.jpg', image)
    image = Image.open('C:\\Users\\fitim\\IdeaProjects\\PythonProject\\PythonProject\\testcases\\images\\temp2.jpg')
    text = image_to_string(image)
    #print(text)
    return text

def read_colour_image():
    imageName = 'C:\\Users\\fitim\\IdeaProjects\\PythonProject\\PythonProject\\testcases\\images\\demoshot0.png'
    img = cv2.imread(imageName,cv2.IMREAD_COLOR) #Open the image from which charectors has to be recognized
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY) #convert to grey to reduce detials
    gray = cv2.bilateralFilter(gray, 11, 17, 17) #Blur to reduce noise
    img = cv2.adaptiveThreshold(gray,255,cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY,71,2) #71 2
    #img = cv2.adaptiveThreshold(gray,255,cv2.ADAPTIVE_THRESH_MEAN_C,cv2.THRESH_BINARY,11,2)
    cv2.imwrite('C:\\Users\\fitim\\IdeaProjects\\PythonProject\\PythonProject\\testcases\\images\\temp3.jpg', img)
    original = pytesseract.image_to_string(img, config='')
    return original

def ocr_core2():
    """
    This function will handle the core OCR processing of images.
    """

    # Grayscale, Gaussian blur, Otsu's threshold
    image = cv2.imread('C:\\Users\\fitim\\IdeaProjects\\PythonProject\\PythonProject\\testcases\\images\\demoshot0.png')
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    blur = cv2.GaussianBlur(gray, (3,3), 0)
    thresh = cv2.threshold(blur, 0, 255, cv2.THRESH_BINARY_INV + cv2.THRESH_OTSU)[1]

    # Morph open to remove noise and invert image
    kernel = cv2.getStructuringElement(cv2.MORPH_RECT, (3,3))
    opening = cv2.morphologyEx(thresh, cv2.MORPH_OPEN, kernel, iterations=1)
    invert = 255 - opening
    cv2.imwrite('C:\\Users\\fitim\\IdeaProjects\\PythonProject\\PythonProject\\testcases\\images\\temp4.jpg', invert)
    image = Image.open('C:\\Users\\fitim\\IdeaProjects\\PythonProject\\PythonProject\\testcases\\images\\temp4.jpg')
    text = image_to_string(image)
    #print(text)
    return text
    #original = pytesseract.image_to_string(img, config='')
    #print(original)

def process_rgb(rgb=None):
    rgb = cv2.imread('C:\\Users\\fitim\\IdeaProjects\\PythonProject\\PythonProject\\testcases\\images\\demoshot0.png')
    hasText = False
    gray = cv2.cvtColor(rgb, cv2.COLOR_BGR2GRAY)
    morphKernel = cv2.getStructuringElement(cv2.MORPH_ELLIPSE, (3,3))
    grad = cv2.morphologyEx(gray, cv2.MORPH_GRADIENT, morphKernel)
    # binarize
    _, bw = cv2.threshold(grad, 0.0, 255.0, cv2.THRESH_BINARY | cv2.THRESH_OTSU)
    # connect horizontally oriented regions
    morphKernel = cv2.getStructuringElement(cv2.MORPH_RECT, (9, 1))
    connected = cv2.morphologyEx(bw, cv2.MORPH_CLOSE, morphKernel)
    # find contours
    mask = np.zeros(bw.shape[:2], dtype="uint8")
    contours, hierarchy = cv2.findContours(connected, cv2.RETR_CCOMP, cv2.CHAIN_APPROX_SIMPLE)
    # filter contours
    idx = 0
    while idx >= 0:
        x,y,w,h = cv2.boundingRect(contours[idx])
        # fill the contour
        cv2.drawContours(mask, contours, idx, (255, 255, 255), cv2.FILLED)
        # ratio of non-zero pixels in the filled region
        r = cv2.contourArea(contours[idx])/(w*h)
        if(r > 0.45 and h > 5 and w > 5 and w > h):
            cv2.rectangle(rgb, (x,y), (x+w,y+h), (0, 255, 0), 2)
            hasText = True
        idx = hierarchy[0][idx][0]
    print(hasText, rgb)
    text = image_to_string(rgb)
    print(text)
    return hasText, rgb

def read_image_text_config():
    pytesseract.tesseract_cmd = r'C:\\Program Files\\Tesseract-OCR\\tesseract.exe'
    img = cv2.imread('C:\\Users\\fitim\\IdeaProjects\\PythonProject\\PythonProject\\testcases\\images\\demoshot0.png')
    img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    # Adding custom options
    #custom_config = r'--oem 3 --psm 6 outputbase digits'
    #print(pytesseract.image_to_string(img, config=custom_config))
    ##custom_config = r'-c tessedit_char_blacklist=0123456789 --psm 6'
    custom_config = r'--oem 3 --psm 6'
    #custom_config = r'-c tessedit_char_whitelist=abcdefghijklmnopqrstuvwxyz --psm 6'
    text = pytesseract.image_to_string(img, config=custom_config)
    cv2.imwrite('C:\\Users\\fitim\\IdeaProjects\\PythonProject\\PythonProject\\testcases\\images\\blaclist.jpg', img)
    print(text)


read_image_text_config()
#print(ocr_core2())

#print(read_colour_image())

#process_rgb()

#print(ocr_core())