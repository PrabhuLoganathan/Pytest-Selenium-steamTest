import re
from selenium.webdriver.common.by import By
from src.python.framework.base_page import BasePage
from src.python.framework.elements.button import Button
from src.python.framework.find import Find


class GamePage(BasePage):
    _page_locator = (By.ID, "game_highlights")

    discount = Find(by=By.XPATH, locator="//div[contains(@class, 'game_purchase_discount')]")
    dwld_btn = Find(Button, by=By.CLASS_NAME, locator="header_installsteam_btn_content")

    def __init__(self):
        super().__init__(self._page_locator, None)

    def assert_discount(self, disc):
        assert int(re.search(r'\d\d', self.discount.text).group()) == disc

    def dowload_click(self):
        self.dwld_btn.click()