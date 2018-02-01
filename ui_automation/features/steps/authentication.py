from lettuce import world, step

from ui_automation.helper.methods.actions import PageAction
from ui_automation.helper.methods.home.home_page import HomePage
from ui_automation.helper.methods.login.login_page import Login
from ui_automation.helper.methods.wait import SupportWaitsAction
from ui_automation.test_data.read_json import read_json

action = PageAction()
wait = SupportWaitsAction()
home = HomePage()


@step('Sign in as "([^"]*)"')
def login_with_email(step_instance, option):
    login = Login()
    world.users = read_json('users')
    if option == "existing user":
        login.valid_email(world.users['existing_users'][world.config['env']['user']]['email'], world.users['existing_users'][world.config['env']['user']]['password'])
    elif option == "user what need to restore password":
        login.valid_email(world.users['restore']['email'], world.users['restore']['password'])
    else:
        raise AttributeError



@step('Verify the login has been "([^"]*)"')
def step_impl(step, login_result):
    world.login_result = login_result
    verify = VerifyLogin()
    if login_result == "successful":
        verify.successful_login()
    elif login_result == "invalid":
        verify.unsuccessful_login()

@step("Reset my password")
def step_impl(step):
    restore = ResotorePassword()
    user = read_json('users')
    delete_email(user['gmail']['email'], user['gmail']['password'])
    if world.login_result == 'invalid':
        restore.restore_password_send_email(user['restore']['email'])
        restore.get_link_from_email(user['gmail']['email'], user['gmail']['password'])
        restore.input_new_password(user['restore']['new password'])
        print('Password has been successfully restored' + "\n")
    delete_email(user['gmail']['email'], user['gmail']['password'])


@step('Do "([^"]*)" from the system')
def step_impl(step, option):
    home.menu_profile(option)
    login_locator = LoginPageLocator()
    a = action.is_element_present(login_locator.login_button)
    if a:
        print(option + " option " + " has been completed" + ".\n")
    elif not a:
        print(option + " option " + " doesn't work" + ".\n")
        raise ValueError


@step('Log in with "([^"]*)" SSO')
def step_impl(step, sso_option):
    world.sso = sso_option
    login_locator = LoginPageLocator()
    wait.is_clickable(login_locator.sso_option % sso_option)
    action.click(login_locator.sso_option % sso_option)
    print('Trying login with %s' % sso_option + ".\n")


