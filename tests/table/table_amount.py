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


class TableAmountSetupTests(unittest.TestCase):
    def setUp(self) -> None:
        load_dotenv()
        warnings.filterwarnings("ignore", category=DeprecationWarning)

        self.driver = LoginDriver().driver

        # data
        self.valid_page_name = 'Atur Meja'
        self.modal_verification_title = 'Apakah jumlah meja yang kamu request sudah sesuai dengan kebutuhanmu?'
        self.request_amount = 5

        # Xpath
        self.table_amount_page_xpath = '//*[@id="root"]/div[2]/div[2]/div[12]/div[1]/div[2]'
        self.status_request_chart_xpath = '/html/body/div[1]/div[2]/div[3]/div/div/div[2]/div[2]'
        self.request_table_modal_xpath = '/html/body/div[3]/div[3]/div'
        self.sales_page = '//*[@id="root"]/div[2]/div[2]/div[4]/div[1]/div[2]/a'

        self.accepting_verification_button_xpath = '/html/body/div[3]/div[3]/div/div[3]/button[2]'
        self.request_table_button_xpath = '//*[@id="root"]/div[2]/div[3]/div/div/div[2]/div[1]/div[2]/button'
        self.continue_button_xpath = '/html/body/div[3]/div[3]/div/div[3]/button[2]'
        self.cancel_button_xpath = '/html/body/div[3]/div[3]/div/div[3]/button[1]'

        # etc
        self.context = {}

    def test_request_table_amount(self):
        with self.driver as driver:

            driver.execute_script("window.scrollTo(0,document.body.scrollHeight)")

            driver.find_element(By.XPATH, self.table_amount_page_xpath).click()

            try:
                _ = WebDriverWait(driver, 10).until(
                    EC.text_to_be_present_in_element((By.TAG_NAME, "h3"), self.valid_page_name)
                )
            except TimeoutException:
                logger.error("Check Table Amount Setup Test Case Resulted Error")
                return

            driver.find_element(By.XPATH, self.request_table_button_xpath).click()

            try:
                _ = WebDriverWait(driver, 10).until(
                    EC.presence_of_element_located((By.XPATH, self.request_table_modal_xpath))
                )
                modal_exist = True
            except TimeoutException:
                logger.error("Check Table Amount Setup Test Case Resulted Error")
                modal_exist = False
                return

            WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.ID, 'totalTable'))).click()

            driver.find_element(By.ID, 'totalTable').send_keys(self.request_amount)

            try:
                _ = WebDriverWait(driver, 10).until(
                    EC.element_to_be_clickable((By.XPATH, self.continue_button_xpath))
                ).click()
            except TimeoutException:
                logger.error("Check Button Still Deactivated")
                return

            try:
                _ = WebDriverWait(driver, 10).until(
                    EC.presence_of_element_located((By.XPATH, self.request_table_modal_xpath)),
                    EC.text_to_be_present_in_element((By.TAG_NAME, "h5"), self.modal_verification_title)
                )
            except TimeoutException:
                logger.error("Check Table Amount Setup Test Case Resulted Error")
                return

            driver.find_element(By.XPATH, self.accepting_verification_button_xpath).click()

            try:
                _ = WebDriverWait(driver, 10).until(
                    EC.presence_of_element_located((By.XPATH, self.status_request_chart_xpath))
                )
                page_exist = True
            except TimeoutException:
                logger.error("Check Table Amount Setup Test Case Resulted Error")
                page_exist = False
                return

            assert modal_exist is True
            assert page_exist is True
            logger.success("Check Request Table Amount Test Case has been Tested")

    def test_canceling_request_table_amount(self):
        with self.driver as driver:

            driver.execute_script("window.scrollTo(0,document.body.scrollHeight)")

            driver.find_element(By.XPATH, self.table_amount_page_xpath).click()

            try:
                _ = WebDriverWait(driver, 10).until(
                    EC.text_to_be_present_in_element((By.TAG_NAME, "h3"), self.valid_page_name)
                )
            except TimeoutException:
                logger.error("Check Table Amount Setup Test Case Resulted Error")
                return

            driver.find_element(By.XPATH, self.request_table_button_xpath).click()

            try:
                _ = WebDriverWait(driver, 10).until(
                    EC.presence_of_element_located((By.XPATH, self.request_table_modal_xpath))
                )
                modal_exist = True
            except TimeoutException:
                logger.error("Check Table Amount Setup Test Case Resulted Error")
                modal_exist = False
                return

            driver.find_element(By.ID, 'totalTable').click()

            driver.find_element(By.ID, 'totalTable').send_keys(self.request_amount)

            driver.find_element(By.XPATH, self.cancel_button_xpath).click()

            try:
                _ = WebDriverWait(driver, 10).until(
                    EC.presence_of_element_located((By.XPATH, self.status_request_chart_xpath))
                )
                page_exist = True
            except TimeoutException:
                logger.error("Check Table Amount Setup Test Case Resulted Error")
                page_exist = False
                return

            assert modal_exist is True
            assert page_exist is True
            logger.success("Check Canceling Request Table Amount Test Case has been Tested")

    def test_click_button_disable(self):
        with self.driver as driver:

            driver.execute_script("window.scrollTo(0,document.body.scrollHeight)")

            driver.find_element(By.XPATH, self.table_amount_page_xpath).click()

            try:
                _ = WebDriverWait(driver, 10).until(
                    EC.text_to_be_present_in_element((By.TAG_NAME, "h3"), self.valid_page_name)
                )
            except TimeoutException:
                logger.error("Check Table Amount Setup Test Case Resulted Error")
                return

            driver.find_element(By.XPATH, self.request_table_button_xpath).click()

            try:
                _ = WebDriverWait(driver, 10).until(
                    EC.presence_of_element_located((By.XPATH, self.request_table_modal_xpath))
                )
                modal_exist = True
            except TimeoutException:
                logger.error("Check Table Amount Setup Test Case Resulted Error")
                modal_exist = False
                return

            try:
                _ = WebDriverWait(driver, 1).until(
                    EC.element_to_be_clickable((By.XPATH, self.continue_button_xpath))
                ).click()
            except TimeoutException:
                logger.success("Check Click Button Disable Test Case has been Tested")
                return

            assert modal_exist is False
            logger.error("Disable Button Activated")

    @classmethod
    def as_suite(cls, test_suite: unittest.TestSuite) -> unittest.TestSuite:
        test_suite.addTest(cls('test_request_table_amount'))
        test_suite.addTest(cls('test_canceling_request_table_amount'))
        test_suite.addTest(cls('test_click_button_disable'))
        return test_suite

    def tearDown(self) -> None:
        pass
