from ui_automation.helper.API_helper.api_data import nik_token
from ui_automation.helper.API_helper.group import delete_first_group
from ui_automation.helper.methods.actions import PageAction
from ui_automation.helper.methods.wait import SupportWaitsAction
from ui_automation.test_data.read_json import read_json


class GroupLocators(object):
    group_create_window = "//div[@class='group-creation-modal']"
    create_group = "//div[@id='groups']//button[@type]//div/span[text()='Create Group']"
    group_name = "//div[@class='group-creation-modal']//input[@class='group-name']"
    group_description = "//div[@class='group-creation-modal']//textarea[@class='group-description']"
    submit_creation = "//div[@class='action-bar']//button[@class='create']"
    group_name_on_group_page = "//div//div[@class='matte group-name'][text()='%s']"
    group_description_on_group_page = "//div//div[contains(@style, 'margin')][text()='%s']"
    first_group_on_group_page = "(//div[@class='five-card-column']/div)[1]"
    message_about_created_group = "//div[@class='StatusModal']//div[text()]"
    confirm_create_group = "//div[@class='StatusModal']//button[@class='confirmStatus']"
    invite_button = "//div[@class='creator-curator']//button[@class='invite']"


class Groups(object):
    def __init__(self):
        self.group_locators = GroupLocators()
        self.data = read_json('test_data')
        self.action = PageAction()
        self.wait = SupportWaitsAction()

    def create_new_group(self):
        # delete first create group
        delete_first_group(nik_token)
        # click on create button
        self.wait.is_visible(self.group_locators.create_group)
        self.action.click(self.group_locators.create_group)
        # input data in order to create a new group
        self.wait.is_visible(self.group_locators.group_create_window)
        self.wait.is_visible(self.group_locators.group_name)
        self.action.send_keys(self.group_locators.group_name, self.data['group']['name'])
        self.wait.is_visible(self.group_locators.group_description)
        self.action.send_keys(self.group_locators.group_description, self.data['group']['description'])
        self.action.click(self.group_locators.submit_creation)
        self.verify_group_creation()


    def verify_group_creation(self):
        # submit creation group
        self.wait.is_visible(self.group_locators.confirm_create_group)
        self.action.click(self.group_locators.confirm_create_group)
        # get message of this
        message_about_created_group = self.action.actual_text(self.group_locators.message_about_created_group)
        self.wait.is_visible(self.group_locators.first_group_on_group_page)
        name = self.action.find_element('element', self.group_locators.group_name_on_group_page % self.data['group']['name'])
        description = self.action.find_element('element',self.group_locators.group_description_on_group_page % self.data['group']['description'])
        if name and description:
            print(message_about_created_group + "\n")
        else: raise Exception

    def invity_user_to_group(self):
        # click on created group
        self.wait.is_visible(self.group_locators.group_name_on_group_page % self.data['group']['name'])
        self.action.click(self.group_locators.group_name_on_group_page % self.data['group']['name'])
        # invite user to a group
        self.wait.is_visible(self.group_locators.invite_button)
        self.action.click(self.group_locators.invite_button)
