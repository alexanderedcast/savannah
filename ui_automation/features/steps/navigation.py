from lettuce import step

from ui_automation.helper.JS_tricks import JS_tricks
from ui_automation.helper.methods.navigation import Navigation

navigation = Navigation()


@step('Navigate to "([^"]*)" page "([^"]*)" tab')
def step_impl(step, category, subcategory):
    navigation.between_pages(category)
    js_tricks = JS_tricks()
    if category == "ME":
        navigation.me_page(subcategory)
    else:
        js_tricks.scroll_to_some_point(50)
        navigation.home_page(subcategory)
    print("Navigate to "+category + " " + subcategory + "\n")


@step('Navigating to "([^"]*)" page')
def step_impl(step, category):
    navigation.between_pages(category)