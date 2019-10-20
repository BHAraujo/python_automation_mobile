import sys
sys.path.append("..")

from time import sleep

from .base_page import BasePage


class OptionPage(BasePage):
    def __init__(self):
        self.driver = BasePage().driver
        self.menu_option = "//android.widget.TextView[@text='Opção bem escondida']"

    def menu_option_tap(self):
        sleep(3)
        self.driver.swipe(100, 700, 100, 150)
        super().wait_element_to_be_clickable(None, self.menu_option)
        self.menu_option_tap = self.driver.find_element_by_xpath(self.menu_option)
        super().tap_element(self.menu_option_tap)
