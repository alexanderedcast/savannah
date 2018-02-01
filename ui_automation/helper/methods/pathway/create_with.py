import time
from lettuce import world

from ui_automation.helper.methods.actions import PageAction
from ui_automation.helper.methods.cards.locators import SmartCardLocators
from ui_automation.helper.methods.common.all_cards import CardType
from ui_automation.helper.methods.common.common_methods import CommonForCards
from ui_automation.helper.methods.pathway.pathway import Pathway
from ui_automation.helper.methods.pathway_journey.locators import PackLocators
from ui_automation.helper.methods.pathway_journey.support_create_with import SupportCreatePackWith
from ui_automation.helper.methods.wait import SupportWaitsAction


class CreatePathwayWith(CardType, SupportCreatePackWith):
    """
    Class for creating Pathway with different optional
    """

    def __init__(self):
        super(CreatePathwayWith, self).__init__()
        self.pack_locator = PackLocators()
        self.action = PageAction()
        self.wait = SupportWaitsAction()
        self.card_locator = SmartCardLocators()
        self.pathway = Pathway()
        self.common = CommonForCards()
        self.card = CardType()

    def create_with_option(self, option, card_type="Text"):
        time.sleep(1)
        data_pathway = read_json('test_data')
        self.wait.is_visible(self.pack_locator.title)
        self.action.send_keys(self.pack_locator.title, data_pathway['pathway']['title'])
        if option == "description":
            self.add_description(data_pathway['pathway']['description'])
        elif option == "post to channel":
            self.post_to_channel(data_pathway['pathway']['channel name'])
            self.verify_added_channel(data_pathway['pathway']['channel name'])
        elif option == "level of complexity":
            world.level_complexity = self.add_level_of_complexity(self.card_locator.complexity_level)
        elif option == "add tag":
            self.add_tag_to_pack(data_pathway['pathway']['tag'])
        elif option == "banner":
            self.upload_banner_for_card('zvezda')
        elif option == "after draft":
            self.draft_card()
        time.sleep(1)
        self.wait.is_visible(self.pack_locator.add_smartcard)
        self.wait.is_clickable(self.pack_locator.add_smartcard)
        self.action.click(self.pack_locator.add_smartcard)
        self.action.click(self.pack_locator.add_card_type % card_type)
        print("This is a " + card_type + " Pathway" + "\n")
        time.sleep(2)
        # for all tests I will create text card
        self.text_card(data_pathway['text card'])
        self.pathway.done_card()
        self.pathway.publish()
        self.pathway.ok_ready_to_view()