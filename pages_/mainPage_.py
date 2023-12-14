from selenium import webdriver
from pages_.basePage import BasePage

class MainPage(BasePage):
    def __init__(self,driver):
        self.driver = driver

    def click_on_change_language_button(self,locator):
        changeLanguageButton = self._find_element(locator)

