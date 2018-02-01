import time

from ui_automation.helper.methods.actions import PageAction
from ui_automation.helper.methods.cards.locators import SmartCardLocators
from ui_automation.helper.methods.journey.locators import JourneyLocator
from ui_automation.helper.methods.pathway.pathway import Pathway
from ui_automation.helper.methods.wait import SupportWaitsAction


class Journey(Pathway):

    def __init__(self):
        super(Journey, self).__init__()
        self.action = PageAction()
        self.wait = SupportWaitsAction()
        self.card_locator = SmartCardLocators()
        self.journey_locators = JourneyLocator()

    def type(self, arg=False, type_journey='self_paced' or 'weekly'):
        time.sleep(1)
        if arg:
            if type_journey == 'self_paced':
                self.action.mouse_hover(self.journey_locators.self_paced)
            elif type_journey == 'weekly':
                self.action.mouse_hover(self.journey_locators.weekly)
                # need to provide data
                # self.action.sendkeys_action(self.journey_locators.date_input, )
        elif not arg:
            pass
