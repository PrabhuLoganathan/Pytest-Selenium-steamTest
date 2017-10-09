from selenium.webdriver.common.by import By
from src.python.framework.base_page import BasePage
from src.python.framework.config import Config
from src.python.framework.elements.label import Label
from src.python.framework.find import Find
from urllib.request import urlretrieve
import os


class AboutPage(BasePage):
    _page_locator = (By.ID, "about_header_ctn")

    btnDownload = Find(Label, By.ID, "about_install_steam_link")

    def __init__(self):
        super().__init__(self._page_locator, Config().config['steam']['url']['aboutPage'])

    def download_installer(self):
        url = self.btnDownload.get_href()
        urlretrieve(url, "steam")
        assert os.path.exists(os.path.join(os.getcwd(), 'steam'))