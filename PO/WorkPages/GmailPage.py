import time

from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as expected
from PO.BasePage import BasePage


class GmailPage(BasePage):

    def init_page(self):
        self.driver.get("https://mail.google.com/mail/?tab=wm&amp;ogbl")

    def login(self, login, password):
        self.driver.find_element(By.XPATH, "//input[@type='email']").send_keys(login)
        self.driver.find_element(By.XPATH, "//span[@class='RveJvd snByac']").click()
        WebDriverWait(self.driver, 10).until(expected.element_to_be_clickable((By.XPATH, "//input[@type='password']")))
        self.driver.find_element(By.XPATH, "//input[@type='password']").send_keys(password)
        self.driver.find_element(By.XPATH, "//span[@class='RveJvd snByac']").click()
        WebDriverWait(self.driver, 10).until(
            expected.element_to_be_clickable((By.XPATH, "//div[@class='T-I J-J5-Ji T-I-KE L3']")))

    def send_letter(self, to_whom, text_massage):
        self.driver.find_element(By.XPATH, "//div[@class='T-I J-J5-Ji T-I-KE L3']").click()
        WebDriverWait(self.driver, 10).until(expected.element_to_be_clickable((By.XPATH, "//div[@class='dC']")))
        self.driver.find_element(By.XPATH, "//textarea[@rows='1']").send_keys(to_whom)
        self.driver.find_element(By.XPATH, "//div[@role='textbox']").send_keys(text_massage)
        self.driver.find_element(By.XPATH, "//div[@class='dC']").click()

    def refresh_mail(self):
        self.driver.find_element(By.XPATH, "//div[@class='G-Ni J-J5-Ji']").click()
        time.sleep(5)

    def get_all_letter(self):
        letters = self.driver.find_elements(By.XPATH, "//div/div/table/tbody/tr[@class]")
        return letters
