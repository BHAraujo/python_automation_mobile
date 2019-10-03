import yaml
import os
from appium import webdriver
from service.emulator import Emulator


driver = Emulator().set_driver()


def before_all(context):
    if not context.config.log_capture:
        logging.basicConfig(level=logging.DEBUG)

def after_scenario(context, scenario):
    driver.close_app()

def before_scenario(context, scenario):
    driver.launch_app()
    if "skip" in scenario.tags:
        scenario.skip("@skip")
