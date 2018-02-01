# coding=utf-8
from ui_automation.helper.methods.actions import PageAction
from ui_automation.helper.methods.home.locators import HomePageLocators
from ui_automation.helper.methods.wait import SupportWaitsAction


class HomePage(object):
    def __init__(self):
        self.wait = SupportWaitsAction()
        self.action = PageAction()
        self.home_page_locator = HomePageLocators()

    def menu_profile(self, option):
        self.wait.wait_for_element_visibility(self.home_page_locator.profile_menu)
        self.action.click(self.home_page_locator.profile_menu)
        self.wait.wait_for_element_visibility(self.home_page_locator.option_profile_menu % option)
        self.action.click(self.home_page_locator.option_profile_menu % option)
