from expects import *

from ui_automation.helper.JS_tricks import JS_tricks
from ui_automation.helper.methods.actions import PageAction
from ui_automation.helper.methods.common.common_methods import CommonForCards
from ui_automation.helper.methods.common.locator import CommonForCardLocator
from ui_automation.helper.methods.common.verification import VerificationMethods
from ui_automation.helper.methods.discover.locators import DiscoverLocators
from ui_automation.helper.methods.navigation import Navigation
from ui_automation.helper.methods.pathway_journey.locators import PackLocators
from ui_automation.helper.methods.wait import SupportWaitsAction
from ui_automation.test_data.read_json import read_json


class VerifyCreationPathway(object):
    def __init__(self):
        self.action = PageAction()
        self.wait = SupportWaitsAction()
        self.common = CommonForCards()
        self.navigate = Navigation()
        self.pack_locator = PackLocators()
        self.discover_locator = DiscoverLocators()
        self.common_locator = CommonForCardLocator()
        self.verify = VerificationMethods()
        self.js_trick = JS_tricks()

    def creation_with(self, option):
        data = read_json('test_data')
        if option == 'description':
            self.common.go_inside_card()
            self.wait.is_visible(self.pack_locator.description_inside_card)
            description = self.action.actual_text(self.pack_locator.description_inside_card)
            expect(description).to(equal(data['pathway']['description']))
            self.common.go_back_from_standalone()
        elif option == 'post to channel':
            # navigate to DISCOVER
            self.navigate.between_pages("DISCOVER")

            self.wait.is_clickable(self.discover_locator.channel_name % data['pathway']['channel name'])
            self.action.click(self.discover_locator.channel_name % data['pathway']['channel name'])
            self.js_trick.scroll_to_some_point(500)
            self.wait.is_visible(self.common_locator.card_container)
            self.common.option_insight_dropdown_menu("Delete")
            self.verify.delete_option()
        elif option == "level of complexity":
            self.verify.level_complexity_outside_card()
        elif option == "add tag":
            self.verify.tag_option(data['pathway']['tag'])
        elif option == "draft":
            draft = self.action.is_element_present(self.pack_locator.draft_label)
            if draft:
                raise ValueError
            else: print("This card created after draft " + "\n")




