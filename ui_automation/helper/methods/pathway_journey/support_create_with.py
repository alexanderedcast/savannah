import time
from expects import *

from ui_automation.helper.methods.actions import PageAction
from ui_automation.helper.methods.cards.locators import SmartCardLocators
from ui_automation.helper.methods.common.all_cards import CardType
from ui_automation.helper.methods.common.common_methods import CommonForCards
from ui_automation.helper.methods.common.locator import CommonForCardLocator
from ui_automation.helper.methods.journey.locators import JourneyLocator
from ui_automation.helper.methods.pathway.pathway import Pathway
from ui_automation.helper.methods.pathway_journey.locators import PackLocators
from ui_automation.helper.methods.wait import SupportWaitsAction


class SupportCreatePackWith(object):

    def __init__(self):
        self.wait = SupportWaitsAction()
        self.action = PageAction()
        self.common = CommonForCards()
        self.card = CardType()
        self.pathway = Pathway()
        self.pack_locator = PackLocators()
        self.journey_locator = JourneyLocator()
        self.card_locator = SmartCardLocators()
        self.common_locator = CommonForCardLocator()

    def add_description(self, text_description):
        self.wait.is_visible(self.pack_locator.description)
        self.action.send_keys(self.pack_locator.description, value=text_description)

    def post_to_channel(self, channel_name):
        self.wait.is_visible(self.pack_locator.channel)
        self.action.click(self.pack_locator.channel)
        time.sleep(1)
        self.wait.is_visible(self.pack_locator.menu_channel)
        self.action.click(self.pack_locator.choose_channel % channel_name)

    def verify_added_channel(self, expected_channel):
        time.sleep(2)
        self.wait.is_visible(self.pack_locator.channel_name)
        actual = self.action.actual_text(self.pack_locator.channel_name)
        expect(actual).to(equal(expected_channel))

    def delete_channel_inside_card(self):
        self.wait.is_visible(self.pack_locator.delete_channel)
        self.wait.is_clickable(self.pack_locator.delete_channel)
        self.action.click(self.pack_locator.delete_channel)

    def add_level_of_complexity(self, locator):
        # return attribute
        return self.common.select_random_radio_button(locator)

    def add_tag_to_pack(self, tag_text):
        # common for cards
        self.common.add_tag(tag_text)

    def add_section_in_jounrey(self):
        self.wait.is_visible(self.journey_locator.add_section_button)
        self.wait.is_clickable(self.journey_locator.add_section_button)
        self.action.click(self.journey_locator.add_section_button)

    def upload_banner_for_card(self, file_name):
        self.wait.is_visible(self.pack_locator.card_banner)
        self.action.click(self.pack_locator.card_banner)
        self.card.upload_from_device_card(file_name)
        self.wait.is_visible(self.card_locator.upload_content)
        self.action.click(self.card_locator.upload_content)
        self.wait.is_visible(self.pack_locator.banner_preview)

    def draft_card(self):
        self.wait.is_visible(self.pack_locator.save_for_later)
        self.action.click(self.pack_locator.save_for_later)
        self.pathway.ok_ready_to_view()
        #self.wait.is_visible(self.common_locator.card_container)
        actual = self.action.actual_text(self.pack_locator.draft_label)
        expect(actual).to(equal("DRAFT"))
        print("This card on " + actual + "\n")
        self.common.option_insight_dropdown_menu("Edit")
