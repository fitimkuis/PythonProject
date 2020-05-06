import pyscreenshot as ImageGrab
import sys
from datetime import datetime
#import os
import cv2
from PIL import Image
from time import sleep


#im = pyscreeze.screenshot(region=(0,0, 300, 400))
#print im
from pytesseract import image_to_string


def image_screenshot(x1,x2,y1,y2):
    sleep(1)
    x11 = int(x1)
    #print "Debug x11 %d "%x11
    x22 = int(x2)
    #print "Debug x22 %d "%x22
    y11 = int(y1)
    #print "Debug y11 %d "%y11
    y22 = int(y2)
    #print "Debug y22 %d "%y22
    # fullscreen
    im=ImageGrab.grab()
    imgrab = 'testcases/images/google.png'
    im.save(imgrab)
    #im.show()

    # part of the screen
    #filename = '/path/to/output/myfile-%s.txt'%datetime.now().strftime('%Y-%m-%d')
    im=ImageGrab.grab(bbox=(x11,y11,x22,y22), childprocess=False) # X1,Y1,X2,Y2
    imfile = 'testcases/images/%s_screenshot.png'%datetime.now().strftime('%Y-%m-%d %H %M %S')
    imfile2 = 'testcases/images/%s_gray_image.tif'%datetime.now().strftime('%Y-%m-%d %H %M %S')
    #print imfile
    im.save(imfile)
    img = Image.open(imfile)
    tifimage = 'testcases/images/%s_gray_image.tif'%datetime.now().strftime('%Y-%m-%d %H %M %S')
    img.save(tifimage)
    #im.save(imfile)
    image = cv2.imread(tifimage)
    gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    cv2.imwrite(tifimage,gray_image)
    return tifimage

def read_image_text(im):
    image = Image.open(im)  # Open image object using PIL
    #print image_to_string(image)     # Run tesseract.exe on image
    return image_to_string(image)


#a =image_screenshot(360,900,140,210)
#a = image_screenshot(571,1100,330,375)
#b = read_image_text(a)
#print b
'''
Debug x11 571 
Debug x22 664 
Debug y11 426 
Debug y22 453
x1 1210 x2 1340
y1 80 y2 120
'''