# coding=utf-8
import random

import time
from expects import expect, equal
from selenium.webdriver.common.by import By

from ui_automation.helper.methods.actions import PageAction
from ui_automation.helper.methods.cards.locators import SmartCardLocators
from ui_automation.helper.methods.common.all_cards import CardType
from ui_automation.helper.methods.common.locator import CommonForCardLocator
from ui_automation.helper.methods.pathway_journey.locators import PackLocators
from ui_automation.helper.methods.wait import SupportWaitsAction


class ReadCard(object):
    def __init__(self):
        self.cardtype = CardType()
        self.card_locator = SmartCardLocators()
        self.action = PageAction()
        self.wait = SupportWaitsAction()
        self.common_page_locator = CommonForCardLocator()
        self.pack_locator = PackLocators()

    def read_text_card(self, data_from_input):
        self.wait.is_visible(self.common_page_locator.card_container)
        text_outside_card = self.action.actual_text(self.card_locator.text_card_details)
        self.action.click(self.card_locator.to_inside_card)
        self.wait.is_visible(self.card_locator.text_card_details)
        text_inside_card = self.action.actual_text(self.card_locator.text_card_details)
        # compare data inside and out side the card
        expect(text_inside_card).to(equal(text_outside_card))
        # compare actual text with text on card
        expect(text_inside_card).to(equal(data_from_input))
        return

    def read_smartcard(self, locator):
        time.sleep(3)
        self.wait.is_visible(self.common_page_locator.card_container)
        self.wait.is_clickable(self.common_page_locator.card_container)
        self.action.click(self.card_locator.to_inside_card)
        if self.action.is_element_present(locator):
            print('Card has been quantity_skill_inside. Content is present!' + "\n")
        elif not self.action.is_element_present(locator):
            raise ValueError
        return

    def vote_inside_poll_card(self, locator, radio_button):
        choices = driver_get().find_elements(By.XPATH, locator)
        for i in range(len(choices)):
            random_num = random.randint(1, 2)
            self.wait.is_visible(self.card_locator.vertical_spacing)
            time.sleep(1)
            self.action.mouse_hover(radio_button % random_num)
            self.wait.is_clickable(self.card_locator.vote_poll_card)
            time.sleep(2)
            self.action.click(self.card_locator.vote_poll_card)
            break
