from selenium.common.exceptions import StaleElementReferenceException
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as expected
from selenium.webdriver.support.wait import WebDriverWait
from infra.page_object.base_page import BasePage


class GmailMainPage(BasePage):
    write_new_letter_button_locator = (By.XPATH, "//div[@class='T-I J-J5-Ji T-I-KE L3']")
    new_letter_address_field_locator = (By.XPATH, "//textarea[@rows='1']")
    new_letter_subjectbox_locator = (By.XPATH, "//input[@name='subjectbox']")
    new_letter_textbox_locator = (By.XPATH, "//div[@role='textbox']")
    send_new_letter_button_locator = (By.XPATH, "//div[@class='dC']")

    refresh_mail_button_locator = (By.XPATH, "//div[@class='T-I J-J5-Ji nu T-I-ax7 L3' and @role='button']")
    select_all_letters_locator = (By.XPATH, "//div/div/table/tbody/tr[@jsmodel='nXDxbd']")

    message_subject_locator = ".//td/div/div/div/span/span[@class='bqe']"
    message_text_locator = ".//td/div/div/span[@class='y2']"
    from_who_address_locator = ".//td/div/span/span[@email]"
    all_letters_checkbox_locator = (By.XPATH, "//div/div/div/span[@role='checkbox']")
    any_letter_checkbox_locator = (By.XPATH, ".//tr/td/div[@role='checkbox']")
    delete_letter_button_locator = (By.XPATH, ".//div/div/div[@role='button' and @data-tooltip='Delete']")

    def check_titile(self, title_name, timeout=15):
        try:
            WebDriverWait(self.driver, timeout).until(expected.title_contains(title_name))
            self.info("'{0}' is present in the title.".format(title_name))
        except Exception, e:
            self.error("'{0}' isn't present in the title. error: '{1}'".format(title_name, e.message))

    def send_letter(self, address, subject_message, text_massage):
        self.wait_for_element_visibility(self.write_new_letter_button_locator)\
            .click()
        self.paste_text_to_web_element(self.new_letter_address_field_locator, address)
        self.paste_text_to_web_element(self.new_letter_subjectbox_locator, subject_message)
        self.paste_text_to_web_element(self.new_letter_textbox_locator, text_massage)
        self.wait_for_element_visibility(self.send_new_letter_button_locator)\
            .click()
        self.info("Letter sent successfully.")

    def refresh_letters(self):
        self.wait_for_element_visibility(self.refresh_mail_button_locator)\
            .click()

    def get_all_letters(self):
        letters = WebDriverWait(self.driver, 5).until(expected.presence_of_all_elements_located(
            self.select_all_letters_locator))
        return letters

    def wait_for_letter_is_loaded(self, subject, text):
        self.wait_for_text_to_be_present((By.XPATH, self.message_subject_locator), subject)
        self.wait_for_text_to_be_present((By.XPATH, self.message_text_locator), text)

    def get_text_from_letters(self):
        result_dict = {}
        letters = self.get_all_letters()
        for i in range(len(letters)):
            try:
                message_subject = str(letters[i].find_element_by_xpath(self.message_subject_locator).text)
                message_text = str(letters[i].find_element_by_xpath(self.message_text_locator).text)
                format_message_text = message_text.replace(" - \n", "")
                result_dict[message_subject] = format_message_text
            except StaleElementReferenceException:
                self.error("Catched and ignored: StaleElementReferenceException")
                pass
        self.info("get_text_from_letters completed successfully")
        return result_dict

    def delete_all_letters_except_last(self):
        try:
            self.wait_for_element_visibility(self.all_letters_checkbox_locator)\
                .click()
            self.wait_for_element_visibility(self.any_letter_checkbox_locator)\
                .click()
            self.wait_for_element_visibility(self.delete_letter_button_locator)\
                .click()
        except StaleElementReferenceException:
            self.error("Catched and ignored: StaleElementReferenceException")
            pass
        letters = self.get_all_letters()
        assert 1 == len(letters), self.error("delete_all_letters_except_last didn't complete correctly. "
                                             "The letters number is '{0}'".format(len(letters)))
        self.info("delete_all_letters_except_last completed successfully")
