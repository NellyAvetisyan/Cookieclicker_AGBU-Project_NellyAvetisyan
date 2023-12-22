from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from common_.utilities_.customLogger import *


class BasePage():
    def __init__(self, driver:webdriver.Chrome):
        self.driver = driver

    def _find_element(self,locator):
        try:
            element = WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(locator))
            return element
        except:
            exit(1)

    def _click(self, webElement):
        webElement.click()

    def _get_element_text(self, webElement):
        logger("INFO", "Text successfully found")
        return webElement.text
