# coding=utf-8
import time
from expects import *
from lettuce import world, step
from selenium.webdriver.common.by import By

from ui_automation.environment.steps_config import driver_get
from ui_automation.helper.JS_tricks import JS_tricks
from ui_automation.helper.methods.actions import PageAction
from ui_automation.helper.methods.cards.create_card_with import CreateCardWith
from ui_automation.helper.methods.cards.locators import SmartCardLocators
from ui_automation.helper.methods.cards.read import ReadCard
from ui_automation.helper.methods.cards.update import UpdateAddCard
from ui_automation.helper.methods.cards.verification import VerificationCard
from ui_automation.helper.methods.common.all_cards import CardType
from ui_automation.helper.methods.common.common_methods import CommonForCards
from ui_automation.helper.methods.common.verification import VerificationMethods
from ui_automation.helper.methods.pathway_journey.locators import PackLocators
from ui_automation.helper.methods.wait import SupportWaitsAction
from ui_automation.test_data.read_json import read_json


@step('Verify that possible to read "([^"]*)"')
def step_impl(step, card_type):
    data_read = read_json('test_data')
    card_locator = SmartCardLocators()
    read = ReadCard()
    common = CommonForCards()
    if card_type == "Link":
        read.read_smartcard(card_locator.resource_inside_link_card)
    elif card_type == "Text":
        read.read_text_card(data_read["text card"])
    elif card_type == "Upload":
        read.read_smartcard(card_locator.image_container)
    elif card_type == "Poll":
        read.read_smartcard(card_locator.poll_radio)
        read.vote_inside_poll_card(card_locator.num_of_choices_inside_card, card_locator.poll_option_radio_button)
    elif card_type == "Poll with video":
        read.read_smartcard(card_locator.video_inside_card)
    elif card_type == "Quiz":
        read.read_smartcard(card_locator.inside_container)
    else:
        raise ValueError
    common.go_back_from_standalone()


@step('Verify that possible to "([^"]*)" a "([^"]*)" SmartCard')
def step_impl(step, option, card_type):
    wait = SupportWaitsAction()
    locator = SmartCardLocators()
    action = PageAction()
    update = UpdateAddCard()
    common = CommonForCards()
    data_read = read_json('test_data')
    common.option_insight_dropdown_menu(option)
    if card_type == "Link":
        world.text_before_update = action.actual_text(locator.text_card_details)
        update.link_card(data_read['link']['link_for_card_2'])
    elif card_type == "Upload":
        update.add_card()
        update.upload_card('update')
    elif card_type == "Poll":
        world.before_num_of_poll_options = len(driver_get().find_elements(By.XPATH, locator.quantity_of_poll_option))
        update.add_option_update_poll_card(data_read['poll']['choice 3'])
    elif card_type == "Text":
        world.text_before_update = action.actual_text(locator.text_card_details)
        update.text_card(data_read['text_after_editing'])
    elif card_type == "Quiz":
        pass
    else:
        raise ValueError
    print("This " + card_type + " SmartCard has been edited!" + "\n")
    time.sleep(3)
    wait.is_clickable(locator.button_create_smartcard)
    action.click(locator.button_create_smartcard)


@step('Verify the edit option for "([^"]*)" SmartCard')
def step_impl(step, card_type):
    locator = SmartCardLocators()
    action = PageAction()
    wait = SupportWaitsAction()
    common = CommonForCards()
    pathway_locator = PackLocators()
    card = CardType()
    data_read = read_json('test_data')
    verify = UpdateAddCard()
    if card_type == "Link":
        text_after_update = action.actual_text(locator.text_card_details + "\n")
        expect(world.text_before_update).to_not(equal(text_after_update))
    elif card_type == "Upload":
        # Find the way how to see the difference
        pass
    elif card_type == "Poll":
        time.sleep(2)
        after_num_of_poll_options = len(driver_get().find_elements(By.XPATH, locator.quantity_of_poll_option))
        expect(world.before_num_of_poll_options).to(be_below(after_num_of_poll_options))
    elif card_type == "Text":
        verify.verify_edit_text_card(data_read['text card'])
    elif card_type == "Poll with picture":
        common.option_insight_dropdown_menu("Edit")
        verify.change_title_poll_card(data_read['poll']['link'])
        wait.is_visible(locator.content_upload_player)
        card.submit_creation()
    else:
        raise ValueError


@step('"([^"]*)" a "([^"]*)" for SmartCard')
def step_impl(step, comment_action, action):
    data_read = read_json('test_data')
    common = CommonForCards()
    common.action_bar(action)
    if comment_action == "Leave":
        common.leave_comment_for_smartcard(data_read['text_for_comment'])
    elif comment_action == "Delete":
        common.delete_comment_for_smartcard()


@step('Verify that possible to "([^"]*)" a SmartCard')
def step_impl(step, action):
    verify = VerificationMethods()
    common = CommonForCards()
    if action == "completed":
        common.action_bar(action)
    elif action == "Mark as Complete":
        common.option_insight_dropdown_menu(action)
    verify.complet_action()


@step('Pick some card and "([^"]*)" and store title of this card')
def step_impl(step, option):
    common = CommonForCards()
    verify = VerificationMethods()
    js_help = JS_tricks()
    time.sleep(1)
    js_help.scroll_to_some_point(100)
    common.option_insight_dropdown_menu(option)
    verify.bookmark_action()
    world.card_info = common.store_info_about_card()


@step('Create "([^"]*)" "([^"]*)" with "([^"]*)"')
def step_impl(step, card_type, type_content, option):
    common = CommonForCards()
    cards = CreateCardWith()
    world.type_content = type_content
    common.creation_option_of_cards(type_content)
    cards.create_cards(card_type, option)


@step('Verify that card has been created with "([^"]*)"')
def step_impl(step, option):
    verify = VerificationCard()
    verify.verify_card(option)
