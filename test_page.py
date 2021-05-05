from .feature_page import FeaturePage
import pytest

link = "https://yandex.ru/"


class TestFeature:

    @pytest.mark.skip
    # должна быть кнопка "Войти"
    def test_there_is_login_button(self, browser):
        page = FeaturePage(browser, link)
        page.open()
        page.should_be_login_button()

    @pytest.mark.skip
    def test_market_redirect(self, browser):
        page = FeaturePage(browser, link)
        page.open()
        page.should_be_market_link()

    @pytest.mark.skip
    def test_market_redirect(self, browser):
        page = FeaturePage(browser, link)
        page.open()
        page.should_be_market_link()

    @pytest.mark.skip
    def test_video_redirect(self, browser):
        page = FeaturePage(browser, link)
        page.open()
        page.should_be_video_link()

    @pytest.mark.skip
    def test_news_redirect(self, browser):
        page = FeaturePage(browser, link)
        page.open()
        page.should_be_news_link()

    @pytest.mark.skip
    def test_maps_redirect(self, browser):
        page = FeaturePage(browser, link)
        page.open()
        page.should_be_maps_link()

    @pytest.mark.skip
    def test_translate_redirect(self, browser):
        page = FeaturePage(browser, link)
        page.open()
        page.should_be_translate_link()

    @pytest.mark.skip
    def test_music_redirect(self, browser):
        page = FeaturePage(browser, link)
        page.open()
        page.should_be_music_link()

    @pytest.mark.skip
    def test_there_is_suggest_list(self, browser):
        page = FeaturePage(browser, link)
        page.open()
        page.should_be_suggest_list()

    @pytest.mark.skip
    def test_search_results_contain_letter(self, browser):
        page = FeaturePage(browser, link)
        page.open()
        page.search_results_should_contain_letter()

    @pytest.mark.skip
    def test_fill_field_and_choose_suggest(self, browser):
        page = FeaturePage(browser, link)
        page.open()
        page.fill_field_and_choose_suggest()

    @pytest.mark.skip
    def test_pagination_presents(self, browser):
        page = FeaturePage(browser, link)
        page.open()
        page.fill_field_and_choose_suggest()
        page.pagination_should_be_presented()

    @pytest.mark.skip
    def test_pagination_works(self, browser):
        page = FeaturePage(browser, link)
        page.open()
        page.fill_field_and_choose_suggest()
        page.pagination_should_work()

    def test_advanced_search_presents(self, browser):
        page = FeaturePage(browser, link)
        page.open()
        page.fill_field_and_choose_suggest()
        page.advanced_search_should_be_presented()

    def test_advanced_search_works(self, browser):
        page = FeaturePage(browser, link)
        page.open()
        page.fill_field_and_choose_suggest()
        page.advanced_search_should_work()