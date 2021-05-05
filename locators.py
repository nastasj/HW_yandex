from selenium.webdriver.common.by import By
import random

class FeaturePageLocators:
    LOGIN_BUTTON = (By.CLASS_NAME, 'desk-notif-card__login-new-items')
    MARKET_LINK = (By.CSS_SELECTOR, '[data-id="market"]')
    VIDEO_LINK = (By.CSS_SELECTOR, '[data-id="video"]')
    IMAGES_LINK = (By.CSS_SELECTOR, '[data-id="images"]')
    NEWS_LINK = (By.CSS_SELECTOR, '[data-id="news"]')
    MAPS_LINK = (By.CSS_SELECTOR, '[data-id="maps"]')
    TRANSLATE_LINK = (By.CSS_SELECTOR, '[data-id="translate"]')
    MUSIC_LINK = (By.CSS_SELECTOR, '[data-id="music"]')
    MORE_LINK = (By.CSS_SELECTOR, '[data-id="more"]')
    INPUT_BOX = (By.CSS_SELECTOR, '[class="input__control input__input mini-suggest__input"]')
    INPUT_BOX_2 = (By.CSS_SELECTOR, '[class="input__control mini-suggest__input"]')
    SUGGEST_LIST = (By.CSS_SELECTOR, '[class="mini-suggest__item mini-suggest__item_type_fulltext"]')
    SUGGEST_LIST_BLOCK = (By.CSS_SELECTOR, '[class="mini-suggest__popup-content"]')
    PAGINATION = (By.CSS_SELECTOR, '[aria-label="Следующая страница"]')
    PAGE_3 = (By.CSS_SELECTOR, '[aria-label="Страница 3"]')
    ADVANCED_SEARCH_BUTTON = (By.CSS_SELECTOR, '[class="input__settings"]')
    ADVANCED_SEARCH_2_WEEKS = (By.CSS_SELECTOR, '[class ="radio-button__radio"]')
    ADVANCED_SEARCH_FIND_BUTTON = (By.CSS_SELECTOR, '.advanced-search__clear button')
