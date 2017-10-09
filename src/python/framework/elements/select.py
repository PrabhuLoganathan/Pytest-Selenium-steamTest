from src.python.framework.elements.base_element import BaseElement


class Select(BaseElement):
    def select_option(self, option):
        items_list = self.get_options()
        for item in items_list:
            if item.get_attribute("value") == option:
                item.click()
                break

    def get_options(self):
        return self.find_elements_by_tag_name('option')