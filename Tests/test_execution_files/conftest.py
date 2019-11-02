import pytest

from infra.page_object.gmail_pages.gmail_login_page import GmailLoginPage
from tests.test_config.gmail_test_config import GmailTestConfig
from utils.properties import Properties


@pytest.fixture(scope="function")
def login_steps(request):
    driver = Properties.get_driver(None)
    login_page = GmailLoginPage(driver)
    login_page.init_login_page(GmailTestConfig.login_page_url)
    login_page.login(GmailTestConfig.login_name, GmailTestConfig.login_password)
    request.cls.driver = driver
    yield
    driver.quit()
