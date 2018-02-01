# coding=utf-8
import time
from expects import expect, equal

from ui_automation.helper.methods.actions import PageAction
from ui_automation.helper.methods.cards.locators import SmartCardLocators
from ui_automation.helper.methods.common.all_cards import CardType
from ui_automation.helper.methods.pathway_journey.locators import PackLocators
from ui_automation.helper.methods.wait import SupportWaitsAction


class UpdateAddCard(object):

    def __init__(self):
        self.cardtype = CardType()
        self.card_locator = SmartCardLocators()
        self.action = PageAction()
        self.wait = SupportWaitsAction()
        self.pathway_locator = PackLocators()

    def add_card_into_pathway(self, card_type):
        self.wait.is_visible(self.pathway_locator.add_smartcard)
        self.action.click(self.pathway_locator.add_smartcard)
        self.action.click(self.pathway_locator.add_card_type % card_type)

    def text_card(self, text):
        return self.cardtype.text_card(text)

    def link_card(self, link):
        self.wait.is_visible(self.card_locator.description_input)
        self.action.clear(self.card_locator.description_input)
        self.action.clear(self.card_locator.link_input)
        self.action.send_keys(self.card_locator.link_input, value=link)
        time.sleep(3)

    def add_card(self):
        time.sleep(1)
        self.wait.is_visible(self.card_locator.change_image)
        self.action.click(self.card_locator.change_image)

    def upload_card(self, file_name):
        self.cardtype.upload_from_device_card(file_name)
        self.wait.is_visible(self.card_locator.upload_content)
        self.action.click(self.card_locator.upload_content)

    def add_option_update_poll_card(self, data):
        self.action.click(self.card_locator.add_choice)
        self.action.send_keys(self.card_locator.third_choice_field, data)

    def change_title_poll_card(self, value):
        self.wait.is_visible(self.card_locator.link_input)
        self.action.clear(self.card_locator.link_input)
        self.action.send_keys(self.card_locator.link_input, value=value)

    def verify_edit_text_card(self, data):
        time.sleep(1)
        self.wait.is_visible(self.card_locator.text_card_details)
        new_text = self.action.actual_text(self.card_locator.text_card_details)
        expect(new_text).to(equal(data))
