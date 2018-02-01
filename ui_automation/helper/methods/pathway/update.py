# coding=utf-8
import time

from ui_automation.helper.methods.cards.update import UpdateAddCard
from ui_automation.helper.methods.pathway.pathway import Pathway
from ui_automation.test_data.read_json import read_json


class UpdateCard(UpdateAddCard):
    def __init__(self):
        super(UpdateCard, self).__init__()
        self.pathway = Pathway()

    def update_card(self, card_type):
        data_read = read_json('test_data')
        self.add_card_into_pathway(card_type)
        if card_type == "Link":
            self.link_card(data_read['link']['link_for_card_2'])
        elif card_type == "Upload":
            self.upload_card('update')
            self.wait.is_visible(self.card_locator.upload_content)
            self.action.click(self.card_locator.upload_content)
            self.wait.is_visible(self.pathway_locator.preview_upload)
        elif card_type == "Poll":
            self.add_option_update_poll_card(data_read['poll']['choice 3'])
        elif card_type == "Text":
            self.text_card(data_read['text_after_editing'])
        self.pathway.done_card()
        time.sleep(2)
        self.pathway.publish()
        self.pathway.ok_ready_to_view()
        print("This " + card_type + " Pathway has been edited! " + "\n")
