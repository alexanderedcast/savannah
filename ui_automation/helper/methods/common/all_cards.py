import os

from lettuce import world

from ui_automation.helper.methods.actions import PageAction
from ui_automation.helper.methods.cards.locators import SmartCardLocators
from ui_automation.helper.methods.wait import SupportWaitsAction


class CardType(object):

    """
    Class for creating card
    """

    def __init__(self):
        self.card_locator = SmartCardLocators()
        self.action = PageAction()
        self.wait = SupportWaitsAction()

    def link_card(self, link):
        self.action.clear(self.card_locator.link_input)
        self.action.send_keys(self.card_locator.link_input, value=link)
        self.wait.is_visible(self.card_locator.preview_upload)

    def upload_from_device_card(self, file_name):
        self.wait.is_visible(self.card_locator.upload_menu)
        self.action.send_keys(self.card_locator.input_my_device_upload, os.path.abspath('test_data/pic/%s.jpg' % file_name))

    def text_card(self, text):
        self.action.click(self.card_locator.text_input_area)
        self.action.clear(self.card_locator.text_input_area)
        self.action.send_keys(self.card_locator.text_input_area, value=text)

    def poll_card(self, message_or_link, first_choice, second_choice):
        self.action.send_keys(self.card_locator.link_input, value=message_or_link)
        self.action.send_keys(self.card_locator.first_choice_field, value=first_choice)
        self.action.send_keys(self.card_locator.second_choice_field, value=second_choice)

    def quiz_card(self, quiz_question, anwser_1, anwser_2):
        self.wait.is_visible(self.card_locator.link_input)
        self.action.send_keys(self.card_locator.link_input, quiz_question)
        # self.wait.is_visible(self.locators.first_field)
        self.action.send_keys(self.card_locator.first_field, anwser_1)
        self.action.mouse_hover(self.card_locator.correct_answer)
        # self.wait.is_visible(self.locators.second_field)
        self.action.send_keys(self.card_locator.second_field, anwser_2)

    def dynamic_card(self, topic, number_card):
        world.number_dynamic_card = number_card
        self.wait.is_visible(self.card_locator.enter_topic)
        self.action.send_keys(self.card_locator.enter_topic, topic)
        self.wait.is_visible(self.card_locator.number_dynamic_card % number_card)
        self.action.click(self.card_locator.number_dynamic_card % number_card)

    def bookmark_card(self, search_input):
        self.wait.is_visible(self.card_locator.link_input)
        self.action.send_keys(self.card_locator.link_input, search_input)
        self.wait.is_visible(self.card_locator.topic_for_bookmark_card)
        self.action.click(self.card_locator.topic_for_bookmark_card)

    def search_smartcard(self, search_input):
        self.bookmark_card(search_input)

    def submit_creation(self):
        self.wait.is_visible(self.card_locator.button_create_smartcard)
        self.action.click(self.card_locator.button_create_smartcard)

