import time
from selenium import webdriver as RemoteWebDriver
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
from locators import BasePageLocators
import random


class BasePage:
    def __init__(self, browser: RemoteWebDriver, url, timeout=10):
        self.browser = browser
        self.url = url
        self.browser.implicitly_wait(timeout)

    def is_disappeared(self, how, what, timeout=4):
        try:
            WebDriverWait(self.browser, timeout, 1, TimeoutException). \
                until_not(EC.presence_of_element_located((how, what)))
        except TimeoutException:
            return False

        return True

    def is_element_present(self, how, what):
        try:
            self.browser.find_element(how, what)
        except NoSuchElementException:
            return False
        return True

    def is_not_element_present(self, how, what, timeout=4):
        try:
            WebDriverWait(self.browser, timeout).until(EC.presence_of_element_located((how, what)))
        except TimeoutException:
            return True

        return False

    def go_to_login_page(self):
        link = self.browser.find_element(*BasePageLocators.LOGIN_LINK)
        link.click()

    def open(self):
        self.browser.get(self.url)

    def should_be_authorized_user(self):
        assert self.is_element_present(*BasePageLocators.USER_ICON), "User icon is not presented," \
                                                                     " probably unauthorised user"

    def should_be_login_link(self):
        assert self.is_element_present(*BasePageLocators.LOGIN_LINK), "Login link is not presented"

    def choose_random_letter(self):
        upper_letter = chr(random.randint(1040, 1072))
        lower_letter = chr(ord(upper_letter) + 32)
        return upper_letter, lower_letter

    def fill_field_and_choose_suggest(self, how, what, how2, what2, how3, what3, filling):
        self.browser.find_element(how, what).click()
        self.browser.find_element(how2, what2).send_keys(filling)
        time.sleep(2)
        suggested_list = self.browser.find_elements(how3, what3)
        for i in range(len(suggested_list)):
            suggest = suggested_list[i].get_attribute('textContent')
            if suggest == filling:
                suggested_list[i].click()
                break