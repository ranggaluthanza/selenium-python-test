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


class BankAccountTests(unittest.TestCase):
    def setUp(self) -> None:
        load_dotenv()
        warnings.filterwarnings("ignore", category=DeprecationWarning)

        self.driver = LoginDriver().driver

        # data
        self.valid_page_name = 'Rekening Bank'
        self.valid_bank_name = 'BNI (Bank Negara Indonesia) dan BNI Syariah'
        self.valid_account_holder_name = 'Rangga Luthanza'
        self.valid_pin = 123456
        self.valid_account_bank_number = '0774689929'

        # Xpath
        self.bank_account_page_xpath = '//*[@id="root"]/div[2]/div[2]/div[14]/div[3]/div[2]'
        self.modal_confirmation_delete_account_xpath = '/html/body/div[3]/div[3]/div'
        self.field_bank_name_xpath = '//*[@id="bankCode"]'
        self.list_of_bank_name_xpath = '//*[@id="menu-"]/div[3]/ul'
        self.modal_adding_bank_account_xpath = '//*[@id="root"]/div[2]/div[3]/div/div/div[2]/div[1]/div[2]'
        self.auto_debt_chart_xpath = '//*[@id="root"]/div[2]/div[3]/div/div/div[2]/div[3]/div/div[1]'

        self.button_delete_account_confirmation_xpath = '/html/body/div[3]/div[3]/div/div[3]/button[2]'
        self.button_cancel_account_confirmation_xpath = '/html/body/div[3]/div[3]/div/div[3]/button[1]'
        self.button_adding_bank_account_xpath = '//*[@id="root"]/div[2]/div[3]/div/div/div[2]/div[2]/button'
        self.button_save_adding_bank_account_xpath = '//*[@id="root"]/div[2]/div[3]/div/div/div[2]/div[1]/div[2]/div[3]/button'
        self.button_delete_bank_account_xpath = '//*[@id="root"]/div[2]/div[3]/div/div/div[2]/div[2]/div/div[1]/button'

        # etc
        self.context = {}

    def test_adding_bank_account(self):
        with self.driver as driver:

            driver.execute_script("window.scrollTo(0,document.body.scrollHeight)")

            try:
                _ = WebDriverWait(driver, 10).until(
                    EC.element_to_be_clickable((By.XPATH, self.bank_account_page_xpath))
                ).click()
            except TimeoutException:
                logger.error("Check Bank Account Test Case Resulted Error")

            try:
                _ = WebDriverWait(driver, 10).until(
                    EC.text_to_be_present_in_element((By.TAG_NAME, "h3"), self.valid_page_name)
                )
            except TimeoutException:
                logger.error("Change Bank Account Test Case Resulted Error")
                return

            try:
                _ = WebDriverWait(driver, 10).until(
                    EC.element_to_be_clickable((By.XPATH, self.button_adding_bank_account_xpath))
                ).click()
            except TimeoutException:
                logger.error("Check Bank Account Test Case Resulted Error")
                return

            try:
                _ = WebDriverWait(driver, 10).until(
                    EC.presence_of_element_located((By.XPATH, self.modal_adding_bank_account_xpath))
                )
                modal_exist = True
            except TimeoutException:
                logger.error("Check Bank Account Test Case Resulted Error")
                modal_exist = False
                return

            try:
                _ = WebDriverWait(driver, 10).until(
                    EC.element_to_be_clickable((By.XPATH, self.field_bank_name_xpath))
                ).click()
            except TimeoutException:
                logger.error("Check Bank Account Test Case Resulted Error")
                return

            table_row_elements = driver.find_element(By.XPATH, self.list_of_bank_name_xpath)
            for row_element in table_row_elements.find_elements(By.TAG_NAME, 'li'):
                if row_element.text == self.valid_bank_name:
                    row_element.click()
                    break

            driver.find_element(By.ID, 'accountNumber').send_keys(self.valid_account_bank_number)
            driver.find_element(By.ID, 'accountHolderName').send_keys(self.valid_account_holder_name)

            try:
                _ = WebDriverWait(driver, 10).until(
                    EC.element_to_be_clickable((By.XPATH, self.button_save_adding_bank_account_xpath))
                ).click()
            except TimeoutException:
                logger.error("Check Bank Account Test Case Resulted Error")
                return

            assert modal_exist is True
            logger.success("Adding Bank Account Test Case has been Tested")

    def test_change_bank_account(self):
        with self.driver as driver:

            driver.execute_script("window.scrollTo(0,document.body.scrollHeight)")

            try:
                _ = WebDriverWait(driver, 10).until(
                    EC.element_to_be_clickable((By.XPATH, self.bank_account_page_xpath))
                ).click()
            except TimeoutException:
                logger.error("Check Bank Account Test Case Resulted Error")

            try:
                _ = WebDriverWait(driver, 10).until(
                    EC.text_to_be_present_in_element((By.TAG_NAME, "h3"), self.valid_page_name)
                )
            except TimeoutException:
                logger.error("Change Bank Account Test Case Resulted Error")
                return

            try:
                _ = WebDriverWait(driver, 10).until(
                    EC.element_to_be_clickable((By.XPATH, self.button_delete_bank_account_xpath))
                ).click()
            except TimeoutException:
                logger.error("Check Bank Account Test Case Resulted Error")
                return

            try:
                _ = WebDriverWait(driver, 10).until(
                    EC.presence_of_element_located((By.XPATH, self.modal_confirmation_delete_account_xpath))
                )
                modal_exist = True
            except TimeoutException:
                logger.error("Check Bank Account Test Case Resulted Error")
                modal_exist = False
                return

            driver.find_element(By.ID, 'pin').send_keys(self.valid_pin)

            try:
                _ = WebDriverWait(driver, 10).until(
                    EC.element_to_be_clickable((By.XPATH, self.button_delete_account_confirmation_xpath))
                ).click()
            except TimeoutException:
                logger.error("Check Bank Account Test Case Resulted Error")
                return

            try:
                _ = WebDriverWait(driver, 10).until(
                    EC.element_to_be_clickable((By.XPATH, self.button_adding_bank_account_xpath))
                ).click()
            except TimeoutException:
                logger.error("Check Bank Account Test Case Resulted Error")
                return

            try:
                _ = WebDriverWait(driver, 10).until(
                    EC.presence_of_element_located((By.XPATH, self.modal_adding_bank_account_xpath))
                )
                modal_exist = True
            except TimeoutException:
                logger.error("Check Bank Account Test Case Resulted Error")
                modal_exist = False
                return

            try:
                _ = WebDriverWait(driver, 10).until(
                    EC.element_to_be_clickable((By.XPATH, self.field_bank_name_xpath))
                ).click()
            except TimeoutException:
                logger.error("Check Bank Account Test Case Resulted Error")
                return

            table_row_elements = driver.find_element(By.XPATH, self.list_of_bank_name_xpath)
            for row_element in table_row_elements.find_elements(By.TAG_NAME, 'li'):
                if row_element.text == self.valid_bank_name:
                    row_element.click()
                    break

            driver.find_element(By.ID, 'accountNumber').send_keys(self.valid_account_bank_number)
            driver.find_element(By.ID, 'accountHolderName').send_keys(self.valid_account_holder_name)

            try:
                _ = WebDriverWait(driver, 10).until(
                    EC.element_to_be_clickable((By.XPATH, self.button_save_adding_bank_account_xpath))
                ).click()
            except TimeoutException:
                logger.error("Check Bank Account Test Case Resulted Error")
                return

            assert modal_exist is True
            logger.success("Change Bank Account Test Case has been Tested")

    def test_canceling_change_bank_account(self):
        with self.driver as driver:

            driver.execute_script("window.scrollTo(0,document.body.scrollHeight)")

            try:
                _ = WebDriverWait(driver, 10).until(
                    EC.element_to_be_clickable((By.XPATH, self.bank_account_page_xpath))
                ).click()
            except TimeoutException:
                logger.error("Check Bank Account Test Case Resulted Error")

            try:
                _ = WebDriverWait(driver, 10).until(
                    EC.text_to_be_present_in_element((By.TAG_NAME, "h3"), self.valid_page_name)
                )
            except TimeoutException:
                logger.error("Change Bank Account Test Case Resulted Error")
                return

            try:
                _ = WebDriverWait(driver, 10).until(
                    EC.element_to_be_clickable((By.XPATH, self.button_delete_bank_account_xpath))
                ).click()
            except TimeoutException:
                logger.error("Check Bank Account Test Case Resulted Error")
                return

            try:
                _ = WebDriverWait(driver, 10).until(
                    EC.presence_of_element_located((By.XPATH, self.modal_confirmation_delete_account_xpath))
                )
                modal_exist = True
            except TimeoutException:
                logger.error("Check Bank Account Test Case Resulted Error")
                modal_exist = False
                return

            driver.find_element(By.ID, 'pin').send_keys(self.valid_pin)

            try:
                _ = WebDriverWait(driver, 10).until(
                    EC.element_to_be_clickable((By.XPATH, self.button_cancel_account_confirmation_xpath))
                ).click()
            except TimeoutException:
                logger.error("Check Bank Account Test Case Resulted Error")
                return

            assert modal_exist is True
            logger.success("Canceling Change Bank Account Test Case has been Tested")

    def test_remove_bank_account(self):
        with self.driver as driver:

            driver.execute_script("window.scrollTo(0,document.body.scrollHeight)")

            try:
                _ = WebDriverWait(driver, 10).until(
                    EC.element_to_be_clickable((By.XPATH, self.bank_account_page_xpath))
                ).click()
            except TimeoutException:
                logger.error("Check Bank Account Test Case Resulted Error")

            try:
                _ = WebDriverWait(driver, 10).until(
                    EC.text_to_be_present_in_element((By.TAG_NAME, "h3"), self.valid_page_name)
                )
            except TimeoutException:
                logger.error("Change Bank Account Test Case Resulted Error")
                return

            try:
                _ = WebDriverWait(driver, 10).until(
                    EC.element_to_be_clickable((By.XPATH, self.button_delete_bank_account_xpath))
                ).click()
            except TimeoutException:
                logger.error("Check Bank Account Test Case Resulted Error")
                return

            try:
                _ = WebDriverWait(driver, 10).until(
                    EC.presence_of_element_located((By.XPATH, self.modal_confirmation_delete_account_xpath))
                )
                modal_exist = True
            except TimeoutException:
                logger.error("Check Bank Account Test Case Resulted Error")
                modal_exist = False
                return

            driver.find_element(By.ID, 'pin').send_keys(self.valid_pin)

            try:
                _ = WebDriverWait(driver, 10).until(
                    EC.element_to_be_clickable((By.XPATH, self.button_delete_account_confirmation_xpath))
                ).click()
            except TimeoutException:
                logger.error("Check Bank Account Test Case Resulted Error")
                return

            assert modal_exist is True
            logger.success("Remove Bank Account Test Case has been Tested")

    def test_activating_auto_debt(self):
        with self.driver as driver:

            driver.execute_script("window.scrollTo(0,document.body.scrollHeight)")

            try:
                _ = WebDriverWait(driver, 10).until(
                    EC.element_to_be_clickable((By.XPATH, self.bank_account_page_xpath))
                ).click()
            except TimeoutException:
                logger.error("Check Bank Account Test Case Resulted Error")

            try:
                _ = WebDriverWait(driver, 10).until(
                    EC.text_to_be_present_in_element((By.TAG_NAME, "h3"), self.valid_page_name)
                )
            except TimeoutException:
                logger.error("Change Bank Account Test Case Resulted Error")
                return

            auto_debt_chart = driver.find_elements(By.XPATH, self.auto_debt_chart_xpath)
            for status_auto_debt in auto_debt_chart:
                if status_auto_debt.find_element(By.TAG_NAME, 'strong').text == 'Tidak Aktif':
                    status_auto_debt.find_element(By.TAG_NAME, 'input').click()
                    break

            auto_debt_status_text = driver.find_element(By.XPATH, self.auto_debt_chart_xpath).text

            assert auto_debt_status_text == 'Aktif'
            logger.success("Activation Auto Debt Bank Account Test Case has been Tested")

    def test_deactivating_auto_debt(self):
        with self.driver as driver:

            driver.execute_script("window.scrollTo(0,document.body.scrollHeight)")

            try:
                _ = WebDriverWait(driver, 10).until(
                    EC.element_to_be_clickable((By.XPATH, self.bank_account_page_xpath))
                ).click()
            except TimeoutException:
                logger.error("Check Bank Account Test Case Resulted Error")

            try:
                _ = WebDriverWait(driver, 10).until(
                    EC.text_to_be_present_in_element((By.TAG_NAME, "h3"), self.valid_page_name)
                )
            except TimeoutException:
                logger.error("Change Bank Account Test Case Resulted Error")
                return

            auto_debt_chart = driver.find_elements(By.XPATH, self.auto_debt_chart_xpath)
            for status_auto_debt in auto_debt_chart:
                if status_auto_debt.find_element(By.TAG_NAME, 'strong').text == 'Aktif':
                    status_auto_debt.find_element(By.TAG_NAME, 'input').click()
                    break

            auto_debt_status_text = driver.find_element(By.XPATH, self.auto_debt_chart_xpath).text

            assert auto_debt_status_text == 'Tidak Aktif'
            logger.success("Deactivation Auto Debt Bank Account Test Case has been Tested")

    @classmethod
    def as_suite(cls, test_suite: unittest.TestSuite) -> unittest.TestSuite:
        test_suite.addTest(cls('test_remove_bank_account'))
        test_suite.addTest(cls('test_adding_bank_account'))
        test_suite.addTest(cls('test_change_bank_account'))
        test_suite.addTest(cls('test_cancelling_change_bank_account'))
        test_suite.addTest(cls('test_deactivating_auto_debt'))
        test_suite.addTest(cls('test_activating_auto_debt'))
        return test_suite

    def tearDown(self) -> None:
        pass
