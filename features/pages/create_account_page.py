import sys
sys.path.append("..")

from .base_page import BasePage


class CreateAccountPage(BasePage):
    def __init__(self):
        self.driver = BasePage().driver
        self.menu_hibrido = "//android.widget.TextView[@text='SeuBarriga Híbrido']"
        self.new_user = "//android.view.View[@text='Novo usuário?']"
        self.field_name = "//android.widget.EditText[contains(@resource-id,'nome')]"
        self.field_email =  "//android.widget.EditText[contains(@resource-id,'email')]"
        self.field_password =  "//android.widget.EditText[contains(@resource-id,'senha')]"
        self.button_save = "//android.widget.Button[@text='Cadastrar']"
        self.button_login = "//android.widget.Button[@text='Entrar']"

    def menu_hidrido_tap(self):
        BasePage().wait_element_to_be_clickable(None, self.menu_hibrido)
        self.menu_hidrido_tap = self.driver.find_element_by_xpath(self.menu_hibrido)
        BasePage().tap_element(self.menu_hidrido_tap)

    def new_user_tap(self):
        self.new_user_tap = self.driver.find_element_by_xpath(self.new_user)
        BasePage().tap_element(self.new_user_tap)

    def wait_menu_create_account(self):
        BasePage().wait_element_to_be_clickable(None, self.new_user)

    def field_name_send_keys(self, text):
        BasePage().wait_visibility_of_element_located(None, self.field_name)
        self.send_field_name = self.driver.find_element_by_xpath(self.field_name)
        BasePage().send_keys_field(self.send_field_name, text)

    def field_email_send_keys(self, text):
        self.get_field_email = self.driver.find_element_by_xpath(self.field_email)
        BasePage().send_keys_field(self.get_field_email, text)

    def field_password_send_keys(self, text):
        self.get_field_password = self.driver.find_element_by_xpath(self.field_password)
        BasePage().send_keys_field(self.get_field_password, text)

    def button_save_tap(self):
        BasePage().wait_element_to_be_clickable(None, self.button_save)
        self.button_save_tap = self.driver.find_element_by_xpath(self.button_save)
        BasePage().tap_element(self.button_save_tap)

    def verify_text_in_screen(self, message):
        return message in self.driver.page_source

    def do_login(self, email, password):
        BasePage().wait_visibility_of_element_located(None, self.field_email)
        BasePage().send_keys_field(self.get_field_email, email)
        BasePage().send_keys_field(self.get_field_password, password)
        self.button_login_tap = self.driver.find_element_by_xpath(self.button_login)
        BasePage().tap_element(self.button_login_tap)
