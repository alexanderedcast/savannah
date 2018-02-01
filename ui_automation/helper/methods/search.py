from expects import *

from ui_automation.helper.methods.actions import PageAction
from ui_automation.helper.methods.wait import SupportWaitsAction


class SearchLocators(object):
    search_input = "(//div[@class='bootstrap-typeahead-input']//input[@class='form-control bootstrap-typeahead-input-main'])[1]"
    types_container = "//div[contains(@class, 'new-search')]"
    """
    1. People
    2. SmartCard
    3. Pathway
    """
    search_types = "//div[@class='outer-checkbox']//label[contains(text(), '%s')]/../../input"
    search_block = "//div[@class='result-block']//span[text()='%s']"


class Search(object):
    def __init__(self):
        self.search_locator = SearchLocators()
        self.action = PageAction()
        self.wait = SupportWaitsAction()

    def search_filter(self, value, type):
        self.wait.is_visible(self.search_locator.search_input)
        self.action.send_keys(self.search_locator.search_input, value=value)
        self.action.press_enter()
        self.wait.is_visible(self.search_locator.types_container)
        self.action.mouse_hover(self.search_locator.search_types % type)
        self.wait.is_visible(self.search_locator.search_block % type)
        expect(self.action.actual_text(self.search_locator.search_block % type)).to(equal(type))
