from lettuce import world

from ui_automation.helper.methods.journey.journey import Journey
from ui_automation.helper.methods.pathway.update_ import UpdateCard
from ui_automation.test_data.read_json import read_json


class UpdateJourney(UpdateCard):

    def __init__(self):
        super(UpdateJourney, self).__init__()
        self.journey = Journey()

    def edit(self, option):
        data = read_json('test_data')
        if option == "edit title":
            self.common.add_title(self.pathway_locator.title, data["journey"]["new title"])
        elif option == "edit description":
            self.wait.is_visible(self.pathway_locator.description)
            self.action.clear(self.pathway_locator.description)
            self.action.send_keys(self.pathway_locator.description, data["journey"]["new description"])
        elif option == "edit channel":
            self.action.click(self.pack_locator.delete_channel)
            self.post_to_channel("PRIVATE-NIK")
            self.verify_added_channel("PRIVATE-NIK")
        elif option == "edit level of complexity":
            world.level_complexity = self.common.select_random_radio_button(self.card_locator.complexity_level)
        elif option == "delete card from journey":
            self.update.delete_smartcard_from_pathway(self.pack_locator.delete_first_card_from_pathway)
            publish_button = self.action.is_element_present(self.pack_locator.publish)
            if publish_button:
                raise AttributeError
            else:
                print("You cannot publish empty journey!" + "\n")
                self.wait.is_visible(self.pack_locator.close_button_inside_pathway)
                self.action.click(self.pack_locator.close_button_inside_pathway)
        if option != "delete card from journey":
            self.journey.publish()
            self.journey.ok_ready_to_view()