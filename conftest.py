import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options


def pytest_addoption(parser):
    parser.addoption('--browser_name', action='store', default="chrome",
                     help="Choose browser: chrome or firefox")


@pytest.fixture(scope="function")
def browser(request):
    browser_name = request.config.getoption("browser_name")
    if browser_name == "chrome":
        options = Options()
        options.add_argument('--start-maximized')
        # options.add_experimental_option('excludeSwitches', ['enable-logging'])
        browser = webdriver.Chrome(options=options)
        # browser = webdriver.Chrome(options=options)
    elif browser_name == "firefox":
        fp = webdriver.FirefoxProfile()
        print("\nstart firefox browser for test..")
        browser = webdriver.Firefox(firefox_profile=fp)
        browser.maximize_window()
    else:
        print("Browser <browser_name> still is not implemented")
    # browser.implicitly_wait(5)
    yield browser
    browser.quit()