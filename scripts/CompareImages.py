import cv2

from PIL import Image

import numpy as np

def comp_images(a, b):
    img1=cv2.imread(a)
    img2=cv2.imread(b)
    difference = cv2.subtract(img1,img2)
    result = not np.any(difference)#if diff is all zeros it will return False
    if result == True:
        return "The images are same"
    else:
        cv2.imwrite("result.jpg", difference)
        return "The images are different"


#comp_images("C:/Users/fitim/Desktop/robot_test_cases/Testing/2019-06-08 11 44 46_gray_image.tif", "C:/Users/fitim/Desktop/robot_test_cases/Testing/2019-06-08 11 44 46_screenshot.png")