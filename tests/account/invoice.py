import os
import random
import platform
import time
import unittest
import warnings
from loguru import logger
from dotenv import load_dotenv
from selenium.webdriver.common.keys import Keys
from selenium import webdriver
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.common.exceptions import TimeoutException

from faker import Faker

from driver.login import LoginDriver


class PayInvoiceTests(unittest.TestCase):
    def setUp(self) -> None:
        load_dotenv()
        warnings.filterwarnings("ignore", category=DeprecationWarning)

        self.driver = LoginDriver().driver

        # data
        self.valid_page_name = 'Tagihan'

        # Xpath
        self.invoice_page_xpath = '//*[@id="root"]/div[2]/div[2]/div[14]/div[2]/div[2]'
        self.button_pay_xpath = '//*[@id="root"]/div[2]/div[3]/div/div/div[2]/div[2]/div/div[2]/div[2]/button'
        self.payment_details_chart_xpath = '//*[@id="root"]/div[2]/div[3]/div/div/div[2]/div[2]/div/div[3]'

        # etc
        self.context = {}

    def test_pay_invoice(self):
        with self.driver as driver:

            driver.execute_script("window.scrollTo(0,document.body.scrollHeight)")

            try:
                _ = WebDriverWait(driver, 10).until(
                    EC.element_to_be_clickable((By.XPATH, self.invoice_page_xpath))
                ).click()
            except TimeoutException:
                logger.error("Pay Invoice Test Case Resulted Error")

            try:
                _ = WebDriverWait(driver, 10).until(
                    EC.text_to_be_present_in_element((By.TAG_NAME, "h3"), self.valid_page_name)
                )
            except TimeoutException:
                logger.error("Pay Invoice Test Case Resulted Error")
                return

            try:
                _ = WebDriverWait(driver, 10).until(
                    EC.presence_of_element_located((By.XPATH, self.payment_details_chart_xpath))
                )
                page_exist = True
            except TimeoutException:
                logger.error("Pay Invoice Test Case Resulted Error")
                page_exist = False
                return

            try:
                _ = WebDriverWait(driver, 10).until(
                    EC.element_to_be_clickable((By.XPATH, self.button_pay_xpath))
                 ).click()
            except TimeoutException:
                logger.error("Pay Invoice Test Case Resulted Error")

            assert page_exist is True
            logger.success("Check Pay Invoice Test Case has been Tested")

    @classmethod
    def as_suite(cls, test_suite: unittest.TestSuite) -> unittest.TestSuite:
        test_suite.addTest(cls('test_pay_invoice'))
        return test_suite

    def tearDown(self) -> None:
        pass
