from selenium.webdriver.common.by import By
from infra.page_object.base_page import BasePage


class GmailLoginPage(BasePage):

    def init_login_page(self, url_address):
        self.driver.get(url_address)

    def login(self, login, password):
        login_button_locator = (By.XPATH, "//span[@class='RveJvd snByac']")
        email_field_locator = (By.XPATH, "//input[@type='email']")
        password_field_locator = (By.XPATH, "//input[@type='password']")
        self.paste_text_to_web_element(email_field_locator, login)
        self.wait_for_element_visibility(login_button_locator)\
            .click()
        self.paste_text_to_web_element(password_field_locator, password)
        self.wait_for_element_visibility(login_button_locator)\
            .click()
        self.info("Login steps is completed successfully.")
