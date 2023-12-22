from selenium import webdriver
from pages_.basePage import BasePage
from selenium.webdriver.common.by import By
from common_.utilities_.customLogger import *
from time import sleep

class MainPage(BasePage):
    def __init__(self, driver:webdriver.Chrome):
        super().__init__(driver)
        self.__bigCookieLogoLocator = (By.ID, "bigCookie")
        self.__cookieCountLocator = (By.ID, "cookies")

    def click_on_big_cookie_once(self):
        bigCookieLogo = self._find_element(self.__bigCookieLogoLocator)
        self._click(bigCookieLogo)

    def get_cookie_count_text(self):
        cookieCountText = self._find_element(self.__cookieCountLocator)
        return self._get_element_text(cookieCountText)

    def get_cookie_count(self):
        cookieCountText = self.get_cookie_count_text()
        cookieCount = cookieCountText.split(" ", 1)[0]
        return int(cookieCount)

    def click_on_big_cookie_10000_times(self):
        bigCookieElement = self._find_element(self.__bigCookieLogoLocator)
        sleep(10)  # to get cookie count locator
        cookieCountBeforeClick = self.get_cookie_count()
        sleep(10)  # to get cookie count locator
        cookieCountAfterClick = self.get_cookie_count()
        for i in range(10000):
            bigCookieElement.click()
            if cookieCountAfterClick != cookieCountBeforeClick + 1:
                logger("ERROR", "Cookie count does not match")

