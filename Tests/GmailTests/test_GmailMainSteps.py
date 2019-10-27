import random
import string
import pytest
from selenium.common.exceptions import StaleElementReferenceException

from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as expected
from selenium.webdriver.support.wait import WebDriverWait

from PO.WorkPages.GmailPage import GmailPage


def create_random_string():
    string_size = 10
    chars = string.ascii_uppercase + string.ascii_lowercase + string.digits
    result_string = ""
    for _ in range(string_size):
        result_string += random.choice(chars)
    return result_string


def character_counter(string_to_count):
    char_counter = 0
    for i in string_to_count:
        if i.isalpha():
            char_counter += 1
    return char_counter


@pytest.mark.usefixtures("login_steps")
class TestGmailMainSteps(object):
    number_letters = 15
    mail_address = "testforasferro@gmail.com"
    result_letter_subject_value = "Result letter"

    def test_gmail_main_steps(self):
        self.page = GmailPage(self.driver)
        self.dict_for_letters = {}
        self.send_package_letters_to_yourself()
        self.select_text_from_package_letters()
        self.send_result_letter_with_report()
        self.delete_all_letters_except_last()

    def send_package_letters_to_yourself(self):
        for i in range(self.number_letters):
            temp_subject, temp_text = "", ""
            temp_subject += create_random_string()
            temp_text += create_random_string()
            self.page.send_letter(self.mail_address, temp_subject, temp_text)
            self.check_sending_letter(temp_subject, temp_text)

    def check_sending_letter(self, subject, text):
        WebDriverWait(self.page.driver, 7).until(expected.text_to_be_present_in_element(
            (By.XPATH, self.page.message_subject_locator), subject))
        WebDriverWait(self.page.driver, 7).until(expected.text_to_be_present_in_element(
            (By.XPATH, self.page.message_text_locator), text))

    def select_text_from_package_letters(self):
        verified_letters = []
        letters = self.page.get_all_letters()
        for i in range(len(letters)):
            if i > self.number_letters:
                break
            from_who = str(letters[i].find_element_by_xpath(self.page.from_who_address_locator).get_attribute("email"))
            if self.mail_address in from_who:
                verified_letters.append(letters[i])
        for i in range(len(verified_letters)):
            message_subject = str(verified_letters[i].find_element_by_xpath(self.page.message_subject_locator).text)
            message_text = str(verified_letters[i].find_element_by_xpath(self.page.message_text_locator).text)
            format_message_text = message_text.replace(" - \n", "")
            self.dict_for_letters[message_subject] = format_message_text

    def send_result_letter_with_report(self):
        result_string = ""
        for key, value in self.dict_for_letters.iteritems():
            char_counter = character_counter(value)
            report_format = "Received mail on theme '{0}' with message: '{1}'. It contains '{2}' letters and '{3}' " \
                            "numbers".format(key, value, char_counter, 10 - char_counter)
            result_string += (report_format + "\n")
        self.page.send_letter(self.mail_address, self.result_letter_subject_value, result_string)
        self.page.refresh_letters()

    def delete_all_letters_except_last(self):
        try:
            WebDriverWait(self.page.driver, 7).until(expected.text_to_be_present_in_element(
                (By.XPATH, self.page.message_subject_locator), self.result_letter_subject_value))
            WebDriverWait(self.page.driver, 7).until(expected.element_to_be_clickable(
                self.page.all_letters_checkbox_locator)).click()
            WebDriverWait(self.page.driver, 7).until(expected.element_to_be_clickable(
                (By.XPATH, self.page.any_letter_checkbox_locator))).click()
            WebDriverWait(self.page.driver, 7).until(expected.element_to_be_clickable(
                self.page.delete_letter_button_locator)).click()
            self.page.refresh_letters()
            WebDriverWait(self.page.driver, 7).until(expected.text_to_be_present_in_element(
                (By.XPATH, self.page.message_subject_locator), self.result_letter_subject_value))
        except StaleElementReferenceException:
            pass
