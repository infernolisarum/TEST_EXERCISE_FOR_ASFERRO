from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager

from Tests.GmailTests.GmailSteps import GmailSteps

driver = webdriver.Chrome("AttachedFiles\drivers\chromedriver.exe")
GmailSteps(driver)
