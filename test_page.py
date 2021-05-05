from .feature_page import FeaturePage
import pytest

link = "https://yandex.ru/"


class TestFeature:

    # должна быть кнопка "Войти"
    def test_there_is_login_button(self, browser):
        page = FeaturePage(browser, link)
        page.open()
        page.should_be_login_button()

    # должен быть редирект на маркет
    def test_market_redirect(self, browser):
        page = FeaturePage(browser, link)
        page.open()
        page.should_be_market_link()

    # должен быть редирект на видео
    def test_video_redirect(self, browser):
        page = FeaturePage(browser, link)
        page.open()
        page.should_be_video_link()

    # должен быть редирект на новости
    def test_news_redirect(self, browser):
        page = FeaturePage(browser, link)
        page.open()
        page.should_be_news_link()

    # должен быть редирект на карты
    def test_maps_redirect(self, browser):
        page = FeaturePage(browser, link)
        page.open()
        page.should_be_maps_link()

    # должен быть редирект на переводчик
    def test_translate_redirect(self, browser):
        page = FeaturePage(browser, link)
        page.open()
        page.should_be_translate_link()

    # должен быть редирект на музыку
    def test_music_redirect(self, browser):
        page = FeaturePage(browser, link)
        page.open()
        page.should_be_music_link()

    # при вводе поискового запроса должны быть показаны саджесты
    def test_there_is_suggest_list(self, browser):
        page = FeaturePage(browser, link)
        page.open()
        page.should_be_suggest_list()

    # в саджестах должны быть символы, введенные в поисковом запросе
    def test_search_results_contain_letter(self, browser):
        page = FeaturePage(browser, link)
        page.open()
        page.search_results_should_contain_letter()

    # проверка ввода рандомных символов и выбора рандомного саджеста
    def test_fill_field_and_choose_suggest(self, browser):
        page = FeaturePage(browser, link)
        page.open()
        page.fill_field_and_choose_suggest()

    # должна присутствовать пагинация
    def test_pagination_presents(self, browser):
        page = FeaturePage(browser, link)
        page.open()
        page.fill_field_and_choose_suggest()
        page.pagination_should_be_presented()

    # должен осуществляться переход на другую страницу поисковой выдачи
    def test_pagination_works(self, browser):
        page = FeaturePage(browser, link)
        page.open()
        page.fill_field_and_choose_suggest()
        page.pagination_should_work()

    # должна быть кнопка расширенного поиска
    def test_advanced_search_presents(self, browser):
        page = FeaturePage(browser, link)
        page.open()
        page.fill_field_and_choose_suggest()
        page.advanced_search_should_be_presented()

    # должен осуществляться расширенный поиск
    def test_advanced_search_works(self, browser):
        page = FeaturePage(browser, link)
        page.open()
        page.fill_field_and_choose_suggest()
        page.advanced_search_should_work()