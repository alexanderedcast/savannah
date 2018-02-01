# coding=utf-8
import time
from lettuce import world

from ui_automation.helper.methods.cards.locators import SmartCardLocators
from ui_automation.helper.methods.common.all_cards import CardType
from ui_automation.helper.methods.common.common_methods import CommonForCards
from ui_automation.helper.methods.pathway_journey.locators import PackLocators
from ui_automation.helper.methods.wait import SupportWaitsAction
from ui_automation.test_data.read_json import read_json


class CreateCardWith(CardType):
    def __init__(self):
        super(CreateCardWith, self).__init__()
        self.card_locator = SmartCardLocators()
        self.wait = SupportWaitsAction()
        self.common = CommonForCards()
        self.pathway_locator = PackLocators()

    def create_cards(self, card_type, option):
        time.sleep(1)
        data = read_json('test_data')
        self.wait.is_visible(self.card_locator.type_of_smartcard % card_type)
        self.action.click(self.card_locator.type_of_smartcard % card_type)
        if card_type == "Poll":
            pass
        else:
            self.link_card(data['link']['link_for_card_1'])
        if option == "description":
            self.common.add_title(self.card_locator.description_input, data['link']['description'])
        elif option == "level of complexity":
            world.level_complexity = self.common.select_random_radio_button(self.card_locator.complexity_level)
            print("Level of complexity for this card: " + world.level_complexity + "\n")
        elif option == "tag":
            self.common.add_tag(data['tag'])
            print("This card created with tag: " + data['tag'])
        elif option == "link":
            self.poll_card(data['poll']['link'], data['poll']['choice 1'], data['poll']['choice 2'])
            self.wait.is_visible(self.card_locator.content_upload_player)
        elif option == "picture":
            self.poll_card(data['poll']['title'], data['poll']['choice 1'], data['poll']['choice 2'])
            self.wait.is_visible(self.card_locator.upload_picture)
            self.action.click(self.card_locator.upload_picture)
            self.upload_from_device_card('update')
            self.wait.is_visible(self.card_locator.upload_content)
            self.action.click(self.card_locator.upload_content)
            self.wait.is_visible(self.pathway_locator.preview_upload)
        elif option == "content provider":
            self.common.advanced_setting()
            # hard code so far , need to implement method which will be return name from login
            self.common.add_provider("Nik")
        elif option == "card type":
            self.common.advanced_setting()
            # hard code so far , need to find solution to pick the card type randomly
            world.choice = self.common.random_choice_dropdown_menu()
        self.submit_creation()