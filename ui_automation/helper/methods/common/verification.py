# coding=utf-8
import time
from expects import *
from lettuce import world

from ui_automation.helper.JS_tricks import JS_tricks
from ui_automation.helper.methods.actions import PageAction
from ui_automation.helper.methods.cards.locators import SmartCardLocators
from ui_automation.helper.methods.common.common_methods import CommonForCards
from ui_automation.helper.methods.common.locator import CommonForCardLocator
from ui_automation.helper.methods.pathway_journey.locators import PackLocators
from ui_automation.helper.methods.wait import SupportWaitsAction


class VerificationMethods(object):

    def __init__(self):
        self.action = PageAction()
        self.wait = SupportWaitsAction()
        self.common_locator = CommonForCardLocator()
        self.pathway_locator = PackLocators()
        self.card_locator = SmartCardLocators()
        self.js_tricks = JS_tricks()
        self.common = CommonForCards()

    def delete_option(self):
        self.action.is_element_present(self.common_locator.text_confirm_delete_option)
        self.action.click(self.common_locator.confirm_delete)
        msg = self.action.actual_text(self.common_locator.message_about_card_deleted)
        print(msg + "\n")
        self.js_tricks.scroll_to_some_point(700)

    def complet_action(self):
        self.wait.is_visible(self.common_locator.text_about_completed_card)
        actual_message = self.action.actual_text(self.common_locator.text_about_completed_card)
        expected_message = "Marked as complete"
        expect(actual_message).to(equal(expected_message))
        print("You " + actual_message + " card. " + "\n")

    def adding_to_channel(self):
        time.sleep(2)
        expected_message = "Content has been posted to the selected channel(s). If it is a curated channel, your post will be visible once approved by the curator."
        self.wait.is_visible(self.common_locator.message_content_posted)
        actual_message = self.action.actual_text(self.common_locator.message_content_posted)
        expect(expected_message).to(equal(actual_message))
        self.wait.is_visible(self.pathway_locator.ok_pathway)
        self.action.click(self.pathway_locator.ok_pathway)
        time.sleep(2)

    def add_to_pathway(self):
        self.wait.is_visible(self.common_locator.message_text)
        actual_message = self.action.actual_text(self.common_locator.message_text)
        expected_message = "Card successfully added to Pathway(s)!"
        expect(actual_message).to(equal(expected_message))
        print(actual_message + "\n")

    def bookmark_action(self):
        time.sleep(1)
        expected_text = "Done! This SmartCard has been Bookmarked."
        having_text = self.action.actual_text(self.common_locator.message_text)
        expect(having_text).to(equal(expected_text))
        print(having_text)

    def description(self, expected):
        time.sleep(1)
        self.wait.is_visible(self.card_locator.text_card_details)
        text = self.action.actual_text(self.card_locator.text_card_details)
        expect(text).to(equal(expected))

    def level_complexity_outside_card(self):
        self.wait.is_visible(self.common_locator.card_container)
        self.wait.is_visible(self.common_locator.level_complexity_on_card)
        actual_level_on_card = self.action.actual_text(self.common_locator.level_complexity_on_card).lower()
        expect(actual_level_on_card).to(equal(world.level_complexity))

    def level_complexity_inside_card(self):
        self.wait.is_visible(self.common_locator.level_complexity_inside_card)
        actual_level_inside_card = self.action.actual_text(self.common_locator.level_complexity_inside_card).lower()
        expect(actual_level_inside_card).to(equal(world.level_complexity))

    def tag_option(self, tag):
        self.common.option_insight_dropdown_menu("Show Tags")
        self.wait.is_visible(self.common_locator.tags_on_card)
        actual_tag = self.action.actual_text(self.common_locator.tags_on_card)
        expect(actual_tag).to(equal(tag))

    def assign_to_me(self):
        self.wait.is_visible(self.common_locator.number_of_assignment)
        actual_number = self.action.actual_text(self.common_locator.number_of_assignment)
        expect(int(actual_number)).to(be_above(0))
        print("You have " + str(actual_number) + " assignment[s]" + "\n")
        self.action.is_element_present(self.common_locator.card_container)

