import sys
sys.path.append("..")

from time import sleep
from .base_page import BasePage



class AboutPage(BasePage):
    def __init__(self):
        self.driver = BasePage().driver
        self.menu_about = "//android.widget.TextView[@text='About...']"
        self.show_course = "//android.widget.TextView[@text='Veja o curso aqui']"
        self.button_notification_browser = "android:id/button_once"


    def menu_about_tap(self):
        super().wait_element_to_be_clickable(None, self.menu_about)
        self.menu_about_tap = self.driver.find_element_by_xpath(self.menu_about)
        super().tap_element(self.menu_about_tap)

    def show_course_tap(self):
        super().wait_element_to_be_clickable(None, self.show_course)
        self.show_course_tap = self.driver.find_element_by_xpath(self.show_course)
        super().tap_element(self.show_course_tap)

    def screenshot_image_course(self, namefile):
        super().wait_element_to_be_clickable(None, self.show_course)
        super().take_screenshot("about", "image_course.png")

    def verify_text_in_screen(self, message):
        super().wait_element_to_be_clickable(None, self.show_course)
        return message in self.driver.page_source

    
