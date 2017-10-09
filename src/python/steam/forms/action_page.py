import re
from selenium.webdriver.common.by import By
from src.python.framework.base_page import BasePage
from src.python.framework.elements.label import Label
from src.python.framework.elements.tab import Tab
from src.python.framework.config import Config
from src.python.framework.find import Find, Finds


class ActionPage(BasePage):
    _page_locator = (By.XPATH, "//h2[contains(text(), '{}')]".format(Config().localization["action"]))

    _tabbtn_discount_locator = "//div[@class='tabbar_ctn']//div[contains(text(), '{}')]".format(
        Config().localization['discount']) # ID "tab_select_Discounts"

    _game_label_locator = "//div[@id='DiscountsRows']//a"

    tabDiscount = Find(Tab, By.XPATH, _tabbtn_discount_locator)
    lblsGames = Finds(Label, By.XPATH, _game_label_locator)

    def __init__(self):
        super().__init__(self._page_locator, Config().config['steam']['url']['actionPage'])

    def open_discount_tab(self):
        self.tabDiscount.click()
        self.scroll_window_to_top()

    def choose_game_by_max_discount(self):
        games = self.lblsGames
        lst = [int(re.search(r'\d\d', g.text).group()) for g in games]
        for g in games:
            if int(re.search(r'\d\d', g.text).group()) == max(lst):
                discount = max(lst)
                g.click()
                return discount
