import time

from lettuce import world

from ui_automation.helper.methods.actions import PageAction
from ui_automation.helper.methods.cards.locators import SmartCardLocators
from ui_automation.helper.methods.journey.journey import Journey
from ui_automation.helper.methods.journey.locators import JourneyLocator
from ui_automation.helper.methods.pathway_journey.create import CreateCards
from ui_automation.helper.methods.pathway_journey.locators import PackLocators
from ui_automation.helper.methods.wait import SupportWaitsAction


class CreateJourney(CreateCards):

    def __init__(self):
        super(CreateJourney, self).__init__()
        self.pathway_locator = PackLocators()
        self.action = PageAction()
        self.wait = SupportWaitsAction()
        self.card_locator = SmartCardLocators()
        self.journey_locators = JourneyLocator()
        self.journey = Journey()

    def journey_create(self, card_type, type):
        time.sleep(1)
        world.pack_card_type = card_type
        data_pathway = read_json('test_data')
        self.wait.is_visible(self.pathway_locator.title)
        self.action.send_keys(self.pathway_locator.title, data_pathway['journey']['title'])
        # add type of journey
        self.journey.type(True, type)
        self.action.send_keys(self.journey_locators.section_title, data_pathway['journey']['section title'])
        self.wait.is_visible(self.pathway_locator.add_smartcard)
        self.action.click(self.pathway_locator.add_smartcard)
        self.action.click(self.pathway_locator.add_card_type % card_type)
        print("This is a " + card_type + " " + type + " Journey" + "\n")
        time.sleep(2)
        # for create card method
        self.types(card_type)
        # finish creation card
        self.journey.done_card()
        #publish card
        self.journey.publish()
        self.journey.ok_ready_to_view()

