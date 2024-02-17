from tests_.baseTest import BaseTest
from pages_.mainPage import MainPage
from time import sleep

class ClickToBigCookieLogo(BaseTest):
    def test_clicking_big_cookie_once(self):
        sleep(10)  # to get cookie count locator
        mainPageObj = MainPage(self.driver)
        cookieCountBeforeClick = mainPageObj.get_cookie_count()
        mainPageObj.click_on_big_cookie_once()
        cookieCountAfterClick =mainPageObj.get_cookie_count()
        sleep(10)  # to get cookie count locator
        self.assertEqual(cookieCountAfterClick, cookieCountBeforeClick + 1)

    def test_clicking_big_cookie_10000_times(self):
        sleep(10)  # to get cookie count locator
        mainPageObj = MainPage(self.driver)
        mainPageObj.click_on_big_cookie_10000_times()
