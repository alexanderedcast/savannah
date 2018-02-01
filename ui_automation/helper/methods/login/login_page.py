# coding=utf-8
from ui_automation.environment.steps_config import driver_get
from ui_automation.helper.API_helper.get_email import read_email
from ui_automation.helper.methods.actions import PageAction
from ui_automation.helper.methods.login.locators import LoginPageLocator
from ui_automation.helper.methods.wait import SupportWaitsAction


class Login(object):

    def __init__(self):
        self.login_page_locator = LoginPageLocator()
        self.action = PageAction()
        self.wait = SupportWaitsAction()

    def valid_email(self, email, password):
        self.action.send_keys(self.login_page_locator.email, value=email)
        self.action.send_keys(self.login_page_locator.password, value=password)
        self.action.click(self.login_page_locator.login_button)

    def login_as_existing_user(self):
        pass


class ResotorePassword(object):

    def __init__(self):
        self.login_page_locator = LoginPageLocator()
        self.action = PageAction()
        self.wait = SupportWaitsAction()

    def restore_password_send_email(self, email):
        self.action.click(self.login_page_locator.forgot_password)
        self.wait.is_visible(self.login_page_locator.email_input_forgot_password)
        self.action.send_keys(self.login_page_locator.email_input_forgot_password, value=email)
        self.action.click(self.login_page_locator.submit_reset_password)

    def get_link_from_email(self, email, password):
        url = read_email(email, password, "[EdCast] Reset your password")
        driver_get().get(url)

    def input_new_password(self, password):
        self.wait.is_visible(self.login_page_locator.new_password)
        self.action.send_keys(self.login_page_locator.new_password, value=password)
        self.wait.is_visible(self.login_page_locator.confirm_password)
        self.action.send_keys(self.login_page_locator.confirm_password, value=password)
        self.action.click(self.login_page_locator.reset_password_button)
