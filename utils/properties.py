import os
from selenium import webdriver


class Properties:
    driver = None

    @staticmethod
    def get_driver(env_var_name, default_name='chromedriver'):
        if env_var_name is None:
            Properties.driver = webdriver.Chrome(os.getenv(default_name))
        else:
            Properties.driver = webdriver.Chrome(os.getenv(env_var_name))
        return Properties.driver
