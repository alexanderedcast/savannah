import time

from lettuce import world

from ui_automation.helper.methods.journey.simple_card import CreateJourney
from ui_automation.helper.methods.pathway.create_with import CreatePathwayWith
from ui_automation.test_data.read_json import read_json


class CreateJourneyWith(CreatePathwayWith, CreateJourney):

    def __init__(self):
        super(CreateJourneyWith, self).__init__()

    def create_with_option(self, option, card_type="Text"):
        time.sleep(1)
        data_journey = read_json('test_data')
        self.wait.is_visible(self.pack_locator.title)
        self.action.send_keys(self.pack_locator.title, data_journey['journey']['title'])
        self.action.send_keys(self.journey_locators.section_title, data_journey['journey']['section title'])
        if option == "description":
            self.add_description(data_journey['journey']['description'])
        elif option == "post to channel":
            self.post_to_channel(data_journey['journey']['channel name'])
            self.verify_added_channel(data_journey['journey']['channel name'])
        elif option == "level of complexity":
            world.level_complexity = self.add_level_of_complexity(self.card_locator.complexity_level)
        elif option == "add tag":
            self.add_tag_to_pack(data_journey['journey']['tag'])
        elif option == "banner":
            self.upload_banner_for_card('zvezda')
        elif option == "after draft":
            self.draft_card()
        else:
            raise ValueError
        self.journey.type(True, "self_paced")
        self.wait.is_visible(self.pathway_locator.add_smartcard)
        self.action.click(self.pathway_locator.add_smartcard)
        self.action.click(self.pathway_locator.add_card_type % card_type)
        print("This is a " + card_type + " " + " Journey" + "\n")
        time.sleep(2)
        # for create card method
        self.types(card_type)
        # finish creation card
        self.journey.done_card()
        #publish card
        self.journey.publish()
        self.journey.ok_ready_to_view()

