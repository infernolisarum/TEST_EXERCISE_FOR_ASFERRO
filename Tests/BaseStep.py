from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager


class BaseStep(object):
    def __init__(self):
        self.driver = None

    def init_driver(self):
        self.driver = webdriver.Chrome("AttachedFiles\drivers\chromedriver.exe")
        return self.driver

    def quit_driver(self):
        self.driver.quit()
