from selenium import webdriver
from pages_.basePage import BasePage
from selenium.webdriver.common.by import By

class LanguageChoosePage(BasePage):
    def __init__(self,driver:webdriver.Chrome):
        super().__init__(driver)
        self.franceLanguageLocator = (By.ID, "langSelect-FR")

    def click_to_france_language(self):
        franceLanguageButton = self._find_element(self.franceLanguageLocator)
        self._click(franceLanguageButton)