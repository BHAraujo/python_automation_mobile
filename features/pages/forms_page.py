import sys
sys.path.append("..")

from time import sleep

from .base_page import BasePage
from helper.helpers import remove_aspas


class FormsPage(BasePage):
    def __init__(self):
        self.driver = BasePage().driver
        self.menu_forms = "//android.widget.TextView[@text='Formulário']"
        self.field_name = "//android.widget.EditText[@text='Nome']"
        self.console = "android:id/text1"
        self.check_date = "check"
        self.switch_time = "switch"
        self.save_lazy = "//android.widget.TextView[@text='SALVAR DEMORADO']"
        self.button_clear = "//android.widget.TextView[@text='LIMPAR']"


    def menu_forms_tap(self):
        super().wait_element_to_be_clickable(None, self.menu_forms)
        self.menu_forms_tap = self.driver.find_element_by_xpath(self.menu_forms)
        super().tap_element(self.menu_forms_tap)

    def get_title_forms(self, title):
        super().wait_visibility_of_element_located(None, self.field_name)
        return title in self.driver.page_source

    def name_field_fill(self, name):
        super().wait_visibility_of_element_located(None, self.field_name)
        self.field_name_field_fill = self.driver.find_element_by_xpath(self.field_name)
        super().fill_field(self.field_name_field_fill, remove_aspas(name))

    def console_select(self, name_console):
        self.console_select = self.driver.find_element_by_id(self.console)
        super().tap_element(self.console_select)
        super().wait_element_to_be_clickable(None, f"//android.widget.CheckedTextView[@text='PS4']")
        op_console = self.driver.find_element_by_xpath("//android.widget.CheckedTextView[@text='PS4']")
        super().tap_element(op_console)

    def check_date_tap(self):
        self.check_date_tap = self.driver.find_element_by_accessibility_id(self.check_date)
        super().tap_element(self.check_date_tap)
        return self.check_date_tap.get_attribute("checked")

    def switch_time_tap(self):
        self.switch_time_tap = self.driver.find_element_by_accessibility_id(self.switch_time)
        super().tap_element(self.switch_time_tap)
        return self.switch_time_tap.get_attribute("checked")

    def save_lazy_tap(self):
        sleep(3)
        self.save_lazy_tap = self.driver.find_element_by_xpath(self.save_lazy)
        super().tap_element(self.save_lazy_tap)
        super().wait_visibility_of_element_located(None, f"//android.widget.TextView[@text='Console: ps4']")

    def verify_text_in_screen(self, message):
        super().wait_element_to_be_clickable(None, f"//android.widget.TextView[@text='Console: ps4']")
        return message in self.driver.page_source

    def button_clear_tap(self):
        self.button_clear_tap = self.driver.find_element_by_xpath(self.button_clear)
        super().tap_element(self.button_clear_tap)

    def verify_data_screen_clear(self, message):
        super().wait_visibility_of_element_located(None, self.field_name)
        return message in self.driver.page_source
