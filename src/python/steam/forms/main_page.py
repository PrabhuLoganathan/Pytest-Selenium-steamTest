from selenium.webdriver.common.by import By
from src.python.framework.base_page import BasePage
from src.python.framework.config import Config
from src.python.framework.find import Find
from src.python.framework.elements.combobox import ComboBox


class MainPage(BasePage):
    _page_locator = (By.XPATH, "//div[@class=\"home_page_gutter\"]")
    _cmbx_lang_locator = "language_pulldown"
    _lbl_lang_locator = "//div[@id='language_dropdown']//a[contains(text(), '{}')]".format(
        Config().localization['language'])

    _cmbx_games_locator = "genre_tab"
    _action_label_locator = "//div[@id='genre_flyout']//a[contains(text(), '{}')]".format(
        Config().localization["action"])

    cmbxGames = Find(ComboBox, By.ID, _cmbx_games_locator)
    cmbxLanguage = Find(ComboBox, By.ID, _cmbx_lang_locator)

    def __init__(self):
        super().__init__(self._page_locator, Config().config['steam']['url']['mainPage'])

    def find_and_click_actions(self):
        self.cmbxGames.hover_and_click_on_lbl(By.XPATH, self._action_label_locator)

    def change_language(self):
        self.cmbxLanguage.click_self_and_lbl(By.XPATH, self._lbl_lang_locator)
        Config().language = 'en'
        self.refresh()