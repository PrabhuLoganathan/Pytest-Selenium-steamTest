from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from src.python.framework.config import Config
from src.python.framework.elements.base_element import BaseElement


class Tab(BaseElement):
    def click_and_wait(self):
        self.click()
        WebDriverWait(self.driver, Config().explicitly_wait).until(
            EC.url_changes(self.driver.current_url))