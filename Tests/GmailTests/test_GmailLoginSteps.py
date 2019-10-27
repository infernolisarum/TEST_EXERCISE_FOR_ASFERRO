from PO.WorkPages.GmailPage import GmailPage


class TestGmailLoginSteps(object):
    gmail_login_page_url = "https://mail.google.com/mail/?tab=wm&amp;ogbl"
    login_name = "testforasferro"
    login_password = "TestForAsferro1"

    def __init__(self, driver):
        self.page = GmailPage(driver)

    def open_gmail_login_page(self):
        self.page.go_to(self.gmail_login_page_url)

    def input_email_and_password(self):
        self.page.login(self.login_name, self.login_password)
        self.page.at_page(self.login_name)
