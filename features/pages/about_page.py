import sys
sys.path.append("..")

from time import sleep
from .base_page import BasePage


class AboutPage(BasePage):
    def __init__(self):
        self.driver = driver
        self.menu_about = "//android.widget.TextView[@text='About...']"
        self.show_course = "//android.widget.TextView[@text='Veja o curso aqui']"
        self.button_notification_browser = "android:id/button_once"


    def menu_about_tap(self):
        super().wait_element_to_be_clickable(None, self.menu_about)
        self.menu_about_tap = self.driver.find_element_by_xpath(self.menu_about)
        super().tap_element(self.menu_about_tap)

    def show_course_tap(self):
        BasePage().wait_element_to_be_clickable(None, self.show_course)
        self.show_course_tap = self.driver.find_element_by_xpath(self.show_course)
        BasePage().tap_element(self.show_course_tap)

    def screenshot_image_course(self, namefile):
        BasePage().wait_element_to_be_clickable(None, self.show_course)
        BasePage().take_screenshot("about", "image_course.png")

    def verify_text_in_screen(self, message):
        BasePage().wait_element_to_be_clickable(None, self.show_course)
        return message in self.driver.page_source

    def button_notification_browser_tap(self):
        BasePage().wait_element_to_be_clickable("ID", self.button_notification_browser)
        self.button_notification_browser_tap = self.driver.find_element_by_id(self.button_notification_browser)
        BasePage().tap_element(self.button_notification_browser_tap)
        sleep(10)
        BasePage().take_screenshot("about", "chrome.png")
        return self.driver.current_activity




#
# alert = driver.find_element_by_id("android:id/button_once")
# alert.click()
# sleep(10)
#
# print(driver.current_activity)
#
