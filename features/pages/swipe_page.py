import sys
sys.path.append("..")

from time import sleep

from .base_page import BasePage


class SwipePage(BasePage):
    def __init__(self):
        self.driver = BasePage().driver
        self.menu_swipe = "//android.widget.TextView[@text='Swipe']"
        self.fist_screen = "//android.widget.TextView[@text='a esquerda']"
        self.second_screen = "//android.widget.TextView[@text='você consegue']"
        self.third_screen = "//android.widget.TextView[@text='Chegar até o fim!']"


    def menu_swipe_tap(self):
        super().wait_element_to_be_clickable(None, self.menu_swipe)
        self.menu_swipe_tap = self.driver.find_element_by_xpath(self.menu_swipe)
        super().tap_element(self.menu_swipe_tap)

    def wait_menu_swipe(self):
        super().wait_visibility_of_element_located(None, self.fist_screen)

    def long_click_tap(self):
        self.long_click_tap = self.driver.find_element_by_xpath(self.long_click)
        super().long_click_element(self.long_click_tap)
        super().take_screenshot("clicks", "long_click.png")

    def swipe_screen_tap(self, lista=[]):
        super().swipe_screen(lista)

    def verify_text_in_screen(self, message):
        sleep(0.5)
        super().take_screenshot("swipe", "swipe.png")
        return message in self.driver.page_source
