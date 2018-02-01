import random

import time
from expects import *

from ui_automation.helper.API_helper.api_data import nik_token
from ui_automation.helper.API_helper.follow import followers, following
from ui_automation.helper.API_helper.users import quantity_users_in_org, sme_users, admin_in_org, leaderboard_user
from ui_automation.helper.methods.actions import PageAction
from ui_automation.helper.methods.wait import SupportWaitsAction


class TeamLocators(object):
    team_filter = "//div[@class='my-team__filter-block']//div//span[text()='%s']"
    container = "//div[@class='my-team_v2']//div[@class='custom-card-container']//div[@class='user-square-item']"
    search_field = "//div[@id='footer-wrapper']//div[@class='my-team_v2']//input[@placeholder='Search people']"
    user_name = "//div[@class='user-square-item']//a[@class][text()]"
    leaderboard_user_name = "//tr[@class='table-row']//div//div[@class='text-overflow']/a[@class][text()]"


class Team(object):

    def __init__(self):
        self.team_locator = TeamLocators()
        self.action = PageAction()
        self.wait = SupportWaitsAction()

    def verify_team_tab(self, option):
        global expected
        self.wait.is_visible(self.team_locator.team_filter % option)
        self.wait.is_clickable(self.team_locator.team_filter % option)
        self.action.click(self.team_locator.team_filter % "All Users")
        if option == "All Users":
            expected = len(quantity_users_in_org(nik_token, 100))
        elif option == "People following me":
            expected = followers(100)
        elif option == "People I am following":
            expected = len(following(100))
        elif option == "Subject Matter Experts":
            expected = len(sme_users(nik_token))
        elif option == "Admins":
            expected = admin_in_org(nik_token, 100)
        self.action.click(self.team_locator.team_filter % option)
        actual = len(self.action.find_element("elements", self.team_locator.container))
        expect(expected).to(equal(actual))
        print(option + " shown correctly. " + "There're " + str(expected) + " under " + option + "\n")

    def search_result(self):
        users = quantity_users_in_org(nik_token, 100)
        users_to_search = random.choice(users)
        self.wait.is_visible(self.team_locator.search_field)
        self.action.send_keys(self.team_locator.search_field, users_to_search)
        self.action.press_enter()
        time.sleep(1)
        expect(len(self.action.find_element("elements", self.team_locator.container))).to(equal(1))
        expect(self.action.actual_text(self.team_locator.user_name)).to(equal(users_to_search))
        print("Search works correct. User: " + users_to_search + " has been found" + "\n")

    def leaderboard_users(self, token):
        expected_users = leaderboard_user(token)
        users_on_page = self.action.find_element("elements", self.team_locator.leaderboard_user_name)
        actual_leaderboard_users = []
        for user in users_on_page:
            actual_leaderboard_users.append(user.text)
        expect(expected_users).to(equal(actual_leaderboard_users))
        print("Leaderboard users shown correctly" + "\n")
