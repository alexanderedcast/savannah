from lettuce import step, world

from ui_automation.helper.methods.me.groups import Groups


@step("Create a new Group")
def step_impl(step_instance):
    group = Groups()
    group.create_new_group()


@step("Invite user to a group")
def step_impl(step_instance):
    """
    :type step_instance: lettuce.core.Step
    """
    pass