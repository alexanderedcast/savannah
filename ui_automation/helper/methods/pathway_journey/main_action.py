import string

import time
from expects import *

from ui_automation.helper.methods.actions import PageAction
from ui_automation.helper.methods.common.common_methods import CommonForCards
from ui_automation.helper.methods.common.locator import CommonForCardLocator
from ui_automation.helper.methods.common.verification import VerificationMethods
from ui_automation.helper.methods.pathway_journey.locators import PackLocators
from ui_automation.test_data.read_json import read_json


class Locators(PackLocators):
    def __init__(self):
        super(Locators, self).__init__()

    actions = "//div[@class='active-btns']//div[@class='icon-inline-block']//button[@class='%s']"
    card_overview = "//div[@class='modalContainer modal']//div[@class='card-overview']"
    comment_input = "//div[@class='modalContainer modal']//div[@class='comment-input-modal']//textarea[contains(@id, 'comment')]"
    text_for_first_comment = "(//div[@class='modalContainer modal']//div[@class='comments']//div//div[@class='comment-list-item']//small[@class='comment-text']/span[text()])[1]"
    comment_number = "(//div[@class='active-btns']//small[@class='actions-counter'])[2]"
    delete_comment = "(//small[@class='delete-action']/span)[1]"
    confirm_delete_comment_content = "//div[@class='container']"
    complete_pending_cards_message = "//div[@class='StatusModal']/p/span[contains(text(), 'all pending')]"


class PackMainActions(object):
    def __init__(self):
        self.common_page_locator = CommonForCardLocator()
        self.action_locator = Locators()
        self.common = CommonForCards()
        self.action = PageAction()
        self.wait = SupportWaitsAction()
        self.verify = VerificationMethods()
        self.data = read_json('test_data')

    def go_comment_pack_block(self, method):
        global amount_comment_before
        # click on comment button for Pack
        self.common.action_bar('comment')
        # wait for label
        self.wait.is_visible(self.action_locator.label)
        # check how many comment do you have
        amount_comment_before = self.common.convert_empty_string_to_zero(self.action_locator.comment_number)
        # click on comment button for Pack inside Pack Details
        self.action.click(self.action_locator.actions % "comment")
        # wait for visibility of pack modal container
        self.wait.is_visible(self.action_locator.card_overview)
        self.wait.is_visible(self.action_locator.comment_input)
        # calling method to leave or delete a comment
        method()
        # click on close cross
        self.action.click(self.action_locator.close_button_inside_pathway)

    def leave_a_comment(self):
        # leave a comment and press enter
        self.action.send_keys(self.action_locator.comment_input, self.data['text_for_comment'])
        self.action.press_enter()
        self.wait.is_visible(self.action_locator.text_for_first_comment)
        # verify that comment
        expect(self.action.actual_text(self.action_locator.text_for_first_comment)).to(
            equal(self.data['text_for_comment']))
        print("Leaved comment for Pack with text: " + self.data['text_for_comment'] + "\n")

    def delete_comment_pack(self):
        # delete card
        self.wait.is_clickable(self.action_locator.delete_comment)
        self.action.click(self.action_locator.delete_comment)
        # confirm deletion
        self.wait.is_visible(self.action_locator.confirm_delete_comment_content)
        self.action.click(self.common_page_locator.confirm_delete)
        print("Comment has been deleted" + "\n")

    def verify_comment(self, option):
        time.sleep(1)
        self.wait.is_visible(self.action_locator.label)
        amount_comment_after = self.common.convert_empty_string_to_zero(self.action_locator.comment_number)
        if option == "Leave":
            expect(int(amount_comment_after)).to(equal(int(amount_comment_before) + 1))
        elif option == "Delete":
            expect(int(amount_comment_after)).to(equal(int(amount_comment_before) - 1))

    def complete_pack(self):
        self.common.go_inside_card()
        self.common.action_bar("completed")
        self.verify.complet_action()
        self.action.click(self.action_locator.actions % "completed")
        message = self.action.is_element_present(self.action_locator.complete_pending_cards_message)
        if message: raise AttributeError
        elif not message:pass

    def leave_comment_inside_card(self):
        pass
