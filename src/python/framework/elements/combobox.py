from src.python.framework.elements.label import Label
from src.python.framework.elements.base_element import BaseElement
from selenium.webdriver.common.action_chains import ActionChains
from src.python.framework.find import Find


class ComboBox(BaseElement):
    def hover_and_click_on_lbl(self, by, lbl_locator):
        self._hover_on_self()
        Find(Label, by, lbl_locator, context=self).click()

    def click_self_and_lbl(self, by, lbl_locator):
        self.click()
        Find(Label, by, lbl_locator, context=self).click()

    def _hover_on_self(self):
        action = ActionChains(self.driver)
        action.move_to_element(self).perform()
