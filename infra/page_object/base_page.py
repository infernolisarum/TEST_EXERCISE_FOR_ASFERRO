import clipboard
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as expected
from selenium.webdriver.support.wait import WebDriverWait
from infra.loggers.LoggingMix import LoggingMix


class BasePage(object, LoggingMix):
    def __init__(self, driver):
        self.driver = driver

    def wait_for_element_visibility(self, locator, timeout=10):
        try:
            return WebDriverWait(self.driver, timeout).until(expected.visibility_of_element_located(
                    locator))
        except Exception, e:
            self.error("wait_for_element_visibility crashed: '{0}'".format(e))

    def wait_for_text_to_be_present(self, locator, text, timeout=10):
        try:
            WebDriverWait(self.driver, timeout).until(expected.text_to_be_present_in_element(
                locator, text))
        except Exception, e:
            self.error("wait_for_text_to_be_present crashed: '{0}'".format(e))

    def paste_text_to_web_element(self, locator, text):
        clipboard.copy(text)
        self.wait_for_element_visibility(locator)\
            .send_keys(Keys.CONTROL, "v")
