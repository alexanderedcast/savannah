# coding=utf-8
from lettuce import step

from ui_automation.helper.methods.common.common_methods import CommonForCards
from ui_automation.helper.methods.pathway.pathway import Pathway
from ui_automation.helper.methods.pathway.update import UpdateCard
from ui_automation.helper.methods.pathway.update_ import SupportForUpdate
from ui_automation.helper.methods.pathway_journey.locators import PackLocators
from ui_automation.helper.methods.pathway_journey.read import ReadPackCard


@step('Find and "([^"]*)" Pathway and delete added card from Pathway')
#TODO: fix this issue this NonType
def step_impl(step, action):
    pathway = Pathway()
    card = SupportForUpdate()
    pathway_locator = PackLocators()
    pathway.menu_pathway(action)
    # before_deleted_card = pathway.lenght_card_inside_pathway()
    card.delete_smartcard_from_pathway(pathway_locator.delete_second_card_from_pathway)
    # after_deleted_card = pathway.lenght_card_inside_pathway()
    # expect(int(before_deleted_card) - 1).to(equal(after_deleted_card))
    pathway.publish()
    pathway.ok_ready_to_view()


@step('Check if you can read the "([^"]*)" with "([^"]*)"')
def step_impl(step, card_label, card_type):
    pack = ReadPackCard()
    pack.read_card(card_label, card_type, 1)


@step('Verify edit option for "([^"]*)"')
def step_impl(step, card_type):
    update = UpdateCard()
    common = CommonForCards()
    common.option_insight_dropdown_menu("Edit")
    update.update_card(card_type)