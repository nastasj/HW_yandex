from selenium.webdriver.common.by import By


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
    INPUT_BOX = (By.CSS_SELECTOR, '[span[class="input__box"]]')
