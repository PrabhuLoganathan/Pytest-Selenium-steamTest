from src.python.framework.base_page import BasePage
from src.python.framework.elements.form import Form
from selenium.webdriver.common.by import By
from src.python.framework.find import Find


class AgePage(BasePage):
    _page_locator = (By.ID, "agecheck_form")

    _age_form_locator = "agecheck_form"

    age_form = Find(Form, by=By.ID, locator=_age_form_locator)

    def __init__(self):
        super().__init__(self._page_locator, None)
        if self._assert_age_page_loaded():
            self._do_age_page_submit()

    def _assert_age_page_loaded(self):
        try:
            self._assert_page_load()
            return True
        except:
            return False

    def _do_age_page_submit(self):
        self.age_form.select_year(By.ID, 'ageYear', '1982')
        self.age_form.submit()

    def go(self):
        pass
