# coding=utf-8
import time

from ui_automation.helper.JS_tricks import JS_tricks
from ui_automation.helper.methods.actions import PageAction
from ui_automation.helper.methods.wait import SupportWaitsAction


class NavigationLocators(object):
    top_menu = "//div[@data-reactroot]//div[@id='secondary-nav']//ul[@class='menu']/li[@data-radium]//span[@class]/span[text()='%s']/../../span"
    me_category = "//div[@data-reactroot]//div[@class='profile-tabs']//div[@class][text()='%s']"
    home_category = "//div[@data-reactroot]//div[@class]//div[contains(@class, 'feed-tab')]//span[text()='%s']"


class Navigation(object):
    def __init__(self):
        self.action = PageAction()
        self.wait = SupportWaitsAction()
        self.navigation_locator = NavigationLocators()
        self.js_trick = JS_tricks()

    def between_pages(self, category):
        time.sleep(1)
        self.wait.wait_for_elem(self.navigation_locator.top_menu % category)
        self.action.click(self.navigation_locator.top_menu % category)

    def me_page(self, subcategory):
        time.sleep(2)
        self.wait.is_clickable(self.navigation_locator.me_category % subcategory)
        self.action.click(self.navigation_locator.me_category % subcategory)

    def home_page(self, subcategory):
        time.sleep(2)
        self.js_trick.scroll_to_some_point(50)
        self.wait.is_clickable(self.navigation_locator.home_category % subcategory)
        self.action.click(self.navigation_locator.home_category % subcategory)
