from selenium.webdriver import Firefox, Chrome
from selenium.webdriver.support.events import EventFiringWebDriver, AbstractEventListener

class MyListener(AbstractEventListener):
    def before_navigate_to(self, url, driver):
        print("Before navigate to %s" % url)
    def after_navigate_to(self, url, driver):
        print("After navigate to %s" % url)

driver = Chrome()
ef_driver = EventFiringWebDriver(driver, MyListener())
ef_driver.get("http://www.google.co.in/")