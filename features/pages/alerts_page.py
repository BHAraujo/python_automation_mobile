import sys
sys.path.append("..")

from time import sleep

from .base_page import BasePage
from helper.helpers import remove_aspas


class AlertsPage(BasePage):
    def __init__(self):
        self.driver = BasePage().driver
        self.menu_alerts = "//android.widget.TextView[@text='Alertas']"
        self.simple_alert = "//android.widget.TextView[@text='ALERTA SIMPLES']"
        self.message_alert = "android:id/message"
        self.button_ok_simple_alert = "android:id/button1"
        self.restrict_alert = "//android.widget.TextView[@text='ALERTA RESTRITIVO']"
        self.button_sair = "android:id/button1"
        self.confirm_alert = "//android.widget.TextView[@text='ALERTA CONFIRM']"
        self.button_ok = "android:id/button2"

    def menu_alerts_tap(self):
        super().wait_element_to_be_clickable(None, self.menu_alerts)
        self.menu_alerts_tap = self.driver.find_element_by_xpath(self.menu_alerts)
        super().tap_element(self.menu_alerts_tap)

    def wait_element_alert(self):
        super().wait_element_to_be_clickable(None, self.simple_alert)

    def simple_alerts_tap(self):
        super().wait_element_to_be_clickable(None, self.simple_alert)
        self.simple_alert_tap = self.driver.find_element_by_xpath(self.simple_alert)
        super().tap_element(self.simple_alert_tap)

    def verify_alert_text(self, message):
        sleep(1.5)
        return remove_aspas(message) in self.driver.page_source

    def button_ok_simple_alert_click(self):
        self.button_ok_simple_alert_click = self.driver.find_element_by_id(self.button_ok_simple_alert)
        super().tap_element(self.button_ok_simple_alert_click)

    def restrict_alert_tap(self):
        super().wait_visibility_of_element_located(None, self.restrict_alert)
        self.restrict_alert_tap = self.driver.find_element_by_xpath(self.restrict_alert)
        super().tap_element(self.restrict_alert_tap)

    def button_sair_tap(self):
        super().wait_element_to_be_clickable("ID", self.button_sair)
        self.button_sair_tap = self.driver.find_element_by_id(self.button_sair)
        super().tap_element(self.button_sair_tap)

    def confirm_alert_tap(self):
        sleep(2)
        self.confirm_alert_tap = self.driver.find_element_by_xpath(self.confirm_alert)
        super().tap_element(self.confirm_alert_tap)

    def button_ok_tap(self):
        super().wait_element_to_be_clickable("ID", self.button_ok)
        self.button_ok_tap = self.driver.find_element_by_id(self.button_ok)
        super().tap_element(self.button_ok_tap)
