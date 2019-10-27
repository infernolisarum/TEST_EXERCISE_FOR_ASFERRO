from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as expected
from PO.BasePage import BasePage


class GmailPage(BasePage):
    message_subject_locator = ".//td/div/div/div/span/span[@class='bqe']"
    message_text_locator = ".//td/div/div/span[@class='y2']"
    from_who_address_locator = ".//td/div/span/span[@email]"
    all_letters_checkbox_locator = (By.XPATH, "//div/div/div/span[@role='checkbox']")
    any_letter_checkbox_locator = ".//tr/td/div[@role='checkbox']"
    delete_letter_button_locator = (By.XPATH, ".//div/div/div[@role='button' and @data-tooltip='Delete']")

    def login(self, login, password):
        email_field_locator = (By.XPATH, "//input[@type='email']")
        login_button_locator = (By.XPATH, "//span[@class='RveJvd snByac']")
        password_field_locator = (By.XPATH, "//input[@type='password']")
        WebDriverWait(self.driver, 10).until(expected.visibility_of_element_located(
            email_field_locator)).send_keys(login)
        WebDriverWait(self.driver, 10).until(expected.element_to_be_clickable(
            login_button_locator)).click()
        WebDriverWait(self.driver, 10).until(expected.visibility_of_element_located(
            password_field_locator)).send_keys(password)
        WebDriverWait(self.driver, 10).until(expected.element_to_be_clickable(
            login_button_locator)).click()

    def send_letter(self, address, subject_message, text_massage):
        new_letter_button_locator = (By.XPATH, "//div[@class='T-I J-J5-Ji T-I-KE L3']")
        address_field_locator = (By.XPATH, "//textarea[@rows='1']")
        subjectbox_locator = (By.XPATH, "//input[@name='subjectbox']")
        textbox_locator = (By.XPATH, "//div[@role='textbox']")
        send_letter_locator = (By.XPATH, "//div[@class='dC']")
        WebDriverWait(self.driver, 10).until(
            expected.element_to_be_clickable(new_letter_button_locator)).click()
        WebDriverWait(self.driver, 7).until(expected.visibility_of_element_located(address_field_locator))\
            .send_keys(address)
        WebDriverWait(self.driver, 7).until(expected.visibility_of_element_located(subjectbox_locator))\
            .send_keys(subject_message)
        WebDriverWait(self.driver, 7).until(expected.visibility_of_element_located(textbox_locator))\
            .send_keys(text_massage)
        WebDriverWait(self.driver, 10).until(expected.element_to_be_clickable(send_letter_locator)).click()

    def refresh_letters(self):
        refresh_button_locator = (By.XPATH, "//div[@class='T-I J-J5-Ji nu T-I-ax7 L3' and @role='button']")
        WebDriverWait(self.driver, 5).until(expected.visibility_of_element_located(refresh_button_locator)).click()

    def get_all_letters(self):
        all_letters_locator = (By.XPATH, "//div/div/table/tbody/tr[@jsmodel='nXDxbd']")
        letters = WebDriverWait(self.driver, 5).until(expected.presence_of_all_elements_located(all_letters_locator))
        return letters
