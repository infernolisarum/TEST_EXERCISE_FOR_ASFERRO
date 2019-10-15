from xml.dom import minidom

from PO.WorkPages.GmailPage import GmailPage
from Tests.BaseStep import BaseStep


class GmailSteps(BaseStep):
    def __init__(self, driver):
        super(GmailSteps, self).__init__(driver)
        self.page = GmailPage(self.driver)
        self.start_steps()
        self.send_letter_to()
        self.check_last_letter_from_who()
        self.finish_tests()

    def start_steps(self):
        self.page.init_page()
        self.page.login("testforasferro", "TestForAsferro1")

    def send_letter_to(self):
        self.page.send_letter("testforasferro@gmail.com", "Darova korova!!!")

    def check_last_letter_from_who(self):
        self.page.refresh_mail()
        letters = self.page.get_all_letter()
        assert "Darova korova!!!" in letters[1].text

    def finish_tests(self):
        self.page.quit_driver()




