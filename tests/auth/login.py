import os
import random
import time
import platform
import unittest
import warnings
from loguru import logger
from dotenv import load_dotenv

from selenium import webdriver
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.common.exceptions import TimeoutException

from faker import Faker

class LoginTests(unittest.TestCase):
    def setUp(self) -> None:
        load_dotenv()
        warnings.filterwarnings("ignore", category=DeprecationWarning)
        if platform.system() == "Darwin":
            self.driver = webdriver.Safari()
        else:
            self.driver = webdriver.Chrome(executable_path=os.environ.get("CHROME_DRIVER"))

        fake = Faker('id-ID')

        self.login_url = "https://www.saucedemo.com/"
        self.valid_username = 'standard_user'
        self.valid_password = 'secret_sauce'
        self.random_username = fake.name()
        self.random_password = fake.name()

        # xPaths
        self.username_field_xpath = '//*[@id="user-name"]'
        self.password_field_xpath = '//*[@id="password"]'
        self.login_button_xpath = '//*[@id="login-button"]'
        self.main_logo_xpath = '//*[@id="header_container"]/div[1]/div[2]/div'
        self.login_logo_xpath = '//*[@id="root"]/div/div[1]'

        # Etc.
        self.context = {}

        # Login Driver
        self.driver.maximize_window()
        self.driver.get(self.login_url)

    def test_valid_login(self):
        with self.driver as driver:
            driver.maximize_window()
            driver.get(self.login_url)

            try:
                _ = WebDriverWait(driver, 3).until(
                    EC.presence_of_element_located((By.XPATH, self.login_logo_xpath))
                )
            except TimeoutException:
                logger.error("Url page error")
                return

            driver.find_element(By.XPATH, self.username_field_xpath).send_keys(self.valid_username)
            driver.find_element(By.XPATH, self.password_field_xpath).send_keys(self.valid_password)

            driver.find_element(By.XPATH, self.login_button_xpath).click()

            try:
                _ = WebDriverWait(driver, 10).until(
                    EC.presence_of_element_located((By.XPATH, self.main_logo_xpath))
                )
                login_success = True
            except TimeoutException:
                logger.error("Home page after login error")
                return

            time.sleep(10)
            assert login_success is True
            logger.success("Login Valid Test Case has been Tested")

    def test_invalid_login(self):
        with self.driver as driver:
            driver.maximize_window()

            driver.get(self.login_url)

            try:
                _ = WebDriverWait(driver, 3).until(
                    EC.presence_of_element_located((By.XPATH, self.login_logo_xpath))
                )
            except TimeoutException:
                logger.error("Login Invalid Test Case resulted Error")
                return

            driver.find_element(By.XPATH, self.username_field_xpath).send_keys(self.random_username)
            driver.find_element(By.XPATH, self.password_field_xpath).send_keys(self.random_password)

            driver.find_element(By.XPATH, self.login_button_xpath).click()

            try:
                _ = WebDriverWait(driver, 10).until(
                    EC.text_to_be_present_in_element(
                        (By.TAG_NAME, "h3"), "Epic sadface: Username and password do not match any user in this service")
                )
            except TimeoutException:
                logger.error("Login Invalid Test Case resulted Error")
                return

            assert "Epic sadface: Username and password do not match any user in this service" in driver.page_source
            logger.success("Login Invalid Test Case has been Tested")

    def tearDown(self) -> None:
        pass