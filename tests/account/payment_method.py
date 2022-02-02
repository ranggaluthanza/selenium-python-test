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

class PaymentMethodSettingsTest(unittest.TestCase):
    def setUp(self) -> None:
        load_dotenv()
        warnings.filterwarnings("ignore", category=DeprecationWarning)

        self.driver = LoginDriver().driver

        #data
        self.payment_method_title_page = 'Atur Metode Pembayaran'
        self.payment_method_qris = 'QRIS'
        self.payment_method_debit = 'Debit'
        self.payment_method_cash = 'Cash'

        #Xpath
        self.account_settings_xpath = '//*[@id="root"]/div[2]/div[2]/div[13]/div[2]/div'
        self.payment_method_page_xpath = '//*[@id="root"]/div[2]/div[2]/div[14]/div[5]/div[2]/a'
        self.payment_method_full_table = '//*[@id="root"]/div[2]/div[3]/div/div/div[2]/div[2]'
        self.manual_table_payment_method_xpath = '//*[@id="root"]/div[2]/div[3]/div/div/div[2]/div[2]/div[2]/div[2]'
        self.modal_confirmation_save_payment_method_xpath = '/html/body/div[3]/div[3]/div'

        #Button
        self.save_payment_method_xpath = '//*[@id="root"]/div[2]/div[3]/div/div/div[2]/div[2]/div[3]/button'
        self.button_modal_save_payment_method_xpath = '/html/body/div[3]/div[3]/div/div[3]/button[2]'

        #Toggle CSS
        self.active_toggle = 'MuiButtonBase-root MuiIconButton-root jss70 MuiSwitch-switchBase jss65 MuiSwitch-colorSecondary jss71 Mui-checked jss68'
        self.inactive_toggle = 'MuiButtonBase-root MuiIconButton-root jss70 MuiSwitch-switchBase jss65 MuiSwitch-colorSecondary'


    def test_activate_qris_payment_method(self):
        with self.driver as driver:

            driver.execute_script("window.scrollTo(0,document.body.scrollHeight)")

            driver.find_element(By.XPATH, self.payment_method_page_xpath).click()

            try:
                _ = WebDriverWait(driver, 10).until(
                    EC.text_to_be_present_in_element((By.TAG_NAME, "h3"), self.payment_method_title_page)
                )
            except TimeoutException:
                logger.error("Activate QRIS Payment Method Test Case Resulted Error")
                return

            try:
                _ = WebDriverWait(driver, 10).until(
                    EC.presence_of_element_located((By.XPATH, self.payment_method_full_table))
                )
            except TimeoutException:
                logger.error("Activate QRIS Payment Method Test Case Resulted Error")
                return

            try:
                _ = WebDriverWait(driver, 10).until(
                    EC.presence_of_element_located((By.XPATH, self.manual_table_payment_method_xpath))
                )
            except TimeoutException:
                logger.error("Activate QRIS Payment Method Test Case Resulted Error")
                return

            payment_method_elements = driver.find_elements(By.XPATH, self.manual_table_payment_method_xpath)
            for row_element in payment_method_elements:
                if row_element.find_element(By.TAG_NAME, 'h6').text == 'QRIS':
                    row_element.find_element(By.TAG_NAME, 'span').click()

            driver.find_element(By.XPATH, self.save_payment_method_xpath).click()
            time.sleep(3)

            try:
                _ = WebDriverWait(driver, 10).until(
                    EC.element_to_be_clickable((By.XPATH, self.button_modal_save_payment_method_xpath))
                ).click()
                activate_payment_method = True
            except TimeoutException:
                logger.error("Activate QRIS Payment Method Test Case Resulted Error")
                activate_payment_method = False
                return

            assert activate_payment_method is True
            logger.success("Activate QRIS Payment Method Test Case has been Tested")

    def test_inactivate_qris_payment_method(self):
        with self.driver as driver:

            driver.execute_script("window.scrollTo(0,document.body.scrollHeight)")

            driver.find_element(By.XPATH, self.payment_method_page_xpath).click()

            try:
                _ = WebDriverWait(driver, 10).until(
                    EC.text_to_be_present_in_element((By.TAG_NAME, "h3"), self.payment_method_title_page)
                )
            except TimeoutException:
                logger.error("Activate QRIS Payment Method Test Case Resulted Error")
                return

            try:
                _ = WebDriverWait(driver, 10).until(
                    EC.presence_of_element_located((By.XPATH, self.payment_method_full_table))
                )
            except TimeoutException:
                logger.error("Activate QRIS Payment Method Test Case Resulted Error")
                return

            try:
                _ = WebDriverWait(driver, 10).until(
                    EC.presence_of_element_located((By.XPATH, self.manual_table_payment_method_xpath))
                )
            except TimeoutException:
                logger.error("Activate QRIS Payment Method Test Case Resulted Error")
                return

            payment_method_elements = driver.find_elements(By.XPATH, self.manual_table_payment_method_xpath)
            for row_element in payment_method_elements:
                if row_element.find_element(By.TAG_NAME, 'h6').text == 'QRIS':
                    row_element.find_element(By.TAG_NAME, 'span').click()

            driver.find_element(By.XPATH, self.save_payment_method_xpath).click()
            time.sleep(3)

            try:
                _ = WebDriverWait(driver, 10).until(
                    EC.element_to_be_clickable((By.XPATH, self.button_modal_save_payment_method_xpath))
                ).click()
                inactivate_payment_method = True
            except TimeoutException:
                logger.error("Inactivate QRIS Payment Method Test Case Resulted Error")
                inactivate_payment_method = False
                return

            assert inactivate_payment_method is True
            logger.success("Inactivate QRIS Payment Method Test Case has been Tested")

    def test_activate_cash_payment_method(self):
        with self.driver as driver:
            driver.execute_script("window.scrollTo(0,document.body.scrollHeight)")

            driver.find_element(By.XPATH, self.payment_method_page_xpath).click()

            try:
                _ = WebDriverWait(driver, 10).until(
                    EC.text_to_be_present_in_element((By.TAG_NAME, "h3"), self.payment_method_title_page)
                )
            except TimeoutException:
                logger.error("Activate Cash Payment Method Test Case Resulted Error")
                return

            try:
                _ = WebDriverWait(driver, 10).until(
                    EC.presence_of_element_located((By.XPATH, self.payment_method_full_table))
                )
            except TimeoutException:
                logger.error("Activate Cash Payment Method Test Case Resulted Error")
                return

            payment_method_elements = driver.find_elements(By.XPATH, self.manual_table_payment_method_xpath)
            for row_element in payment_method_elements:
                if row_element.find_element(By.TAG_NAME, 'h6').text == "Cash":
                    row_element.find_element(By.TAG_NAME, 'span').click()

            driver.find_element(By.XPATH, self.save_payment_method_xpath).click()
            time.sleep(3)
            try:
                _ = WebDriverWait(driver, 10).until(
                    EC.element_to_be_clickable((By.XPATH, self.button_modal_save_payment_method_xpath))
                ).click()
                is_click = True
            except TimeoutException:
                logger.error("Activate Cash Payment Method Test Case Resulted Error")
                is_click = False
                return

                assert is_click is True
                logger.success("Activate Cash Payment Method Test Case has been Tested")

    def test_inactivate_cash_payment_method(self):
        with self.driver as driver:

            driver.execute_script("window.scrollTo(0,document.body.scrollHeight)")

            driver.find_element(By.XPATH, self.payment_method_page_xpath).click()

            try:
                _ = WebDriverWait(driver, 10).until(
                    EC.text_to_be_present_in_element((By.TAG_NAME, "h3"), self.payment_method_title_page)
                )
            except TimeoutException:
                logger.error("Inactivate Cash Payment Method Test Case Resulted Error")
                return

            try:
                _ = WebDriverWait(driver, 10).until(
                    EC.presence_of_element_located((By.XPATH, self.payment_method_full_table))
                )
            except TimeoutException:
                logger.error("Inactivate Cash Payment Method Test Case Resulted Error")
                return

            payment_method_elements = driver.find_elements(By.XPATH, self.manual_table_payment_method_xpath)
            for row_element in payment_method_elements:
                if row_element.find_element(By.TAG_NAME, 'h6').text == "Cash":
                    row_element.find_element(By.TAG_NAME, 'span').click()

            driver.find_element(By.XPATH, self.save_payment_method_xpath).click()
            time.sleep(3)

            try:
                _ = WebDriverWait(driver, 10).until(
                    EC.element_to_be_clickable((By.XPATH, self.button_modal_save_payment_method_xpath))
                ).click()
                is_click = True
            except TimeoutException:
                logger.error("Inactivate Cash Payment Method Test Case Resulted Error")
                is_click = False
                return

            assert is_click is True
            logger.success("Inactivate Cash Payment Method Test Case has been Tested")

    @classmethod
    def as_suite(cls, test_suite: unittest.TestSuite) -> unittest.TestSuite:
        test_suite.addTest(cls('test_activate_qris_payment_method'))
        test_suite.addTest(cls('test_inactivate_cash_payment_method'))
        test_suite.addTest(cls('test_activate_cash_payment_method'))
        test_suite.addTest(cls('test_inactivate_cash_payment_method'))
        return test_suite

    def tearDown(self) -> None:
        pass





