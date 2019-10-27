import pytest

from Tests.BaseStep import BaseStep
from Tests.GmailTests.test_GmailLoginSteps import TestGmailLoginSteps


@pytest.fixture(scope="function")
def login_steps(request):
    base = BaseStep()
    driver = base.init_driver()
    login = TestGmailLoginSteps(driver)
    login.open_gmail_login_page()
    login.input_email_and_password()
    request.cls.driver = driver
    yield
    base.quit_driver()
