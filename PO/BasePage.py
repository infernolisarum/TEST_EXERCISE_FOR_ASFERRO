from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as expected


class BasePage(object):
    def __init__(self, driver):
        self.driver = driver

    def go_to(self, url_address):
        self.driver.get(url_address)

    def at_page(self, title_name):
        WebDriverWait(self.driver, 7).until(expected.title_contains(title_name))
