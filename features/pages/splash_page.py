import sys
sys.path.append("..")

from .base_page import BasePage


class SplashPage(BasePage):
    def __init__(self):
        self.driver = BasePage().driver
        self.menu_splash = "//android.widget.TextView[@text='Splash']"
        self.message_splash =  "//android.widget.TextView[@text='Splash!']"


    def menu_splash_tap(self):
        BasePage().wait_element_to_be_clickable(None, self.menu_splash)
        self.menu_splash_tap = self.driver.find_element_by_xpath(self.menu_splash)
        BasePage().tap_element(self.menu_splash_tap)

    def message_splash_text(self):
        BasePage().wait_element_to_be_clickable(None, self.message_splash)
        self.message_splash_text = self.driver.find_element_by_xpath(self.message_splash)
        BasePage().tap_element(self.message_splash_text)

    def wait_message_splash(self):
        BasePage().wait_element_to_be_clickable(None, self.message_splash)
