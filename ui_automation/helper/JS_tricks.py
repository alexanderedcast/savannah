from lettuce import step



###
# JS tricks most likely will fail on IE
###
from ui_automation.environment.steps_config import driver_get


class JS_tricks(object):

    def mouse_over_element(self, element):
        """
        JS implementation of mouse over element event
        """
        java_script = "var evObj = document.createEvent('MouseEvents');\n" \
                      "evObj.initMouseEvent(\"mouseover\",true, false, window," \
                      " 0, 0, 0, 0, 0, false, false, false, false, 0, null);\n" \
                      "arguments[0].dispatchEvent(evObj);"
        driver_get().execute_script(java_script, element)

    def mouse_click_element(self, element):
        """
        JS implementation of mouse click event
        """
        java_script = "var evObj = document.createEvent('MouseEvents');\n" \
                      "evObj.initMouseEvent(\"click\",true, true, window," \
                      " 0, 0, 0, 80, 20, false, false, false, false, 0, null);\n" \
                      "arguments[0].dispatchEvent(evObj);"
        driver_get().execute_script(java_script, element)

    def scroll_into_view(self, element):
        driver_get().execute_script("return arguments[0].scrollIntoView();", element)

    def element_to_the_middle(self, element):
        """
        adjust screen position to show the element in the middle
        """
        current_screen_height = driver_get().get_window_size()['height']
        element_y_axis_position = element.location['y']
        pxs = int(element_y_axis_position - current_screen_height / 2)

        driver_get().execute_script('document.body.scrollTop = document.documentElement.scrollTop = 0;')
        driver_get().execute_script("scroll(0, %s)" % pxs)

    def hide_element(self, element):
        driver_get().execute_script("arguments[0].style.display='none'", element)

    def inner_scroll_to_element(self, element, inside_element=None):
        """
        scroll within container
        """
        driver_get().execute_script("arguments[0].scrollTop = arguments[1];", element, inside_element)

    def scroll_to_some_point(self, pixels):
        return driver_get().execute_script("window.scrollTo(0, %s)" % pixels)

    def zoom_out_cheat(self, zoom_lvl):
        """
        Zooming helps to avoid overlapping on small resolution screens.
        This is pure selenium cheat. Will not work with IE
        """
        zoom = float(zoom_lvl) / 100
        driver_get().execute_script("document.body.style.transform = 'scale(%s)'" % str(zoom))

    def forced_scroll(self, power):
        driver_get().execute_script("scroll(0, %s)" % power)

    def scroll_top(self):
        driver_get().execute_script('document.body.scrollTop = document.documentElement.scrollTop = 0;')

    def hide_footer(self):
        driver_get().execute_script("document.getElementById('footer').style.display='none'")

    def hide_header(self):
        header = driver_get().find_element_by_xpath("//nav[contains(@class, 'navbar-fixed-top')]")
        driver_get().execute_script("arguments[0].style.display='none'", header)

    def show_header(self):
        header = driver_get().find_element_by_xpath("//nav[contains(@class, 'navbar-fixed-top')]")
        driver_get().execute_script("arguments[0].style.display='block'", header)

    def send_keys(self, value, element):
        script = "return arguments[0].target = '%s'" % value
        driver_get().execute_script(script, element)
