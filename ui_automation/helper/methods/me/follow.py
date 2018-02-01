import random

from expects import *

from ui_automation.helper.API_helper.api_data import nik_token
from ui_automation.helper.API_helper.follow import following
from ui_automation.helper.API_helper.users import recommended_users, quantity_users_in_org, leaderboard_user
from ui_automation.helper.JS_tricks import JS_tricks
from ui_automation.helper.methods.actions import PageAction
from ui_automation.helper.methods.search import Search
from ui_automation.helper.methods.wait import SupportWaitsAction


class Locator(object):
    """
    Following and Followers
    """
    follow = "//div[@class='user-follow-data']/span//span[text()='%s']/../strong[@class]"
    button_follow = "//div[@class='user-follow-data']/span//span[text()='%s']"
    show_following_list = "//div[@class='data-users']"
    name_follower = "//div[@class='data-users']//div[@class='data-name'][text()]"
    close_following_list = "//span[@class='close close-icon-btn']"
    follow_by_name = "//div[@class='influencer']//div[@class='influencer-name'][text()='%s']/../../../button//span[text()='Follow']"
    unfollow_by_name = "//div[@class='influencer']//div[@class='influencer-name'][text()='%s']/../../../button//span[text()='Following']"
    profile_containe = "//div[@class='influencer-wrapper']//div[contains(@class, 'influencer-info')]//div[text()='%s']"
    user_info_container = "//div[@class='container-padding user-info']"
    follow_on_profile_page = "//div[@class='small-3 right']//button"
    profile_name = "//div[@class='user-info-list']//div/b[text()]"
    team_follow_button = "//div[contains(@class, 'user-square')]//div[contains(@class, 'name')]//a[text()='%s']/../..//div[@class='btn-block']//button//span[text()='Follow']"
    team_unfollow_button = "//div[contains(@class, 'user-square')]//div[contains(@class, 'name')]//a[text()='%s']/../..//div[@class='btn-block']//button//span[text()='Following']"
    leardboard_follow = "//div[@class='vertical-spacing-large']//tbody//td[@class]//a[text()='%s']/../../../../..//button//span[text()='Follow']"
    leardboard_unfollow = "//div[@class='vertical-spacing-large']//tbody//td[@class]//a[text()='%s']/../../../../..//button//span[text()='Following']"


