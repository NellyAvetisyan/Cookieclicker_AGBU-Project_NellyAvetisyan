from selenium import webdriver
from pages_.basePage import BasePage
from selenium.webdriver.common.by import By


class NavigationBar(BasePage):
    def __init__(self, driver:webdriver.Chrome):
        super().__init__(driver)
        self.changeLanguageButtonLocator = (By.ID, "changeLanguage")

    def click_to_change_language_button(self):
        changeLanguageButton = self._find_element(self.changeLanguageButtonLocator)
        self._click(changeLanguageButton)