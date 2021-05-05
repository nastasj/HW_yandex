from .base_page import BasePage
import random
import time
from .locators import FeaturePageLocators


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
        self.should_be_correct_redirect(*FeaturePageLocators.VIDEO_LINK), \
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

    def fill_field_and_choose_suggest(self):
        upper_letter, lower_letter = self.choose_random_letter()
        self.browser.find_element(*FeaturePageLocators.INPUT_BOX).send_keys(upper_letter)
        suggested_list = self.browser.find_elements(*FeaturePageLocators.SUGGEST_LIST)
        for i in range(len(suggested_list)):
            print(suggested_list[i].get_attribute('textContent'))
        number = random.randint(0, len(suggested_list) - 1)
        suggest = suggested_list[number].get_attribute('textContent')
        print(suggest)
        suggested_list[number].click()
        time.sleep(2)
        suggest2 = self.browser.find_element(*FeaturePageLocators.INPUT_BOX_2).get_property('value')
        print(suggest2)
        time.sleep(2)
        assert suggest == suggest2

    def search_results_should_contain_letter(self):
        upper_letter, lower_letter = self.choose_random_letter()
        print(upper_letter, lower_letter)
        self.browser.find_element(*FeaturePageLocators.INPUT_BOX).send_keys(upper_letter)
        suggested_list = self.browser.find_elements(*FeaturePageLocators.SUGGEST_LIST)
        number = random.randint(0, len(suggested_list) - 1)
        suggest = suggested_list[number].get_attribute('textContent')
        print(suggest)
        assert upper_letter in suggest or lower_letter in suggest

    def should_be_suggest_list(self):
        assert self.is_element_present(*FeaturePageLocators.SUGGEST_LIST_BLOCK), \
            "Suggest list is not presented, but it should be"

    def pagination_should_be_presented(self):
        assert self.is_element_present(*FeaturePageLocators.PAGINATION), \
            "Pagination is not presented, but it should be"

    def pagination_should_work(self):
        self.browser.find_element(*FeaturePageLocators.PAGE_3).click()
        assert "p=2" in self.browser.current_url

    def advanced_search_should_be_presented(self):
        assert self.is_element_present(*FeaturePageLocators.ADVANCED_SEARCH_BUTTON), \
            "Advanced search is not presented, but it should be"

    def advanced_search_should_work(self):
        self.browser.find_element(*FeaturePageLocators.ADVANCED_SEARCH_BUTTON).click()
        self.browser.find_element(*FeaturePageLocators.ADVANCED_SEARCH_2_WEEKS).click()
        self.browser.find_element(*FeaturePageLocators.ADVANCED_SEARCH_FIND_BUTTON).click()