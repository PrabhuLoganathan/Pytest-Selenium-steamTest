from src.python.framework.browser import Browser
from src.python.framework.config import Config
import pytest
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


@pytest.fixture(scope="module")
def setup_class(request):
    browser = Browser(Config().config['main']['browserName'])
    Config().driver = browser.driver

    def teardown_class():
        browser.driver.quit()
    request.addfinalizer(teardown_class)
