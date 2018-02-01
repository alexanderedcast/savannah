from lettuce import step

from ui_automation.helper.API_helper.api_data import nik_token
from ui_automation.helper.methods.me.content import Content
from ui_automation.helper.methods.me.team import Team


@step('Verify that "([^"]*)" cards shown')
def step_impl(step_instance, option):
    content = Content()
    content.verify_content(option)


@step("Create all type of content")
def step_impl(step_instance):
    content = Content()
    content.create_all_cards()

@step('Verify users under "([^"]*)" tab')
def step_impl(step_instance, option):
    team = Team()
    team.verify_team_tab(option)

@step("Verify Search under Me Team")
def step_impl(step_instance):
    team = Team()
    team.search_result()


@step("Verify that user under Leaderboard shown correctly")
def step_impl(step_instance):
    team = Team()
    team.leaderboard_users(nik_token)