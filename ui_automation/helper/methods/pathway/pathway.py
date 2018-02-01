# # coding=utf-8
import time
from ui_automation.helper.JS_tricks import JS_tricks
from ui_automation.helper.methods.actions import PageAction
from ui_automation.helper.methods.cards.locators import SmartCardLocators
from ui_automation.helper.methods.common.common_methods import CommonForCards
from ui_automation.helper.methods.common.locator import CommonForCardLocator
from ui_automation.helper.methods.pathway_journey.locators import PackLocators
from ui_automation.helper.methods.wait import SupportWaitsAction


class Pathway(object):

    def __init__(self):
        self.pathway_locator = PackLocators()
        self.common_locator = CommonForCardLocator()
        self.card_locator = SmartCardLocators()
        self.action = PageAction()
        self.wait = SupportWaitsAction()
        self.js_tricks = JS_tricks()
        self.common = CommonForCards()

    def done_card(self):
        time.sleep(2)
        self.wait.is_visible(self.pathway_locator.done_card)
        self.action.click(self.pathway_locator.done_card)

    def publish(self):
        time.sleep(2)
        self.wait.is_clickable(self.pathway_locator.publish)
        self.action.click(self.pathway_locator.publish)

    def ok_ready_to_view(self):
        time.sleep(2)
        self.wait.is_visible(self.pathway_locator.ok_pathway)
        self.action.click(self.pathway_locator.ok_pathway)

    def menu_pathway(self, options):
        time.sleep(2)
        self.js_tricks.scroll_to_some_point(300)
        self.wait.is_visible(self.common_locator.insight_menu)
        self.action.click(self.pathway_locator.menu_pathway)
        self.action.click(self.common_locator.option_inside_menu % options)
        print("Choose the " + options + " option to the card" + "\n")

    def lenght_card_inside_pathway(self):
        self.action.length(self.pathway_locator.cards_inside_pathway)