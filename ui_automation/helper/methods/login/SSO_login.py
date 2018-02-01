from helper.methods.actions import PageAction
from helper.methods.login.locators import LoginPageLocator
from helper.methods.wait import SupportWaitsAction


class SSOLogin(object):

    def __init__(self):
        self.login_page_locator = LoginPageLocator()
        self.action = PageAction()
        self.wait = SupportWaitsAction()


    def FB_login(self,email, password):
        self.action.is_element_present(self.login_page_locator.fb_email_input)
        self.action.send_keys(self.login_page_locator.fb_email_input, value=email)
        self.action.send_keys(self.login_page_locator.fb_password_input, value=password)
        self.action.click(self.login_page_locator.fb_login_button)


    def google_login(self, email, password):
        self.wait.is_visible(self.login_page_locator.input_gmail_email)
        self.action.send_keys(self.login_page_locator.input_gmail_email, value=email)
        self.action.click(self.login_page_locator.button_next_gmail)
        self.wait.is_visible(self.login_page_locator.input_gmail_password)
        self.action.send_keys(self.login_page_locator.input_gmail_password, value=password)
        self.action.click(self.login_page_locator.button_next_gmail)


    def linkedin_login(self, email, password):
        self.wait.is_visible(self.login_page_locator.linkedin_email)
        self.action.send_keys(self.login_page_locator.linkedin_email, value=email)
        self.action.send_keys(self.login_page_locator.linkedin_password, value=password)
        self.action.click(self.login_page_locator.linkedin_submit)