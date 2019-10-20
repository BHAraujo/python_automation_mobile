import sys
sys.path.append("..")

from .base_page import BasePage


class SwipeListPage(BasePage):
    def __init__(self):
        self.driver = BasePage().driver
        self.menu_swipe_list = "//android.widget.TextView[@text='Swipe List']"
        self.button_plus = "//android.widget.TextView[@text='(+)']"
        self.button_less = "//android.widget.TextView[@text='(-)']"
        self.height = [100, 400, 600 ,800, 1000, 1200, 1300, 1500]

    def menu_swipe_list_tap(self):
        self.driver.swipe(100, 700, 100, 150)
        super().wait_element_to_be_clickable(None, self.menu_swipe_list)
        self.menu_swipe_list_tap = self.driver.find_element_by_xpath(self.menu_swipe_list)
        super().tap_element(self.menu_swipe_list_tap)

    def wait_swipe_list(self):
        super().wait_element_to_be_clickable(None, "//android.widget.TextView[@text='Opção 1']")

    def swipe_and_button_plus_tap(self):
        for index in self.height:
            self.driver.swipe(800, index, 200,0)
            super().wait_element_to_be_clickable(None, self.button_plus)
            self.button_plus_tap = self.driver.find_element_by_xpath(self.button_plus)
            super().tap_element(self.button_plus_tap)
