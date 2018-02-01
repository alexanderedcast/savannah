from expects import *

from ui_automation.helper.methods.pathway.verfiy_create_with import VerifyCreationPathway
from ui_automation.test_data.read_json import read_json


class VerifyCreationJourney(VerifyCreationPathway):
    def __init__(self):
        super(VerifyCreationJourney, self).__init__()

    def creation_with(self, option):
        data_journey = read_json('test_data')
        if option == 'description':
            self.common.go_inside_card()
            self.wait.is_visible(self.pack_locator.description_inside_card)
            description = self.action.actual_text(self.pack_locator.description_inside_card)
            expect(description).to(equal(data_journey['journey']['description']))
            self.common.go_back_from_standalone()
        elif option == 'post to channel':
            # navigate to DISCOVER
            self.navigate.between_pages("DISCOVER")
            self.wait.is_clickable(self.discover_locator.channel_name % data_journey['journey']['channel name'])
            self.action.click(self.discover_locator.channel_name % data_journey['journey']['channel name'])
            self.js_trick.scroll_to_some_point(500)
            self.wait.is_visible(self.common_locator.card_container)
        elif option == "level of complexity":
            self.verify.level_complexity_outside_card()
        elif option == "add tag":
            self.verify.tag_option(data_journey['journey']['tag'])
        elif option == "draft":
            draft = self.action.is_element_present(self.pack_locator.draft_label)
            if draft:
                raise ValueError
            else:
                print("This card created after draft " + "\n")