import sys
sys.path.append("..")

from .base_page import BasePage


class ClicksPage(BasePage):
    def __init__(self):
        self.driver = BasePage().driver
        self.menu_clicks = "//android.widget.TextView[@text='Cliques']"
        self.long_click = "//android.widget.TextView[@text='Clique Longo']"
        self.double_click = "//android.widget.TextView[@text='Clique duplo']"
        self.lazy_double_click = "//android.widget.TextView[@text='Clique duplo lento']"
        self.btn_clear = "//android.widget.TextView[@text='Limpar']"

    def menu_clicks_tap(self):
        super().wait_element_to_be_clickable(None, self.menu_clicks)
        self.menu_clicks_tap = self.driver.find_element_by_xpath(self.menu_clicks)
        super().tap_element(self.menu_clicks_tap)

    def wait_menu_click(self):
        super().wait_element_to_be_clickable(None, self.long_click)

    def long_click_tap(self):
        self.long_click_tap = self.driver.find_element_by_xpath(self.long_click)
        super().long_click_element(self.long_click_tap)
        super().take_screenshot("clicks", "long_click.png")

    def double_click_tap(self):
        self.double_click_tap = self.driver.find_element_by_xpath(self.double_click)
        super().double_click_element(self.double_click_tap)
        super().take_screenshot("clicks", "double_click.png")

    def lazy_double_click_tap(self):
        self.lazy_double_click_tap = self.driver.find_element_by_xpath(self.lazy_double_click)
        super().lazy_double_click_tap(self.lazy_double_click_tap)
        super().take_screenshot("clicks", "lazy_double_click.png")

    def btn_clear_tap(self):
        self.btn_clear_tap = self.driver.find_element_by_xpath(self.btn_clear)
        super().tap_element(self.btn_clear_tap)
