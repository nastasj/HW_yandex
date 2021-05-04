from base_page import BasePage
import pytest
import time
from locators import FeaturePageLocators


class FeaturePage(BasePage):

    def should_be_login_button(self):
        assert self.is_element_present(*FeaturePageLocators.LOGIN_BUTTON), \
            "Login button is not presented, but it should be"

    def should_be_market_link(self):
        self.should_be_correct_redirect(*FeaturePageLocators.MARKET_LINK), \
            "Market link is not presented, but it should be"
        assert (self.browser.current_url.startswith("https://market.yandex.ru/"))
        self.browser.close()
        self.browser.switch_to.window(self.browser.window_handles[0])

    def should_be_video_link(self):
        self.should_be_correct_redirect(*FeaturePageLocators.VIDEO_LINk), \
            "Video link is not presented, but it should be"
        assert (self.browser.current_url.startswith("https://yandex.ru/video/"))
        self.browser.close()
        self.browser.switch_to.window(self.browser.window_handles[0])

    def should_be_news_link(self):
        self.should_be_correct_redirect(*FeaturePageLocators.NEWS_LINK), \
            "News link is not presented, but it should be"
        assert (self.browser.current_url.startswith("https://yandex.ru/news/"))
        self.browser.close()
        self.browser.switch_to.window(self.browser.window_handles[0])

    def should_be_maps_link(self):
        self.should_be_correct_redirect(*FeaturePageLocators.MAPS_LINK), \
            "Maps link is not presented, but it should be"
        assert (self.browser.current_url.startswith("https://yandex.ru/maps/"))
        self.browser.close()
        self.browser.switch_to.window(self.browser.window_handles[0])

    def should_be_translate_link(self):
        self.should_be_correct_redirect(*FeaturePageLocators.TRANSLATE_LINK), \
            "Translate link is not presented, but it should be"
        assert (self.browser.current_url.startswith("https://translate.yandex.ru/"))
        self.browser.close()
        self.browser.switch_to.window(self.browser.window_handles[0])

    def should_be_music_link(self):
        self.should_be_correct_redirect(*FeaturePageLocators.MUSIC_LINK), \
            "Music link is not presented, but it should be"
        assert (self.browser.current_url.startswith("https://music.yandex.ru/"))
        self.browser.close()
        self.browser.switch_to.window(self.browser.window_handles[0])