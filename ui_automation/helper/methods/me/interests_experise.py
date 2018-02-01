import time

from lettuce import world
from ui_automation.helper.methods.actions import PageAction
from ui_automation.helper.methods.wait import SupportWaitsAction


class Locator(object):
    """
    Just add Interests of Expertise
    """
    button_edit = "//div[@id='profile-wrapper']//div[@class='interests-section']//div[@class]//span[text()='%s']/..//button[@class]"
    text_of_skills = "//div[@class='row']//div[@style]//span/small"
    input_skill = "//div[@data-reactroot]//div[@class='row']//input[@type]"
    number_skills = "//div[@class='interests-section']//div[@class='row']//span[text()='%s']/../../..//div[@style]//div"
    update_number = "//button[@class='float-right create']"
    close = "//button[@class='float-right close']"
    name_of_last_skill = "(//div[@class='small-12 columns text-center']//span/small)[last()]"
    delete_skill_by_name = "//div[@class='small-12 columns text-center']//span/small[text()='%s']/..//button[@class='cancel-icon delete']//*[@viewBox]"
    delete_last_skill = "//div[@class='small-12 columns text-center']//span/small[text()]/..//button[@class='cancel-icon delete']//*[@viewBox]"
    message_about_skills = "//div[@class='flash-alert']//p//span"


class LearningExpertise(object):
    def __init__(self):
        self.action = PageAction()
        self.wait = SupportWaitsAction()
        self.skills_locator = Locator()

    def quantity_skill_inside(self, skill):
        global list
        try:
            list = []
            time.sleep(5)
            self.wait.is_clickable(self.skills_locator.button_edit % skill)
            self.wait.is_visible(self.skills_locator.button_edit % skill)
            self.action.click(self.skills_locator.button_edit % skill)
            skills = self.action.find_element('elements', self.skills_locator.text_of_skills)
            for one_skill in skills:
                list.append(one_skill)
            world.text_last_skill = self.action.actual_text(self.skills_locator.name_of_last_skill)
        except AttributeError:
            print("No skills")
        finally:
            self.action.click(self.skills_locator.update_number)
            need_one_topic = self.action.is_element_present(self.skills_locator.message_about_skills)
            if need_one_topic:
                print(self.action.actual_text(self.skills_locator.message_about_skills))
                self.action.click(self.skills_locator.close)
            elif not need_one_topic:
                return len(list)

    def quantity_skill_outside(self, skill):
        """
        :param skill: Interests or Expertise
        :return: number of interest
        """
        list = []

        skills = self.action.find_element('elements', self.skills_locator.number_skills % skill)
        for one_skill in skills:
            list.append(one_skill)
        if skill == "Expertise":
            if len(list) == 0:
                pass
        return len(list)

    def add_one(self, skill):
        time.sleep(1)
        self.wait.is_clickable(self.skills_locator.button_edit % skill)
        self.action.click(self.skills_locator.button_edit % skill)
        import random
        skill = random.choice("ABCDEFGHIJKL"
                              "MNOPQRSTUVWXYZ")
        time.sleep(1)
        self.wait.is_visible(self.skills_locator.input_skill)
        self.action.double_click(self.skills_locator.input_skill)
        self.action.send_keys(self.skills_locator.input_skill, skill)
        time.sleep(2)
        self.action.press_enter()
        time.sleep(1)
        added_skill = self.action.is_element_present(self.skills_locator.text_of_skills)
        if not added_skill and len(self.action.find_element("elements", self.skills_locator.text_of_skills)) == 0:
            raise ValueError
        self.action.click(self.skills_locator.update_number)

    def add_limit_of(self, skill):
        self.wait.is_clickable(self.skills_locator.button_edit % skill)
        self.action.click(self.skills_locator.button_edit % skill)
        while True:
            if self.action.find_element("elements", self.skills_locator.message_about_skills):
                if self.action.actual_text(self.skills_locator.message_about_skills) == "The topic is already added!":
                    pass
                else:
                    break
            import random
            skill = random.choice("ABCDEFGHIJKL"
                                  "MNOPQRSTUVWXYZ")
            self.action.send_keys(self.skills_locator.input_skill, skill)
            time.sleep(2)
            self.action.press_enter()
            time.sleep(1)
        self.action.click(self.skills_locator.update_number)

    def delete_all(self, skill):
        time.sleep(1)
        self.wait.is_clickable(self.skills_locator.button_edit % skill)
        self.action.click(self.skills_locator.button_edit % skill)
        for _ in range(len(self.action.find_element("elements", self.skills_locator.text_of_skills))):
            self.action.click(self.skills_locator.delete_last_skill)
            time.sleep(1)
        self.action.click(self.skills_locator.update_number)
        #self.wait.is_visible(self.skills_locator.message_about_skills)
        if self.action.find_element("elements", self.skills_locator.message_about_skills):
            if self.action.actual_text(self.skills_locator.message_about_skills) == "The topic is already added!":
                pass
            elif self.action.actual_text(
                    self.skills_locator.message_about_skills) == "You should have atleast 1 topic selected.":
                self.action.click(self.skills_locator.close)
                print("You cannot delete all " + skill + "\n")

    def delete_one(self, skill):
        time.sleep(1)
        self.wait.is_clickable(self.skills_locator.button_edit % skill)
        self.action.click(self.skills_locator.button_edit % skill)
        self.action.click(self.skills_locator.delete_skill_by_name % world.text_last_skill)
        time.sleep(1)
        self.action.click(self.skills_locator.update_number)

    def verify_number_skills(self, skill):
        time.sleep(1)
        outside = self.quantity_skill_outside(skill)
        inside = self.quantity_skill_inside(skill)
        print("Number of your " + str(skill) + " is : " + str(outside) + "\n")
        if inside == 3:
            print("You cannot add more " + skill + "\n")
        elif inside <= 2:
            possible_number = int(3) - int(inside)
            print("You can add " + str(possible_number) + " more " + skill + "\n")
        elif inside > 3:
            raise ValueError
        return inside, outside
