import random

from ui_automation.helper.methods.common.all_cards import CardType
from ui_automation.helper.methods.pathway_journey.locators import PackLocators
from ui_automation.test_data.read_json import read_json


class CreateCards(CardType):

    def __init__(self):
        super(CreateCards, self).__init__()
        self.pathway_locator = PackLocators()

    def types(self, card_type):
        card_data = read_json('test_data')
        if card_type == "Link":
            self.link_card(card_data['link']['link_for_card_1'])
        elif card_type == "Upload":
            self.upload_from_device_card('my_device')
            self.wait.is_visible(self.card_locator.upload_content)
            self.action.click(self.card_locator.upload_content)
            self.wait.is_visible(self.pathway_locator.preview_upload)
        elif card_type == "Poll":
            self.poll_card(card_data['poll']['title'], card_data['poll']['choice 1'], card_data['poll']['choice 2'])
        elif card_type == "Text":
            self.text_card(card_data['text card'])
        elif card_type == "Quiz":
            self.quiz_card(card_data['quiz']['question'], card_data['quiz']['option 1'], card_data['quiz']['option 2'])
        elif card_type == "Dynamic Pathway":
            self.dynamic_card(card_data['dynamic_card_topic'], int(random.randrange(2, 3)))
        elif card_type == "From Bookmark":
            """
            use this pattern, because how issue with search result
            """
            self.bookmark_card("Python")
        elif card_type == "Search SmartCard":
            self.search_smartcard("Cats")