class Follow(object):
    def __init__(self):
        self.action = PageAction()
        self.wait = SupportWaitsAction()
        self.follow_locator = Locator()
        self.search = Search()
        self.js_tricks = JS_tricks()

    def check_number_follow_me(self, option):
        self.wait.is_visible(self.follow_locator.follow % option)
        number_follow = self.action.actual_text(self.follow_locator.follow % option)
        try:
            if int(number_follow) == 0:
                try:
                    self.wait.is_visible(self.follow_locator.button_follow % option)
                    self.action.click(self.follow_locator.button_follow % option)
                    if not self.action.is_element_present(self.follow_locator.show_following_list):
                        pass
                except AttributeError as e:
                    raise e
                return int(number_follow)
            elif int(number_follow) > 0:
                list_users = []
                self.wait.is_visible(self.follow_locator.button_follow % option)
                self.action.click(self.follow_locator.button_follow % option)
                self.wait.is_visible(self.follow_locator.show_following_list)
                users = self.action.find_element("elements", self.follow_locator.name_follower)
                for user in users:
                    list_users.append(user.text)
                expect(int(number_follow)).to(equal(len(list_users)))
                self.action.click(self.follow_locator.close_following_list)
                return list_users
        except AttributeError as e:
            raise e

    def get_another_user(self, user_to_follow, users, users_following):
        while user_to_follow in users_following:
            print("You already follow this user: " + user_to_follow + "\n")
            user_to_follow = random.choice(users)
        return user_to_follow

    def return_list_needed_users(self, token, option):
        global users
        # return users thru API
        if option == "Discover: People carousel" and "Discover: Profile page":
            users = recommended_users(token, 100)
        elif option == "Search" and "Team":
            users = quantity_users_in_org(token, 100)
        elif option == "Leader board":
            users = leaderboard_user(token)
        return users

    def follow_users(self, token, option):
        users = self.return_list_needed_users(token, option)
        # randomly pick a user from list recommended users
        user_to_follow = random.choice(users)
        # return list of following users thru API
        users_following = following(100)
        # check if this user already following
        if user_to_follow in users_following:
            user_to_follow = self.get_another_user(user_to_follow, users, users_following)
        if option == "Discover: People carousel":
            self.action.click(self.follow_locator.follow_by_name % user_to_follow)
        elif option == "Discover: Profile page":
            self.wait.is_visible(self.follow_locator.profile_containe % user_to_follow)
            self.action.click(self.follow_locator.profile_containe % user_to_follow)
            self.wait.is_visible(self.follow_locator.user_info_container)
            expect(user_to_follow).to(equal(self.action.actual_text(self.follow_locator.profile_name)))
            # wait until button is shown  # start to follow
            self.action.click(self.follow_locator.follow_on_profile_page)
        elif option == "Search":
            self.search.search_filter(user_to_follow, "People")
            self.wait.is_visible(self.follow_locator.follow_by_name % user_to_follow)
            self.action.click(self.follow_locator.follow_by_name % user_to_follow)
        elif option == "Team":
            self.js_tricks.scroll_to_some_point(500)
            self.wait.is_visible(self.follow_locator.team_follow_button % user_to_follow)
            self.action.click(self.follow_locator.team_follow_button % user_to_follow)
        elif option == "Leader board":
            try:
                if user_to_follow == "Nik Omel":
                    rest_users = len(users) - len(users_following)
                    print(rest_users)
                    if rest_users > 1:
                        self.get_another_user(user_to_follow, users, users_following)
                        self.js_tricks.scroll_to_some_point(500)
                        self.wait.is_visible(self.follow_locator.leardboard_follow % user_to_follow)
                        self.action.click(self.follow_locator.leardboard_follow % user_to_follow)
                    elif rest_users == 1:
                        print("You cannot follow yourself" + "\n")
                else:
                    self.js_tricks.scroll_to_some_point(500)
                    self.wait.is_visible(self.follow_locator.leardboard_follow % user_to_follow)
                    self.action.click(self.follow_locator.leardboard_follow % user_to_follow)
                print("You started to follow " + user_to_follow + "\n")
                return user_to_follow
            except AttributeError as e:
                raise e
        return user_to_follow

    def unfollow_users(self, option):
        users = following(100)
        user_to_unfollow = random.choice(users)
        if option == "Discover: People carousel":
            self.action.click(self.follow_locator.unfollow_by_name % user_to_unfollow)
        elif option == "Discover: Profile page":
            self.wait.is_visible(self.follow_locator.profile_containe % user_to_unfollow)
            self.action.click(self.follow_locator.profile_containe % user_to_unfollow)
            self.wait.is_visible(self.follow_locator.user_info_container)
            expect(user_to_unfollow).to(equal(self.action.actual_text(self.follow_locator.profile_name)))
            self.action.click(self.follow_locator.follow_on_profile_page)
        elif option == "Search":
            self.search.search_filter(user_to_unfollow, "People")
            self.action.click(self.follow_locator.unfollow_by_name % user_to_unfollow)
        elif option == "Team":
            self.js_tricks.scroll_to_some_point(500)
            self.action.click(self.follow_locator.team_unfollow_button % user_to_unfollow)
        elif option == "Leader board":
            leardearbord_users = leaderboard_user(nik_token)  # hardcoded API token
            user_to_unfollow = random.choice(list(set(users) & set(leardearbord_users)))
            self.js_tricks.scroll_to_some_point(500)
            self.action.click(self.follow_locator.leardboard_unfollow % user_to_unfollow)
        print(user_to_unfollow + " has been unfollowed" + "\n")
        return user_to_unfollow
