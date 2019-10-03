import yaml
from appium import webdriver
import os


def capabilities():
    config = yaml.safe_load(open(f"{os.getcwd()}/service/capabilities.yml"))
    desired_caps = {}
    desired_caps['platformName'] = config["platformName"]
    desired_caps['platformVersion'] = config["platformVersion"]
    desired_caps['automationName'] = config["automationName"]
    desired_caps['deviceName'] = config["deviceName"]
    desired_caps['app'] = "{}/service/apk/{}".format(os.getcwd(), config["app"])
    return desired_caps


class Emulator():
    def __init__(self):
        self.capabilities = capabilities()
        self.driver = webdriver.Remote('http://localhost:4723/wd/hub', self.capabilities)

    def set_driver(self):
        return self.driver
