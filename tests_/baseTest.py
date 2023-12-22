import unittest
from selenium import webdriver
from selenium.webdriver.support.events import EventFiringWebDriver
from common_.utilities_.customListener import MyListener
from testData_.testData import cookieClickerUrl
from pages_.navigationBar_.navigationBar import NavigationBar
from pages_.navigationBar_.langageChoosePage import LanguageChoosePage


class BaseTest(unittest.TestCase):
    def setUp(self):
        simpleDriver = webdriver.Chrome()
        self.driver = EventFiringWebDriver(simpleDriver, MyListener())
        self.driver.implicitly_wait(10)
        self.driver.maximize_window()
        self.driver.delete_all_cookies()
        self.driver.get(cookieClickerUrl)
        navigationBarObj = NavigationBar(simpleDriver)
        navigationBarObj.click_to_change_language_button()
        languageChoosePageObj = LanguageChoosePage(simpleDriver)
        languageChoosePageObj.click_to_france_language()

    def tearDown(self):
        self.driver.close()






