import time
from lettuce import world



# TODO: NEED TO FINISH
from ui_automation.helper.methods.actions import PageAction
from ui_automation.helper.methods.cards.locators import SmartCardLocators
from ui_automation.helper.methods.common.common_methods import CommonForCards
from ui_automation.helper.methods.pathway.create_with import CreatePathwayWith
from ui_automation.helper.methods.pathway_journey.locators import PackLocators
from ui_automation.helper.methods.wait import SupportWaitsAction


class UpdateCard(CreatePathwayWith):

    def __init__(self):
        super(UpdateCard, self).__init__()
        self.wait = SupportWaitsAction()
        self.pathway_locator = PackLocators()
        self.card_locator = SmartCardLocators()
        self.action = PageAction()
        self.update = SupportForUpdate()
        self.common = CommonForCards()

    def edit(self, option):
        time.sleep(1)
        data = read_json('test_data')
        if option == "edit title":
            self.common.add_title(self.pathway_locator.title, data["pathway"]["new title"])
        elif option == "edit description":
            self.wait.is_visible(self.pathway_locator.description)
            self.action.clear(self.pathway_locator.description)
            self.action.send_keys(self.pathway_locator.description, data["pathway"]["new description"])
        elif option == "edit channel":
            self.action.click(self.pack_locator.delete_channel)
            self.post_to_channel("PRIVATE-NIK")
            self.verify_added_channel("PRIVATE-NIK")
        elif option == "edit level of complexity":
            world.level_complexity = self.common.select_random_radio_button(self.card_locator.complexity_level)
        elif option == "delete card from pathway":
            self.update.delete_smartcard_from_pathway(self.pack_locator.delete_first_card_from_pathway)
            publish_button = self.action.is_element_present(self.pack_locator.publish)
            if publish_button:
                raise AttributeError
            else:
                print("You cannot publish empty pathway!" + "\n")
                self.wait.is_visible(self.pack_locator.close_button_inside_pathway)
                self.action.click(self.pack_locator.close_button_inside_pathway)
        if option != "delete card from pathway":
            self.pathway.publish()
            self.pathway.ok_ready_to_view()


class SupportForUpdate(object):
    def __init__(self):
        self.wait = SupportWaitsAction()
        self.pathway_locator = PackLocators()
        self.action = PageAction()
        self.common_locator = CommonForCardLocator()

    def delete_smartcard_from_pathway(self, locator):
        self.wait.is_visible(locator)
        self.action.click(locator)
        self.wait.is_visible(self.common_locator.confirm_delete)
        self.action.click(self.common_locator.confirm_delete)
        print("SmartCard has been deleted from Pathway!" + "\n")
