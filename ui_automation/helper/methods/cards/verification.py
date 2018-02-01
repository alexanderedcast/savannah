# coding=utf-8
import time

from expects import *
from lettuce import world
from selenium.webdriver.common.by import By

from ui_automation.helper.methods.common.common_methods import CommonForCards
from ui_automation.helper.methods.common.verification import VerificationMethods
from ui_automation.test_data.read_json import read_json


class VerificationCard(VerificationMethods):
    def __init__(self):
        super(VerificationCard, self).__init__()
        self.common = CommonForCards()

    def verify_card(self, option, inside_menu="Show Tags"):
        time.sleep(2)
        data = read_json('test_data')
        if option == "description":
            self.description(data['link']['description'])
            print("This card created properly with description: " + data['link']['description'] + "\n")
        elif option == "level of complexity":
            self.level_complexity_outside_card()
            self.common.go_inside_card()
            self.level_complexity_inside_card()
            self.common.go_back_from_standalone()
        elif option == "tag":
            self.common.option_insight_dropdown_menu(inside_menu)
            self.wait.is_visible(self.common_locator.tags_on_card)
            actual_tag = self.action.actual_text(self.common_locator.tags_on_card)
            expect(actual_tag).to(equal(data['tag']))
            print("This tags are match: " + data['tag'])
        elif option == "content provider":
            # go to card details
            self.wait.is_clickable(self.card_locator.to_inside_card)
            self.action.click(self.card_locator.to_inside_card)

            # hard code before implementing method
            self.action.find_element("element", "Nik", By.LINK_TEXT)

            self.common.go_back_from_standalone()
        elif option == "card type":
            self.wait.is_clickable(self.card_locator.to_inside_card)
            self.action.click(self.card_locator.to_inside_card)
            expect(world.choice).to(equal(self.action.actual_text(self.card_locator.card_type_inside_card)))
            print("Card type for this card is: " + world.choice)
            self.common.go_back_from_standalone()







