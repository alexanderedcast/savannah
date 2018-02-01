import time
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

from ui_automation.environment.steps_config import driver_get


class PageAction(object):

    def find_element(self,  option, locator, by=By.XPATH):
        global element
        if option == "element":
            element = driver_get().find_element(by, locator)
        elif option == "elements":
            element = driver_get().find_elements(by, locator)
        return element

    def send_keys(self, locator, value):
        input_text = driver_get().find_element(By.XPATH, locator).send_keys(value)
        return input_text

    def action_sendkeys(self, locator, value):
        actions = ActionChains(driver_get())
        element = By.XPATH, locator
        action = actions.move_to_element(element).send_keys(value).perform()
        return action

    def sendkeys_action(self, locator, value):
        element = driver_get().find_element(By.XPATH, locator)
        actions = ActionChains(driver_get())
        actions.move_to_element(element)
        actions.send_keys_to_element(element, value)
        actions.perform()

    def slow_send_keys(self, locator, value):
        el = driver_get().find_element(By.XPATH, value=locator)
        text = value
        for character in text:
            el.send_keys(character)
            time.sleep(0.1)

    def click(self, locator):
        try:
            element = driver_get().find_element(By.XPATH, value=locator)
            if element.is_displayed():
                element.click()
            else:
                print("cannot click on this locator")
        except AttributeError as e:
            print(e)
            raise e

    def double_click(self, locator):
        element = driver_get().find_element(By.XPATH, value=locator)
        actionChains = ActionChains(driver_get())
        double = actionChains.double_click(element).perform()
        return double

    def click_action(self, locator):
        some = driver_get().find_element(By.XPATH, value=locator)
        actions = ActionChains(driver_get())
        actions.move_to_element(some)
        actions.click(some)
        actions.perform()

    def mouse_hover(self, locator):
        radio_button = driver_get().find_element(By.XPATH, value=locator)
        actions = ActionChains(driver_get())
        actions.move_to_element(radio_button)
        actions.click(radio_button)
        actions.perform()

    def check_exists_by(self, locator):
        try:
            driver_get().find_element(By.XPATH, value=locator)
        except NoSuchElementException:
            return False
        print("Element is present" + "\n")
        return True

    def actual_text(self, locator):
        return driver_get().find_element(By.XPATH, value=locator).text

    def press_enter(self):
        return ActionChains(driver_get()).send_keys(Keys.ARROW_DOWN).send_keys(Keys.ENTER).perform()

    def is_element_present(self, locator):
        try:
            driver_get().find_element(By.XPATH, value=locator)
        except NoSuchElementException:
            return False
        return True

    def clear(self, locator):
        return driver_get().find_element(By.XPATH, locator).clear()

    def length(self, locator):
        elements = driver_get().find_elements(By.XPATH, locator)
        length = len(elements)
        return length


