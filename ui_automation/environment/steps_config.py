# coding=utf-8
import os
import sys
import time
import datetime
from lettuce import before, world, after
from selenium import webdriver
from selenium.webdriver import DesiredCapabilities
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait

from ui_automation.test_data.read_json import read_config_file

chromedriver_path = "/usr/local/bin/chromedriver"
world.config = read_config_file()


def driver_get():
    """
    webdriver wrapper
    """
    return driver


def close_all_alerts():
    try:
        alert = driver_get().switch_to.alert
        alert.accept()
        time.sleep(2)
        close_all_alerts()
    except:
        return


def browser_local_run(browser_name):
    global driver
    if browser_name == "chrome":
        chrome_options = webdriver.ChromeOptions()
        chrome_options.add_argument('--no-sandbox')
        driver = webdriver.Chrome(executable_path=chromedriver_path, chrome_options=chrome_options)
        driver.set_window_size(1920, 1080)
        driver.maximize_window()
    elif browser_name == "firefox":
        # for Fifefox browser
        caps = DesiredCapabilities.FIREFOX
        caps["marionette"] = True
        caps["binary"] = "/Applications/Firefox.app/Contents/MacOS/firefox-bin"
        geckodriver = "/Library/Frameworks/Python.framework/Versions/2.7/bin/geckodriver"
        driver = webdriver.Firefox(capabilities=caps, executable_path=geckodriver)
    elif browser_name == "safari":
        # You need to activate the Automation in Dev Tools
        driver = webdriver.Safari()
    elif browser_name == "phantom":
        driver = webdriver.PhantomJS()
    return driver


@before.all
def env_set_up():
    print(sys.version)
    if 'JENKINS' in os.environ:
        world.url = os.environ['URL']
        print('JENKINS RUN \n')
    else:
        print('LOCAL RUN \n')


@before.each_scenario
def startup(scenario):
    global driver
    global start
    start = datetime.datetime.now()
    for i in ["\n", "[ " + scenario.name + " ] has began", "\n"]:
        print(i)
    if 'JENKINS' in os.environ:
        from pyvirtualdisplay import Display
        global display
        display = Display(visible=0, size=(1920, 1080))
        display.start()
        driver = webdriver.Chrome(executable_path=chromedriver_path)
        driver.set_window_size(1920, 1080)
        # driver.set_window_size(1366, 768)
    else:
        browser_local_run(world.config['env']['browser'])
    driver.implicitly_wait(30)
    driver.set_page_load_timeout(120)
    driver.set_script_timeout(120)
    driver.get(world.config['env']['url'])


@before.each_step
def no_redux_mask(step):
    driver.implicitly_wait(4)
    if not EC.alert_is_present():
        time.sleep(5)
        if driver_get().find_element_by_xpath('//div[@data-reactroot]'):
            WebDriverWait(driver, 30).until(
                EC.invisibility_of_element_located((By.XPATH, '//div[@data-reactroot]')))


@after.each_step
def step_name(step):
    if step.failed:
        world.failedStepName = step.sentence
        for entry in driver.get_log('browser'):
            print(entry)
    elif not EC.alert_is_present:
        if driver_get().find_element_by_xpath('//div[@data-reactroot]'):
            try:
                WebDriverWait(driver, 50).until(
                    EC.invisibility_of_element_located((By.XPATH, '//div[@data-reactroot]')))
            except Exception as e:
                print(e)


@after.each_scenario
def save_quit(scenario):
    stop = datetime.datetime.now()
    try:
        if scenario.failed:
            filename = "[ " + scenario.name + " ]" + " - " + world.failedStepName.replace("\"",
                                                                                          "") + " - " + time.strftime(
                "%d-%m-%Y %I-%M %p") + ".png"
            path = os.path.abspath("Failed_scenarios")
            if not os.path.exists(path):
                os.makedirs(path)
            fullpath = os.path.join(path, filename)
            print("\n" + "[-] FAILED " + scenario.name)
            number_of_files = len([item for item in os.listdir(path) if os.path.isfile(os.path.join(path, item))])
            driver_get().save_screenshot(fullpath)
            if not len([item for item in os.listdir(path) if
                        os.path.isfile(os.path.join(path, item))]) == number_of_files + 1:
                print ('Screenshot has not been saved')
            else:
                print("Screenshot with a failure has been saved" + "\n")
        else:
            print("[+] PASSED\n")
            print('Finished in    ', (stop - start).total_seconds())
    finally:
        driver.delete_all_cookies()
        # driver.quit()
        if 'JENKINS' in os.environ:
            driver.close()
            driver.quit()
            display.stop()
