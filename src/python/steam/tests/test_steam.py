from src.python.steam.forms.action_page import ActionPage
from src.python.steam.forms.age_page import AgePage
from src.python.steam.forms.game_page import GamePage
from src.python.steam.forms.main_page import MainPage
from src.python.steam.forms.about_page import AboutPage
from src.python.framework.fixtures import setup_class
import pytest


@pytest.mark.usefixtures('setup_class')
class TestSteam():
    def test_steam(self):
        main_page = MainPage()
        main_page.go()
        #main_page.change_language()
        main_page.find_and_click_actions()

        action_page = ActionPage()
        action_page.open_discount_tab()
        discount = action_page.choose_game_by_max_discount()

        AgePage()
        game_page = GamePage()
        game_page.assert_discount(discount)
        game_page.dowload_click()

        about_page = AboutPage()
        about_page.download_installer()