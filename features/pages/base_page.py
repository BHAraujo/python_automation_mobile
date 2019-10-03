from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from appium.webdriver.common.touch_action import TouchAction

from environment import driver
from helper.constants import TIMEOUT


class BasePage():
    def __init__(self):
        self.driver = driver
        self.wait = WebDriverWait(self.driver, TIMEOUT)
        self.action = TouchAction(self.driver)

    def wait_element_to_be_clickable(self, type, element):
        if type is None:
            return self.wait.until(EC.element_to_be_clickable((By.XPATH, element)))
        else:
            return self.wait.until(EC.element_to_be_clickable((By.ID, element)))

    def wait_visibility_of_element_located(self,type, element):
        if type is None:
            return self.wait.until(EC.visibility_of_element_located((By.XPATH, element)))
        else:
            return self.wait.until(EC.visibility_of_element_located((By.ID, element)))

    def tap_element(self, element):
        self.action.tap(element).perform()

    def long_click_element(self, element):
        self.action.long_press(element).perform()

    def double_click_element(self, element):
        self.action.tap(element, count=2).perform()

    def lazy_double_click_tap(self, element):
        for x in range(0,2):
            self.action.press(element).wait(1500).perform()

    def fill_field(self, element,value):
        element.send_keys(value)

    def take_screenshot(self, folder, namefile):
        path = f"reports/screenshots/{folder}/{namefile}"
        self.driver.save_screenshot(path)

    def swipe_screen(self, lista=[]):
        self.driver.swipe(lista[0], lista[1], lista[2], lista[3])

    def drag_and_drop_element(self, firt_element, second_element):
        self.driver.drag_and_drop(firt_element, second_element)

    def send_keys_field(self, element, text):
        element.send_keys(text)

    def verify_text_in_activity(self, message):
        return message in self.driver.page_source
