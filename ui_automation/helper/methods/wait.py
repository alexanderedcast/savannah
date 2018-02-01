import time
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from ui_automation.environment.steps_config import driver_get


class SupportWaitsAction(object):

    def wait_for_element_visibility(self, locator, time=40):
        WebDriverWait(driver_get(), time).until(lambda driver: driver.find_element(By.XPATH, locator).is_displayed)

    def is_clickable(self, locator):
        wait_element = WebDriverWait(driver_get(), 100).until(EC.element_to_be_clickable((By.XPATH, locator)))
        return wait_element

    def wait_until(self, locator, timeout=100):
        wait = WebDriverWait(driver_get(), timeout)
        element = wait.until(EC.element_to_be_clickable((By.XPATH, locator)))
        return element

    def is_visible(self, locator):
        return WebDriverWait(driver_get(), 100).until(EC.visibility_of_element_located((By.XPATH, locator)))

    def wait_for_page_to_load(self, timeout=10000):
        w = WebDriverWait(driver_get(), timeout / 1000.0)
        w.until(lambda driver: driver.execute_script("return document.readyState") == "complete")


    def wait_for_elem(self, xpath, timeout=100):
        start = time.time()
        elems = []
        while time.time() - start < timeout:
            elems = driver_get().find_elements_by_xpath(str(xpath))
            if elems:
                return elems
            time.sleep(0.2)
        return elems

    def isElementPresent(self, xpath):
        waitForPresence = WebDriverWait(driver_get(), 120)
        try:
            waitForPresence.until(EC.presence_of_element_located((By.XPATH, xpath)))
        except TimeoutException:
            print('The element appears')
        try:
            waitForPresence.until(EC.invisibility_of_element_located((By.XPATH, xpath)))
        except TimeoutException:
            print('The element does not disappear')
