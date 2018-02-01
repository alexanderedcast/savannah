# coding=utf-8
import time
from lettuce import world

from ui_automation.helper.methods.actions import PageAction
from ui_automation.helper.methods.cards.locators import SmartCardLocators
from ui_automation.helper.methods.pathway.pathway import Pathway
from ui_automation.helper.methods.pathway_journey.create import CreateCards
from ui_automation.helper.methods.pathway_journey.locators import PackLocators
from ui_automation.helper.methods.wait import SupportWaitsAction


class CreateSimplePathway(CreateCards):
    """
    Class for creating Pathway
    """

    def __init__(self):
        super(CreateSimplePathway, self).__init__()
        self.pathway_locator = PackLocators()
        self.action = PageAction()
        self.wait = SupportWaitsAction()
        self.card_locator = SmartCardLocators()
        self.pathway = Pathway()

    def pathway_create(self, card_type):
        world.pack_card_type = card_type
        time.sleep(1)
        data_pathway = read_json('test_data')
        self.wait.is_visible(self.pathway_locator.title)
        self.action.send_keys(self.pathway_locator.title, data_pathway['pathway']['title'])
        self.wait.is_visible(self.pathway_locator.add_smartcard)
        self.action.click(self.pathway_locator.add_smartcard)
        self.action.click(self.pathway_locator.add_card_type % card_type)
        print("This is a " + card_type + " Pathway" + "\n")
        time.sleep(2)
        # create cards
        self.types(card_type)
        self.pathway.done_card()
        self.pathway.publish()
        self.pathway.ok_ready_to_view()
