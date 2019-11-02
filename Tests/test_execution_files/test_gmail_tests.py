import pytest

from infra.page_object.gmail_pages.gmail_main_page import GmailMainPage
from tests.test_config.gmail_test_config import GmailTestConfig as test_config
from utils.general_utils import text_utils


@pytest.mark.usefixtures("login_steps")
class TestsForAsferro():

    def test_for_asferro(self):
        page = GmailMainPage(self.driver)
        page.check_titile(test_config.login_name)
        for i in range(test_config.main_send_letters_number):
            temp_subject = text_utils.create_random_string(test_config.main_random_string_size)
            temp_text = text_utils.create_random_string(test_config.main_random_string_size)
            page.send_letter(test_config.main_mail_address, temp_subject, temp_text)
            page.wait_for_letter_is_loaded(temp_subject, temp_text)
        dict_for_letters = page.get_text_from_letters()
        result_text = text_utils.create_rusult_letter(dict_for_letters)
        page.send_letter(test_config.main_mail_address, test_config.main_result_letter_subject_text, result_text)
        page.refresh_letters()
        page.wait_for_letter_is_loaded(test_config.main_result_letter_subject_text, dict_for_letters.keys()[1])
        page.delete_all_letters_except_last()
        page.refresh_letters()
        page.wait_for_letter_is_loaded(test_config.main_result_letter_subject_text, dict_for_letters.keys()[1])
