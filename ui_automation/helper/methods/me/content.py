import time

from expects import *

from ui_automation.helper.methods.actions import PageAction
from ui_automation.helper.methods.cards.cards import CreateCard
from ui_automation.helper.methods.common.common_methods import CommonForCards
from ui_automation.helper.methods.journey.simple_card import CreateJourney
from ui_automation.helper.methods.pathway.simple_card import CreateSimplePathway
from ui_automation.helper.methods.wait import SupportWaitsAction


class ContentLocators():
    left_filter = "//div[@class='left-filter']//div//span[text()='%s']"
    card_container = "//div[@data-reactroot]//div[contains(@class, 'card')]//div[@class='paper-card']"


class Content(object):
    def __init__(self):
        self.content_locator = ContentLocators()
        self.action = PageAction()
        self.wait = SupportWaitsAction()
        self.common = CommonForCards()
        self.card = CreateCard()
        self.pathway = CreateSimplePathway()
        self.journey = CreateJourney()

    def verify_content(self, option):
        time.sleep(2)
        self.wait.is_visible(self.content_locator.left_filter % "All")
        self.wait.is_clickable(self.content_locator.left_filter % "All")
        self.action.click(self.content_locator.left_filter % "All")
        time.sleep(2)
        if option == "All":
            all_card = len(self.action.find_element("elements", self.content_locator.card_container))
            expect(int(all_card)).to(equal(3))
        elif option == "SmartCards":
            self.wait.is_visible(self.content_locator.left_filter % option)
            self.wait.is_clickable(self.content_locator.left_filter % option)
            self.action.click(self.content_locator.left_filter % option)
            smartcard = len(self.action.find_element("elements", self.content_locator.card_container))
            expect(int(smartcard)).to(equal(1))
        elif option == "Pathways":
            self.wait.is_visible(self.content_locator.left_filter % option)
            self.wait.is_clickable(self.content_locator.left_filter % option)
            self.action.click(self.content_locator.left_filter % option)
            pathways = len(self.action.find_element("elements", self.content_locator.card_container))
            expect(int(pathways)).to(equal(1))
        elif option == "Journeys":
            self.wait.is_visible(self.content_locator.left_filter % option)
            self.wait.is_clickable(self.content_locator.left_filter % option)
            self.action.click(self.content_locator.left_filter % option)
            journey = len(self.action.find_element("elements", self.content_locator.card_container))
            expect(int(journey)).to(equal(1))
        elif option == "Completed":
            self.common.action_bar("completed")
            self.wait.is_visible(self.content_locator.left_filter % option)
            self.wait.is_clickable(self.content_locator.left_filter % option)
            self.action.click(self.content_locator.left_filter % option)
            completed = len(self.action.find_element("elements", self.content_locator.card_container))
            expect(int(completed)).to(equal(1))
        elif option == "Bookmarked":
            self.common.option_insight_dropdown_menu("Bookmark")
            self.wait.is_visible(self.content_locator.left_filter % option)
            self.wait.is_clickable(self.content_locator.left_filter % option)
            self.action.click(self.content_locator.left_filter % option)
            bookmarked = len(self.action.find_element("elements", self.content_locator.card_container))
            expect(int(bookmarked)).to(equal(1))
        print(option + " card" + "shown correctly" + "\n")

    def create_all_cards(self):
        type_of_contents = ["Pathway", "Journey", "SmartCard"]
        for content in type_of_contents:
            self.common.creation_option_of_cards(content)
            if content == "SmartCard":
                self.card.create_smartcard("Link")
            elif content == "Pathway":
                self.pathway.pathway_create("Link")
            elif content == "Journey":
                self.journey.journey_create("Link", 'self_paced')




