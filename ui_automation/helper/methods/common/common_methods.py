import time
from lettuce import world
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select

from ui_automation.helper.JS_tricks import JS_tricks
from ui_automation.helper.methods.actions import PageAction
from ui_automation.helper.methods.cards.locators import SmartCardLocators
from ui_automation.helper.methods.common.locator import CommonForCardLocator
from ui_automation.helper.methods.home.locators import HomePageLocators
from ui_automation.helper.methods.wait import SupportWaitsAction


class CommonForCards(object):
    """
    Class with common actions with card
    """

    def __init__(self):
        self.action = PageAction()
        self.wait = SupportWaitsAction()
        self.common_page_locator = CommonForCardLocator()
        self.home_page_locator = HomePageLocators()
        self.card_locator = SmartCardLocators()
        self.js_tricks = JS_tricks()

    def creation_option_of_cards(self, type_content):
        time.sleep(3)
        self.wait.is_visible(self.home_page_locator.create_button)
        self.wait.is_clickable(self.home_page_locator.create_button)
        self.action.click(self.home_page_locator.create_button)
        self.wait.is_visible(self.home_page_locator.create_list)
        self.wait.is_visible(self.common_page_locator.type_of_card % type_content)
        self.action.click(self.common_page_locator.type_of_card % type_content)
        print("Creating the: " + type_content + "\n")

    def option_insight_dropdown_menu(self, options):
        time.sleep(3)
        self.js_tricks.scroll_to_some_point(400)
        self.wait.is_visible(self.common_page_locator.insight_menu)
        self.wait.is_clickable(self.common_page_locator.insight_menu)
        self.action.click(self.common_page_locator.insight_menu)
        self.action.click(self.common_page_locator.option_inside_menu % options)
        time.sleep(1)

    def action_bar(self, action):
        time.sleep(2)
        self.js_tricks.scroll_to_some_point(400)
        self.wait.is_visible(self.common_page_locator.action_in_action_bar % action)
        self.action.click(self.common_page_locator.action_in_action_bar % action)

    def convert_empty_string_to_zero(self, locator):
        string = self.action.actual_text(locator)
        num = [(x and int(x)) or 0 for x in string.split(',')]
        number_like_before = str(num)[1:-1]
        return number_like_before

    def leave_comment_for_smartcard(self, comment_text):
        self.wait.is_visible(self.common_page_locator.leave_comment_smartcard)
        self.action.send_keys(self.common_page_locator.leave_comment_smartcard, comment_text)
        self.action.press_enter()
        print("Card has been commented with text : " + self.action.actual_text(
            self.common_page_locator.expected_text_comment) + "\n")

    def delete_comment_for_smartcard(self):
        self.wait.is_visible(self.common_page_locator.delete_comment)
        if not self.action.is_element_present(self.common_page_locator.delete_comment):
            raise AttributeError
        self.js_tricks.scroll_to_some_point(50)
        self.action.click(self.common_page_locator.delete_comment)
        print(self.action.actual_text(self.common_page_locator.text_confirm_delete_option) + "\n")
        self.action.click(self.common_page_locator.confirm_delete)
        time.sleep(2)
        self.action.click(self.common_page_locator.arrow_go_back)
        # self.action.click(self.common_page_locator.close_rate_content)
        print("Comment has been deleted" + "\n")

    def get_data_from_statistic(self, stat):
        time.sleep(1)
        table_row_1 = self.action.actual_text(self.common_page_locator.statistic_table_row_1 % stat)
        table_row_2 = self.action.actual_text(self.common_page_locator.statistic_table_row_2 % stat)
        print(table_row_1 + " : " + table_row_2 + "\n")
        return table_row_2

    def add_to_new_pathway(self):
        time.sleep(1)
        self.wait.is_visible(self.common_page_locator.last_pathway)
        self.action.mouse_hover(self.common_page_locator.last_pathway)
        self.wait.is_visible(self.common_page_locator.add_to_pathway)
        self.action.click(self.common_page_locator.add_to_pathway)
        print("Editing to Pathway" + "\n")

    def add_to_channel(self, channel_name):
        time.sleep(2)
        self.action.mouse_hover(self.common_page_locator.post_to_channel_specific_name % channel_name)
        self.wait.is_clickable(self.common_page_locator.post_to_channel_button)
        self.action.click(self.common_page_locator.post_to_channel_button)

    def go_inside_channel(self, channel_name):
        time.sleep(2)
        self.js_tricks.scroll_to_some_point(100)
        if self.action.is_element_present(self.common_page_locator.group_name_in_channel % channel_name):
            self.wait.is_visible(self.common_page_locator.group_name_in_channel % channel_name)
            self.wait.is_clickable(self.common_page_locator.group_name_in_channel % channel_name)
            self.action.click(self.common_page_locator.group_name_in_channel % channel_name)

    def store_info_about_card(self):
        time.sleep(1)
        card_info = self.action.actual_text(self.card_locator.text_card_details)
        return card_info

    def go_inside_card(self):
        time.sleep(1)
        self.wait.is_clickable(self.common_page_locator.card_container)
        self.wait.is_visible(self.common_page_locator.card_container)
        self.action.click(self.card_locator.to_inside_card)

    def go_back_from_standalone(self):
        time.sleep(1)
        self.js_tricks.scroll_to_some_point(50)
        self.wait.is_visible(self.common_page_locator.arrow_go_back)
        self.action.click(self.common_page_locator.arrow_go_back)
        # self.wait.is_visible(self.common_page_locator.close_rate_content)
        # self.action.click(self.common_page_locator.close_rate_content)

    def select_random_radio_button(self, locator):
        options = driver_get().find_elements(By.XPATH, locator)
        for i in options:
            import random
            option = random.choice(options)
            attribute = option.get_attribute('value')
            option.click()
            return attribute

    def tommorow_date(self):
        import datetime
        today = datetime.datetime.today()
        correct_tommorow_date = datetime.datetime.strftime((today + datetime.timedelta(1)), '%m/%d/%Y')
        return correct_tommorow_date

    def add_tag(self, tag):
        self.wait.is_visible(self.common_page_locator.tag_input_field)
        self.action.send_keys(self.common_page_locator.tag_input_field, tag)
        self.action.press_enter()

    def add_title(self, locator, value):
        self.wait.is_visible(locator)
        self.action.clear(locator)
        self.action.send_keys(locator, value=value)

    def assing_to_me(self):
        self.wait.is_visible(self.common_page_locator.assign_window)
        self.action.click(self.common_page_locator.create_assign)
        self.wait.is_visible(self.common_page_locator.confirm_assign)
        self.action.click(self.common_page_locator.confirm_assign)
        self.wait.is_visible(self.common_page_locator.message_about_assign)
        print(self.action.actual_text(self.common_page_locator.message_about_assign) + "\n")

    def advanced_setting(self):
        self.wait.is_clickable(self.card_locator.advanced_setting)
        self.action.click(self.card_locator.advanced_setting)

    def add_provider(self, provider_name):
        self.wait.is_visible(self.card_locator.provider_name)
        self.action.send_keys(self.card_locator.provider_name, provider_name)
        return provider_name

    def random_choice_dropdown_menu(self, ):
        time.sleep(2)
        my_select = Select(self.action.find_element("element", self.card_locator.dropdown_menu))
        card_type = "Livefeed"
        my_select.select_by_visible_text(card_type)
        return card_type.upper()

