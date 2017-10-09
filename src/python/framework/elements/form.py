from src.python.framework.elements.base_element import BaseElement
from src.python.framework.elements.select import Select
from src.python.framework.find import Find


class Form(BaseElement):
    def select_year(self, by, locator, value):
        selecter = Find(Select, by=by, locator=locator, context=self)
        selecter.select_option(value)