class BasePage(object):
    def __init__(self, driver):
        self.driver = driver

    def quit_driver(self):
        self.driver.quit()