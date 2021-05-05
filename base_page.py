from selenium import webdriver as RemoteWebDriver
from selenium.common.exceptions import NoSuchElementException
import random


class BasePage:
    def __init__(self, browser: RemoteWebDriver, url, timeout=10):
        self.browser = browser
        self.url = url
        self.browser.implicitly_wait(timeout)

    def is_element_present(self, how, what):
        try:
            self.browser.find_element(how, what)
        except NoSuchElementException:
            return False
        return True

    def open(self):
        self.browser.get(self.url)

    def choose_random_letter(self):
        upper_letter = chr(random.randint(1040, 1072))
        lower_letter = chr(ord(upper_letter) + 32)
        return upper_letter, lower_letter

    def should_be_correct_redirect(self, how, what):
        self.browser.find_element(how, what).click()
        window_after = self.browser.window_handles[1]
        self.browser.switch_to.window(window_after)





