from selenium.webdriver.common.by import By


class BasePageLocators:
    CITY_CHOOSER_FIELD = (By.CSS_SELECTOR, '[data-marker="location-chooser/value"]')
    CITY_SEARCH_BOX = (By.CSS_SELECTOR, '[data-marker="region-search-bar/search"]')
    SUBWAY_CHOOSER_FIELD = (By.CSS_SELECTOR, '[data-marker="metro-select/withoutValue"]')
    ALPHABET_CHOOSER_TAB = (By.CSS_SELECTOR, '[class ="css-17syd5g"][tabindex="0"]')
    LINE_CHOOSER_TAB = (By.CSS_SELECTOR, '[class ="css-17syd5g"][tabindex="-1"]')
    STATIONS_ALPHABET_LIST_FIELD = (By.CLASS_NAME, "css-1nm6007")