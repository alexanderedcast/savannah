# coding=utf-8
from helper.methods.actions import PageAction
from helper.methods.home.locators import HomePageLocators
from helper.methods.login.locators import LoginPageLocator
from helper.methods.wait import SupportWaitsAction


class VerifyLogin(object):
    def __init__(self):
        self.login_page_locator = LoginPageLocator()
        self.home_page_locator = HomePageLocators()
        self.action = PageAction()
        self.wait = SupportWaitsAction()

    # Verify why two same value not equal
    def successful_login(self):
        self.wait.is_visible(self.home_page_locator.create_button)
        expected_user = self.action.actual_text(self.login_page_locator.expected_user)
        #expect(expected_user).to(be(equal(world.user['existing_users']['admin']['first name'])))
        print("Login has been successful. You logged in as %s" % expected_user + "\n")


    def unsuccessful_login(self):
        if self.action.is_element_present(self.login_page_locator.invalid_email):
            print(self.action.actual_text(self.login_page_locator.invalid_email))