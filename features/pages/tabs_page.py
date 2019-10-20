import sys
sys.path.append("..")

from .base_page import BasePage


class TabsPage(BasePage):
    def __init__(self):
        self.driver = BasePage().driver
        self.menu_tabs = "//android.widget.TextView[@text='Abas']"
        self.tab_first = "//android.widget.TextView[@text='ABA 1']"
        self.tab_second = "//android.widget.TextView[@text='ABA 2']"
        self.message_tab_second = "//android.widget.TextView[@text='Este é o conteúdo da Aba 2']"

    def menu_tabs_tap(self):
        super().wait_element_to_be_clickable(None, self.menu_tabs)
        self.menu_tabs_tap = self.driver.find_element_by_xpath(self.menu_tabs)
        super().tap_element(self.menu_tabs_tap)

    def wait_tabs(self):
        super().wait_element_to_be_clickable(None, self.tab_first)
        super().wait_element_to_be_clickable(None, self.tab_second)

    def tab_second_tap(self):
        super().wait_element_to_be_clickable(None, self.tab_second)
        self.tab_second_tap = self.driver.find_element_by_xpath(self.tab_second)
        super().tap_element(self.tab_second_tap)
        super().wait_visibility_of_element_located(None, self.message_tab_second)
