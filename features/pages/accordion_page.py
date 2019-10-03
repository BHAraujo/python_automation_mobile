import sys
sys.path.append("..")

from .base_page import BasePage
from helper.helpers import remove_aspas
from time import sleep

class AccordionPage(BasePage):
    def __init__(self):
        self.driver = BasePage().driver
        self.menu_accordion = "//android.widget.TextView[@text='Accordion']"

    def menu_accordion_tap(self):

        BasePage().wait_element_to_be_clickable(None, self.menu_accordion)
        self.menu_accordion_tap = self.driver.find_element_by_xpath(self.menu_accordion)
        BasePage().tap_element(self.menu_accordion_tap)

    def wait_accordion(self):
        BasePage().wait_element_to_be_clickable(None, "//android.widget.TextView[@text='Opção 1']")

    def options_tap(self, value_option):
        self.options_tap = self.driver.find_element_by_xpath(f"//android.widget.TextView[@text='Opção 1']")
        BasePage().tap_element(self.options_tap)

    def verify_text_in_screen(self, message):
        return message in self.driver.page_source

    def options_one_tap(self):
        self.options_tap = self.driver.find_element_by_xpath(f"//android.widget.TextView[@text='Opção 1']")
        BasePage().tap_element(self.options_tap)

    def options_two_tap(self):
        self.options_tap = self.driver.find_element_by_xpath(f"//android.widget.TextView[@text='Opção 2']")
        BasePage().tap_element(self.options_tap)

    def options_three_tap(self):
        self.options_tap = self.driver.find_element_by_xpath(f"//android.widget.TextView[@text='Opção 3']")
        BasePage().tap_element(self.options_tap)

    def options_four_tap(self):
        self.options_tap = self.driver.find_element_by_xpath(f"//android.widget.TextView[@text='Opção 4']")
        BasePage().tap_element(self.options_tap)

    def options_five_tap(self):
        self.options_tap = self.driver.find_element_by_xpath(f"//android.widget.TextView[@text='Opção 5']")
        BasePage().tap_element(self.options_tap)

    def options_six_tap(self):
        self.options_tap = self.driver.find_element_by_xpath(f"//android.widget.TextView[@text='Opção 6']")
        BasePage().tap_element(self.options_tap)
