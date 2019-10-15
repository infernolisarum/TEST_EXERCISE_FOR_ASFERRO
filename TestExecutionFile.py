from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager

from Tests.GmailTests.GmailSteps import GmailSteps

GmailSteps(webdriver.Chrome(ChromeDriverManager().install("AttachedFiles/drivers")))
