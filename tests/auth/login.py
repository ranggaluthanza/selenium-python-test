import os
import random
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

        self.login_url = "https://silvi-merchant-develop.netlify.app/"
        self.valid_email = 'samsantechrestoran@mailnesia.com'
        self.valid_password = '123456'
        self.valid_merchant_name = 'Samsan Tech Restoran!!'

        self.invalid_email = fake.email()
        self.invalid_password = random.randint(99999, 999999)

        # xPaths
        self.login_button_xpath = '//*[@id="root"]/div[2]/div/div[2]/form/button'

        # Etc.
        self.context = {}

    def test_valid_login(self):
        with self.driver as driver:
            driver.maximize_window()

            driver.get(self.login_url)

            try:
                _ = WebDriverWait(driver, 3).until(
                    EC.presence_of_element_located((By.ID, "email"))
                )
            except TimeoutException:
                logger.error("Login Valid Test Case resulted Error")
                return

            driver.find_element(By.ID, "email").send_keys(self.valid_email)
            driver.find_element(By.ID, "pin").send_keys(self.valid_password)

            driver.find_element(By.XPATH, self.login_button_xpath).click()

            try:
                _ = WebDriverWait(driver, 10).until(
                    EC.text_to_be_present_in_element((By.TAG_NAME, "h4"), self.valid_merchant_name)
                )
            except TimeoutException:
                logger.error("Login Valid Test Case resulted Error")
                return

            assert self.valid_merchant_name in driver.page_source
            logger.success("Login Valid Test Case has been Tested")

    def test_invalid_login(self):
        with self.driver as driver:
            driver.maximize_window()

            driver.get(self.login_url)

            try:
                _ = WebDriverWait(driver, 3).until(
                    EC.presence_of_element_located((By.ID, "email"))
                )
            except TimeoutException:
                logger.error("Login Invalid Test Case resulted Error")
                return

            driver.find_element(By.ID, "email").send_keys(self.invalid_email)
            driver.find_element(By.ID, "pin").send_keys(self.invalid_password)

            driver.find_element(By.XPATH, self.login_button_xpath).click()

            try:
                _ = WebDriverWait(driver, 10).until(
                    EC.text_to_be_present_in_element(
                        (By.CLASS_NAME, "MuiAlert-message"), "Bad Credential")
                )
            except TimeoutException:
                logger.error("Login Invalid Test Case resulted Error")
                return

            assert "Bad Credential" in driver.page_source
            logger.success("Login Invalid Test Case has been Tested")

    def tearDown(self) -> None:
        pass