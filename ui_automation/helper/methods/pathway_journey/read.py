import time

from expects import *
from lettuce import world

from ui_automation.helper.methods.actions import PageAction
from ui_automation.helper.methods.cards.read import ReadCard
from ui_automation.helper.methods.common.common_methods import CommonForCards
from ui_automation.helper.methods.common.locator import CommonForCardLocator
from ui_automation.helper.methods.pathway_journey.locators import PackLocators
from ui_automation.helper.methods.wait import SupportWaitsAction


class ReadPackCard(object):

    def __init__(self):
        self.common = CommonForCards()
        self.wait = SupportWaitsAction()
        self.pack_locator = PackLocators()
        self.action = PageAction()
        self.common_locator = CommonForCardLocator()
        self.read = ReadCard()

    def read_logo_inside_card(self, logo_name):
        logo = self.action.is_element_present(self.pack_locator.card_logo % logo_name)
        if not logo:
            raise ValueError
        print("You have the " + self.action.actual_text(
            self.pack_locator.card_logo % logo_name) + " inside a Pathway" + "\n")

    def read_card(self, card_label, card_type, expected_number_cards):
        time.sleep(1)
        self.common.go_inside_card()
        time.sleep(1)
        self.wait.is_visible(self.pack_locator.label)
        label = self.action.actual_text(self.pack_locator.label)
        expect(str(label)).to(equal(str(card_label.upper())))
        print("You are reading the " + label + "\n")
        actual_num_contaniners = self.action.length(self.common_locator.card_container)
        if world.pack_card_type == "Dynamic Pathway":
            expect(actual_num_contaniners).to(equal(int(world.number_dynamic_card)))
        else:
            expect(actual_num_contaniners).to(equal(int(expected_number_cards)))
        print("Inside a pathway you have: " + str(actual_num_contaniners) + " card[s]" + "\n")
        self.common.go_inside_card()
        self.wait.is_visible(self.pack_locator.card_overview_content)
        if card_type == "Link":
            self.action.is_element_present(self.pack_locator.image_link)
            self.read_logo_inside_card('ARTICLE')
        elif card_type == "Upload":
            self.action.is_element_present(self.pack_locator.card_image_block)
            self.read_logo_inside_card('IMAGE')
        elif card_type == "Poll":
            self.read_logo_inside_card('POLL')
            self.read.vote_inside_poll_card(self.pack_locator.poll_option, self.pack_locator.radio_button)
        elif card_type == "Quiz":
            self.read_logo_inside_card('QUIZ')
        elif card_type == "Text":
            self.read_logo_inside_card('TEXT')
        else:
            pass
        self.wait.is_visible(self.pack_locator.close_button_inside_pathway)
        self.action.click(self.pack_locator.close_button_inside_pathway)
        self.common.go_back_from_standalone()
