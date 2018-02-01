# coding=utf-8
import time

from ui_automation.helper.methods.actions import PageAction
from ui_automation.helper.methods.cards.locators import SmartCardLocators
from ui_automation.helper.methods.common.all_cards import CardType
from ui_automation.helper.methods.wait import SupportWaitsAction
from ui_automation.test_data.read_json import read_json


class CreateCard(object):

    def __init__(self):
        self.cardtype = CardType()
        self.card_locator = SmartCardLocators()
        self.action = PageAction()
        self.wait = SupportWaitsAction()

    def create_smartcard(self, card_type):
        data = read_json('test_data')
        time.sleep(1)
        self.wait.is_visible(self.card_locator.type_of_smartcard % card_type)
        self.action.click(self.card_locator.type_of_smartcard % card_type)
        print("This is a " + card_type + " SmartCard" + "\n")
        time.sleep(1)
        if card_type == 'Link':
            self.cardtype.link_card(data['link']['link_for_card_1'])
        elif card_type == "Upload":
            self.cardtype.upload_from_device_card('my_device')
            self.wait.is_visible(self.card_locator.upload_content)
            self.action.click(self.card_locator.upload_content)
            self.wait.is_visible(self.card_locator.change_image)
            self.wait.is_visible(self.card_locator.button_create_smartcard)
        elif card_type == "Text":
            self.cardtype.text_card(data["text card"])
        elif card_type == "Poll":
            self.cardtype.poll_card(data['poll']['title'], data['poll']['choice 1'], data['poll']['choice 2'])
        elif card_type == "Quiz":
            self.cardtype.quiz_card(data['quiz']['question'], data['quiz']['option 1'], data['quiz']['option 2'])
        self.cardtype.submit_creation()



