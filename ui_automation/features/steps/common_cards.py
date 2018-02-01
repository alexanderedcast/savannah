# coding=utf-8
import time
from expects import *
from lettuce import step, world

from ui_automation.environment.steps_config import driver_get
from ui_automation.helper.JS_tricks import JS_tricks
from ui_automation.helper.methods.actions import PageAction
from ui_automation.helper.methods.cards.cards import CreateCard
from ui_automation.helper.methods.common.common_methods import CommonForCards
from ui_automation.helper.methods.common.locator import CommonForCardLocator
from ui_automation.helper.methods.common.verification import VerificationMethods
from ui_automation.helper.methods.journey.simple_card import CreateJourney
from ui_automation.helper.methods.navigation import Navigation
from ui_automation.helper.methods.pathway.simple_card import CreateSimplePathway
from ui_automation.helper.methods.pathway_journey.locators import PackLocators
from ui_automation.helper.methods.wait import SupportWaitsAction


@step('Create "([^"]*)" with "([^"]*)" card')
def step_impl(step, type_content, card_type):
    card = CreateCard()
    pathway = CreateSimplePathway()
    common = CommonForCards()
    journey = CreateJourney()
    world.type_content = type_content
    common.creation_option_of_cards(type_content)
    if type_content == "SmartCard":
        card.create_smartcard(card_type)
    elif type_content == "Pathway":
        pathway.pathway_create(card_type)
    elif type_content == "Journey":
        journey.journey_create(card_type, 'self_paced')
    print(type_content + " has been created" + "\n")
    time.sleep(1)


@step("Verify that a card")
def step_impl(step):
    common_locator = CommonForCardLocator()
    action = PageAction()
    wait = SupportWaitsAction()
    pathway_locator = PackLocators()
    wait.is_visible(common_locator.card_container)
    if action.is_element_present(common_locator.card_container):
        if world.type_content != "SmartCard":
            card_label = action.actual_text(pathway_locator.label)
            actual = world.type_content.upper()
            expect(card_label).to(equal(actual))
        print("This " + world.type_content + " is present" + "\n")
    else:
        raise ValueError
    time.sleep(2)


@step('"([^"]*)" a card')
def step_impl(step, option):
    common = CommonForCards()
    verify = VerificationMethods()
    common.option_insight_dropdown_menu(option)
    verify.delete_option()


@step('Leave a "([^"]*)" on the card and verify the "([^"]*)" action')
def step_impl(step, action, types):
    """step only for like"""
    common_locator = CommonForCardLocator()
    common = CommonForCards()
    before_like = common.convert_empty_string_to_zero(common_locator.num_of_like)
    print("You have " + before_like + " like on your content!" + "\n")
    common.action_bar(action)
    time.sleep(2)
    after_like = common.convert_empty_string_to_zero(common_locator.num_of_like)
    if types == "post":
        expect(int(before_like) + 1).to(equal(int(after_like)))
    elif types == "remove":
        expect(int(before_like) - 1).to(equal(int(after_like)))
    else:
        raise ValueError
    print("After " + types + " like action, you have " + after_like + " likes" + "\n")


@step('Verify "([^"]*)" in "([^"]*)"')
def step_impl(step, stat, option):
    global common_locator
    common = CommonForCards()
    common_locator = CommonForCardLocator()
    js_tricks = JS_tricks()
    action = PageAction()
    wait = SupportWaitsAction()
    if stat == "comments_count":
        js_tricks.scroll_to_some_point(50)
        action.click(common_locator.arrow_go_back)
        wait.is_visible(common_locator.close_rate_content)
        action.click(common_locator.close_rate_content)
    else:
        pass
    common.action_bar(option)
    print("Verifying the " + stat + " in statistic")
    statistic_record = common.get_data_from_statistic(stat)
    expect(statistic_record).to(be_above(int(0)))
    action.click(common_locator.close_card_statistic)


@step('"([^"]*)" a content')
def step_impl(step, option):
    common = CommonForCards()
    verify = VerificationMethods()
    common.option_insight_dropdown_menu(option)
    verify.bookmark_action()


@step('"([^"]*)" the card')
def step_impl(step, option):
    common = CommonForCards()
    verify = VerificationMethods()
    common.option_insight_dropdown_menu(option)
    common.add_to_new_pathway()
    verify.add_to_pathway()


@step('"([^"]*)" all created data')
def step_impl(step, action):
    common = CommonForCards()
    locator = CommonForCardLocator()
    verify = VerificationMethods()
    try:
        menu = int(len(driver_get().find_elements(By.XPATH, locator.menu)))
        print(menu)
        if menu == 0:
            print("Nothing to delete" + "\n")
        elif menu >= 1:
            while menu != 0:
                common.option_insight_dropdown_menu(action)
                verify.delete_option()
                menu = int(len(driver_get().find_elements(By.XPATH, locator.insight_menu)))
    except AttributeError as e:
        raise e


@step('"([^"]*)" a card and then verify in a "([^"]*)" channel')
def step_impl(step, option, channel_name):
    verify = VerificationMethods()
    world.channel_name = channel_name
    common = CommonForCards()
    common.option_insight_dropdown_menu(option)
    common.add_to_channel(channel_name)
    verify.adding_to_channel()


@step('Verify in "([^"]*)" channel')
def step_impl(step, channel_name):
    common = CommonForCards()
    action = PageAction()
    js_tricks = JS_tricks()
    common_locator = CommonForCardLocator()
    time.sleep(2)
    js_tricks.scroll_to_some_point(50)
    if action.is_element_present(common_locator.group_name_in_channel % channel_name):
        print("Name of this channel: " + channel_name + "\n")
    else:
        print("You not able to see this group : " + channel_name + "\n")
    common.go_inside_channel(channel_name)
    js_tricks.scroll_to_some_point(400)


@step('Verify "([^"]*)" card feature')
def step_impl(step, option):
    common = CommonForCards()
    time.sleep(2)
    if option == "Promote":
        common.option_insight_dropdown_menu(option)
    elif option == "Unpromote":
        common.option_insight_dropdown_menu(option)
        driver_get().refresh()
    print(option + " content" + "\n")


@step('"([^"]*)" a piece of content')
def step_impl(step_instance, option):
    common = CommonForCards()
    common.option_insight_dropdown_menu(option)
    if option == "Assign to Me":
        common.assing_to_me()
    elif option == "Assign":
        pass
    else:
        print("This " + option + "doesn't exist!" + "\n")
        raise ValueError


@step('Verify "([^"]*)" option')
def step_impl(step_instance, option):
    navigate = Navigation()
    verify = VerificationMethods()
    navigate.between_pages("HOME")
    navigate.home_page("MY ASSIGNMENTS")
    if option == "Assign to Me":
        verify.assign_to_me()
