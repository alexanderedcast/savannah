import random

from expects import *
from lettuce import step, world
from ui_automation.helper.API_helper.api_data import nik_token
from ui_automation.helper.methods.me.follow import Follow


@step('Check the number "([^"]*)" users')
def step_impl(step_instance, option):
    global length_follow_users
    follow = Follow()
    users_following = follow.check_number_follow_me(option)
    if users_following > 0:
        length_follow_users = len(users_following)
    elif users_following == 0:
        print("You don't follow any user from org" + "\n")
        length_follow_users = 0


@step('"([^"]*)" user from "([^"]*)"')
def step_impl(step_instance, option, place):
    global user
    follow = Follow()
    if option == "Follow":
        user = follow.follow_users(nik_token, place)
    elif option == "Unfollow":
        user = follow.unfollow_users(place)
    return user


@step('Verify "([^"]*)" action')
def step_impl(step_instance, option):
    global after_action_number_users
    follow = Follow()
    after_action_list_follow_users = follow.check_number_follow_me("Following")
    if after_action_list_follow_users > 0:
        after_action_number_users = len(after_action_list_follow_users)
    elif after_action_list_follow_users == 0:
        after_action_number_users = 0
    if option == "Follow":
        expect(after_action_list_follow_users).to(contain(user))
        expect(length_follow_users + 1).to(equal(after_action_number_users))
    elif option == "Unfollow":
        expect(length_follow_users - 1).to(equal(after_action_number_users))
        if after_action_list_follow_users > 0:
            expect(after_action_list_follow_users).to_not(contain(user))

