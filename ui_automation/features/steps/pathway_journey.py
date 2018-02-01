from lettuce import step, world

from ui_automation.helper.methods.common.common_methods import CommonForCards
from ui_automation.helper.methods.journey.create_with import CreateJourneyWith
from ui_automation.helper.methods.journey.update import UpdateJourney
from ui_automation.helper.methods.journey.verify_create_with import VerifyCreationJourney
from ui_automation.helper.methods.pathway.create_with import CreatePathwayWith
from ui_automation.helper.methods.pathway.update_ import UpdateCard
from ui_automation.helper.methods.pathway.verfiy_create_with import VerifyCreationPathway
from ui_automation.helper.methods.pathway_journey.main_action import PackMainActions


@step('Create "([^"]*)" with any card and "([^"]*)"')
def step_impl(step_instance, type_content, option):
    common = CommonForCards()
    pathway = CreatePathwayWith()
    journey = CreateJourneyWith()
    common.creation_option_of_cards(type_content)
    world.type_content = type_content
    if type_content == "Pathway":
        pathway.create_with_option(option)
    elif type_content == "Journey":
        journey.create_with_option(option)
    else:
        raise ValueError

@step('Verify that this "([^"]*)" has been created with "([^"]*)"')
def step_impl(step_instance, type_content, option):
    verify_pathway = VerifyCreationPathway()
    verify_journey = VerifyCreationJourney()
    if type_content == "Pathway":
        verify_pathway.creation_with(option)
    elif type_content == "Journey":
        verify_journey.creation_with(option)



@step('Edit "([^"]*)": "([^"]*)"')
def step_impl(step_instance, card_type, option):
    common = CommonForCards()
    update_pathway = UpdateCard()
    update_journey = UpdateJourney()
    common.option_insight_dropdown_menu("Edit")
    if card_type == "Pathway":
        update_pathway.edit(option)
    elif card_type == "Journey":
        update_journey.edit(option)


@step('"([^"]*)" a comment for "([^"]*)"')
def step_impl(step_instance, option, card):
    pack = PackMainActions()
    common = CommonForCards()
    if option == "Leave":
        pack.go_comment_pack_block(pack.leave_a_comment)
    elif option == "Delete":
        pack.go_comment_pack_block(pack.delete_comment_pack)
    pack.verify_comment(option)
    common.go_back_from_standalone()


@step('Verify that possible to completed "([^"]*)"')
def step_impl(step_instance, option):
    pack = PackMainActions()
    pack.complete_pack()