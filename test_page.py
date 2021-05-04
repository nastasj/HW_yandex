from feature_page import FeaturePage
import pytest

link = "https://yandex.ru/"


class TestFeature:

    # должна быть кнопка "Войти"
    def test_there_is_login_button(self, browser):
        page = FeaturePage(browser, link)
        page.open()
        page.should_be_login_button()

    def test_market_redirect(self, browser):
        page = FeaturePage(browser, link)
        page.open()
        page.should_be_correct_redirect()
