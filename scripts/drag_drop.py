import unittest
from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
import time

from faker import Faker
from faker.providers import internet
from faker.providers import ssn

fake = Faker('fi_FI')
fake.add_provider(internet)

fake.add_provider(ssn)

print(fake.ssn())

#class DragTest():
def test_drag_drop(dragUrl, dropUrl, exePath):
    driver = webdriver.Chrome(executable_path=exePath)

    #driver = self.driver
    #self.driver.maximize_window()
    driver.get(dragUrl)
    driver.switch_to.frame(0)
    source1 = driver.find_element_by_id('draggable')
    action = ActionChains(driver)
    action.drag_and_drop_by_offset(source1, 100, 100).perform()
    time.sleep(2)
    driver.get(dropUrl)
    driver.switch_to.frame(0)
    source1 = driver.find_element_by_id('draggable')
    target1 = driver.find_element_by_id('droppable')
    actions2 = ActionChains(driver)
    actions2.drag_and_drop(source1, target1).perform()
    time.sleep(2)
    if target1.text != "Dropped!":
        raise Exception("element is not dropped")
    assert "Dropped!", target1.text
    print(target1.text)
    time.sleep(2)

    driver.quit()

'''
    def setUp(self):
        self.driver = webdriver.Chrome(executable_path='C:/Users/fitim/bin/chromedriver.exe')

    def test_drag_drop(self):
        #driver = self.driver
        #self.driver.maximize_window()
        self.driver.get('https://jqueryui.com/draggable/')
        self.driver.switch_to.frame(0)
        source1 = self.driver.find_element_by_id('draggable')
        action = ActionChains(self.driver)
        action.drag_and_drop_by_offset(source1, 100, 100).perform()
        time.sleep(5)
        self.driver.get('https://jqueryui.com/droppable/')
        self.driver.switch_to.frame(0)
        source1 = self.driver.find_element_by_id('draggable')
        target1 = self.driver.find_element_by_id('droppable')
        actions2 = ActionChains(self.driver)
        actions2.drag_and_drop(source1, target1).perform()
        time.sleep(5)
        #self.assertEqual("Dropped!", target1.text)
        time.sleep(2)

    def tearDown(self):
        self.driver.quit()
'''


'''
a = DragTest()
a.setUp()
a.test_drag_drop()
a.tearDown()
'''