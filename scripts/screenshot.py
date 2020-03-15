from robot.libraries.BuiltIn import BuiltIn
from selenium import webdriver

from PIL import Image
from io import BytesIO
from selenium.webdriver.chrome.options import Options
import time

def capture_full_page_screenshot():
    # get webdriver instance from robotframework selenium library
    seleniumlib = BuiltIn().get_library_instance('SeleniumLibrary')
    driver = seleniumlib.driver

    # capturing body tag gives full page screenshot
    body_tag = driver.find_element_by_tag_name('body')
    body_tag.screenshot('image_name.png')

def capture_full_page():
    seleniumlib = BuiltIn().get_library_instance('SeleniumLibrary')
    driver = seleniumlib.driver
    total_width = driver.execute_script("return document.body.offsetWidth")
    total_height = driver.execute_script("return document.body.scrollHeight")
    driver.set_window_size(total_width, total_height)
    driver.save_screenshot("SomeName.png")

def take_fullpage_sceenshot(url):
    open_url(url)

def open_url(url):
    options = Options()
    options.headless = True
    driver = webdriver.Chrome(chrome_options=options)
    driver.maximize_window()
    driver.get(url)
    save_screenshot(driver, 'screen.png')

def save_screenshot(driver, file_name):
    height, width = scroll_down(driver)
    driver.set_window_size(width, height)
    img_binary = driver.get_screenshot_as_png()
    img = Image.open(BytesIO(img_binary))
    img.save(file_name)
    # print(file_name)
    print(" screenshot saved ")

def scroll_down(driver):
    total_width = driver.execute_script("return document.body.offsetWidth")
    total_height = driver.execute_script("return document.body.parentNode.scrollHeight")
    viewport_width = driver.execute_script("return document.body.clientWidth")
    viewport_height = driver.execute_script("return window.innerHeight")

    rectangles = []

    i = 0
    while i < total_height:
        ii = 0
        top_height = i + viewport_height

        if top_height > total_height:
            top_height = total_height

        while ii < total_width:
            top_width = ii + viewport_width

            if top_width > total_width:
                top_width = total_width

            rectangles.append((ii, i, top_width, top_height))

            ii = ii + viewport_width

        i = i + viewport_height

    previous = None
    part = 0
    for rectangle in rectangles:
        if not previous is None:
            driver.execute_script("window.scrollTo({0}, {1})".format(rectangle[0], rectangle[1]))
            time.sleep(0.5)
        # time.sleep(0.2)

        if rectangle[1] + viewport_height > total_height:
            offset = (rectangle[0], total_height - viewport_height)
        else:
            offset = (rectangle[0], rectangle[1])

        previous = rectangle

    return (total_height, total_width)