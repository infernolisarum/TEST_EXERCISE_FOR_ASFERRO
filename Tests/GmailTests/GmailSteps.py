import random
import string

from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as expected
from selenium.webdriver.support.wait import WebDriverWait

from PO.WorkPages.GmailPage import GmailPage
from Tests.BaseStep import BaseStep


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


class GmailSteps(BaseStep):
    number_letters = 15
    mail_address = "testforasferro@gmail.com"
    result_letter_subject = "Result letter"
    message_subject_locator = ".//td/div/div/div/span/span[@class='bqe']"
    message_text_locator = ".//td/div/div/span[@class='y2']"

    def __init__(self, driver):
        super(GmailSteps, self).__init__(driver)
        self.dict_for_letters = {}
        self.page = GmailPage(self.driver)
        self.start_steps()
        self.send_package_letters_to_yourself()
        self.select_text_from_package_letters()
        self.send_result_letter_with_report()
        self.delete_all_letters_except_last()
        self.finish_tests()

    def start_steps(self):
        self.page.init_page()
        self.page.login("testforasferro", "TestForAsferro1")

    def send_package_letters_to_yourself(self):
        for i in range(self.number_letters):
            temp_subject, temp_text = "", ""
            temp_subject += create_random_string()
            temp_text += create_random_string()
            self.page.send_letter(self.mail_address, temp_subject, temp_text)
            self.check_sending_letter(temp_subject, temp_text)

    def check_sending_letter(self, subject, text):
        WebDriverWait(self.page.driver, 7).until(expected.text_to_be_present_in_element(
            (By.XPATH, self.message_subject_locator), subject))
        WebDriverWait(self.page.driver, 7).until(expected.text_to_be_present_in_element(
            (By.XPATH, self.message_text_locator), text))

    def select_text_from_package_letters(self):
        from_who_address_locator = ".//td/div/span/span[@email]"
        verified_letters = []
        letters = self.page.get_all_letters()
        for i in range(len(letters)):
            if i > 15:
                break
            from_who = str(letters[i].find_element_by_xpath(from_who_address_locator).get_attribute("email"))
            if self.mail_address in from_who:
                verified_letters.append(letters[i])
        for i in range(len(verified_letters)):
            message_subject = str(verified_letters[i].find_element_by_xpath(self.message_subject_locator).text)
            message_text = str(verified_letters[i].find_element_by_xpath(self.message_text_locator).text)
            format_message_text = message_text.replace(" - \n", "")
            self.dict_for_letters[message_subject] = format_message_text

    def send_result_letter_with_report(self):
        result_string = ""
        for key, value in self.dict_for_letters.iteritems():
            char_counter = character_counter(value)
            report_format = "Received mail on theme '{0}' with message: '{1}'. It contains '{2}' letters and '{3}' " \
                            "numbers".format(key, value, char_counter, 10 - char_counter)
            result_string += (report_format + "\n")
        self.page.send_letter(self.mail_address, self.result_letter_subject, result_string)
        self.page.refresh_letters()

    def delete_all_letters_except_last(self):
        select_all_letters_locator = (By.XPATH, "//div/div/div/span[@role='checkbox']")
        checkbox_any_letter_locator = ".//tr/td/div[@role='checkbox']"
        delete_button_locator = (By.XPATH, ".//div/div/div[@role='button' and @data-tooltip='Delete']")
        WebDriverWait(self.page.driver, 7).until(expected.element_to_be_clickable(
            select_all_letters_locator)).click()
        WebDriverWait(self.page.driver, 7).until(expected.element_to_be_clickable(
            (By.XPATH, checkbox_any_letter_locator))).click()
        WebDriverWait(self.page.driver, 7).until(expected.element_to_be_clickable(delete_button_locator)).click()
        self.page.refresh_letters()
        WebDriverWait(self.page.driver, 7).until(expected.element_to_be_clickable(
            (By.XPATH, checkbox_any_letter_locator)))

    # TODO: move to BaseStep
    def finish_tests(self):
        self.page.quit_driver()
