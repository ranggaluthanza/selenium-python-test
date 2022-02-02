import os
import platform
import warnings
from dotenv import load_dotenv

from selenium import webdriver
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.common.exceptions import TimeoutException


class LoginDriver:

    def __init__(self):
        load_dotenv()
        warnings.filterwarnings("ignore", category=DeprecationWarning)
        if platform.system() == "Safari":
            self.driver = webdriver.Safari()
        else:
            self.driver = webdriver.Chrome(executable_path=os.environ.get("CHROME_DRIVER"))

        self.login_url = "https://www.saucedemo.com/"
        self.valid_username = 'standard_user'
        self.valid_password = 'secret_sauce'

        # xPaths
        self.username_field_xpath = '//*[@id="user-name"]'
        self.password_field_xpath = '//*[@id="password"]'
        self.login_button_xpath = '//*[@id="login-button"]'
        self.main_logo_xpath = '//*[@id="header_container"]/div[1]/div[2]/div'

        # Etc.
        self.context = {}

        # Login Driver
        self.driver.maximize_window()
        self.driver.get(self.login_url)

        try:
            _ = WebDriverWait(self.driver, 3).until(
                EC.presence_of_element_located((By.ID, "user-name"))
            )
        except TimeoutException:
            return

        self.driver.find_element(By.XPATH, self.username_field_xpath).send_keys(self.valid_username)
        self.driver.find_element(By.ID, self.valid_password).send_keys(self.valid_password)

        self.driver.find_element(By.XPATH, self.login_button_xpath).click()

        try:
            _ = WebDriverWait(self.driver, 10).until(
                EC.text_to_be_present_in_element((By.XPATH, self.main_logo_xpath))
            )
        except TimeoutException:
            return