from expects import *
from lettuce import step
from ui_automation.helper.API_helper.api_data import nik_token
from ui_automation.helper.API_helper.skills import reset_skills
from ui_automation.helper.methods.me.interests_experise import LearningExpertise


@step('Check the number of "([^"]*)"')
def step_impl(step_instance, option):
    skill = LearningExpertise()
    inside, outside = skill.verify_number_skills(option)
    expect(inside).to(equal(outside))
    if inside >= 2:
        reset_skills(nik_token)


@step('"([^"]*)" the "([^"]*)"')
def step_impl(step_instance, action, option):
    """
    :param option: Interests or Expertise
    :param action: Add, Delete, Delete all Interests, Delete all Expertise
    :type step_instance: lettuce.core.Step
    """
    skill = LearningExpertise()
    if action == "Add":
        before_update = skill.verify_number_skills(option)
        skill.add_one(option)
        after_update = skill.verify_number_skills(option)
        expect(before_update[0]).to(be_below(after_update[0]))
        print("You " + str(action) + "ed " + str(option) + "\n")
    elif action == "Add limit":
        before_update = skill.verify_number_skills(option)
        skill.add_limit_of(option)
        after_update = skill.verify_number_skills(option)
        expect(before_update[0]).to(be_below(after_update[0]))
    elif action == "Delete":
        before_update = skill.verify_number_skills(option)
        skill.delete_one(option)
        after_update = skill.verify_number_skills(option)
        expect(before_update[0]).to(be_above(after_update[0]))
        print("You " + str(action) + "d " + str(option) + "\n")
    elif action == "Delete All":
        before_update = skill.verify_number_skills(option)
        skill.delete_all(option)
        after_update = skill.verify_number_skills(option)
        if option == "Interests":
            expect(after_update[0]).to(equal(before_update[0]))
        elif option == "Expertise":
            expect(int(after_update[0])).to(equal(0))
        print("You " + str(action) + " " + str(option) + "\n")
