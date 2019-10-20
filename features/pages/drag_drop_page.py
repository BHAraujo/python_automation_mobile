import sys
sys.path.append("..")

from time import sleep
from .base_page import BasePage



class DragDropPage(BasePage):
    def __init__(self):
        self.driver = BasePage().driver
        self.menu_drag_drop = "//android.widget.TextView[@text='Drag and drop']"
        self.this = "//android.widget.TextView[@text='Esta']"
        self.is_list = "//android.widget.TextView[@text='é uma lista']"
        self.drag = "//android.widget.TextView[@text='Drag em Drop!']"
        self.long_click = "//android.widget.TextView[@text='Faça um clique longo,']"
        self.drag_drop = "//android.widget.TextView[@text='e arraste para']"
        self.wish = "//android.widget.TextView[@text='qualquer local desejado.']"

    def menu_drag_drop_tap(self):
        sleep(3)
        self.driver.swipe(100, 700, 100, 150)
        super().wait_element_to_be_clickable(None, self.menu_drag_drop)
        self.menu_drag_drop_tap = self.driver.find_element_by_xpath(self.menu_drag_drop)
        super().tap_element(self.menu_drag_drop_tap)

    def wait_drag_drop(self):
        super().wait_element_to_be_clickable(None, self.this)

    def drag_and_drop_elements(self, firt_element, second_element):
        dict_element = {
                        "Esta": self.this, "lista": self.is_list,
                        "Drop!": self.drag, "longo": self.long_click,
                        "para": self.drag_drop, "desejado": self.wish
                         }
        super().drag_and_drop_element(self.driver.find_element_by_xpath(dict_element[firt_element.replace('"','')]),
                                          self.driver.find_element_by_xpath(dict_element[second_element.replace('"','')]))
    def take_screenshot_save(self):
        super().take_screenshot("drag_drop", "drag_drop.png")
