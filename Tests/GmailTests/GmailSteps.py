import random
import string

from selenium.common.exceptions import NoSuchElementException, StaleElementReferenceException
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
    def __init__(self, driver):
        super(GmailSteps, self).__init__(driver)
        self.number_letters = 15
        self.my_dict_for_letters = {}
        self.mail_address = "testforasferro@gmail.com"
        self.page = GmailPage(self.driver)
        self.start_steps()
        self.send_letters_to_yourself()
        self.select_text_from_my_letters()
        self.send_result_letter_with_report()
        self.finish_tests()

    def start_steps(self):
        self.page.init_page()
        self.page.login("testforasferro", "TestForAsferro1")

    def send_letters_to_yourself(self):
        for i in range(self.number_letters):
            self.page.send_letter(self.mail_address, create_random_string(), create_random_string())
            self.page.refresh_mail()

    # TODO: after 'for' => 'if current_number_letters < 15:'...
    def check_letters_in_mail(self):
        current_number_letters = 0
        verified_letters = []
        letters = self.page.get_all_letters()
        for i in range(len(letters)):
            from_whom = str(letters[i].find_element_by_xpath(".//td/div/span/span[@email]").get_attribute("email"))
            if self.mail_address in from_whom:
                verified_letters.append(letters[i])
                current_number_letters += 1
            elif current_number_letters < self.number_letters:
                assert "Found {current_number_letters} letters of {number_letters} sent letters."
        return verified_letters

    def select_text_from_my_letters(self):
        message_subject_locator = ".//td/div/div/div/span/span[@class='bqe']"
        message_text_locator = ".//td/div/div/span[@class='y2']"
        self.page.refresh_mail()
        letters = self.check_letters_in_mail()
        for i in range(len(letters)):
            message_subject = str(letters[i].find_element_by_xpath(message_subject_locator).text)
            message_text = str(letters[i].find_element_by_xpath(message_text_locator).text)
            format_message_text = message_text.replace(" - \n", "")
            self.my_dict_for_letters[message_subject] = format_message_text

    def send_result_letter_with_report(self):
        result_string = ""
        for key, value in self.my_dict_for_letters.iteritems():
            char_counter = character_counter(value)
            report_format = "Received mail on theme '{0}' with message: '{1}'. It contains '{2}' letters and '{3}' " \
                            "numbers".format(key, value, char_counter, 10 - char_counter)
            result_string += (report_format + "\n")
        self.page.send_letter(self.mail_address, "Result letter", result_string)
        self.page.refresh_mail()

    def finish_tests(self):
        self.page.quit_driver()
