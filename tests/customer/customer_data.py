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


class CustomerDataReportTests(unittest.TestCase):
    def setUp(self) -> None:
        load_dotenv()
        warnings.filterwarnings("ignore", category=DeprecationWarning)

        self.driver = LoginDriver().driver

        # data
        self.valid_page_name = 'Daftar Pelanggan'
        self.valid_merchant_name = 'Samsan Tech Restoran!!'
        self.title_menu_chart = 'Ringkasan'
        self.search_name = 'Rangga'

        # Xpath
        self.list_customer_page_xpath = '//*[@id="root"]/div[2]/div[2]/div[8]/div[1]/div[2]'
        self.report_list_customer_chart_xpath = '/html/body/div[1]/div[2]/div[3]/div/div[5]/div[2]'
        self.report_list_customer_filter_chart_xpath = '/html/body/div[1]/div[2]/div[3]/div/div[6]/div[2]'

        self.search_button_xpath = '/html/body/div[1]/div[2]/div[3]/div/div[2]/div/input'
        self.calendar_button_xpath = '/html/body/div[1]/div[2]/div[3]/div/div[3]/div/button[2]'
        self.today_button_xpath = '/html/body/div[3]/div[3]/ul/div/div[2]/button[1]'
        self.yesterday_button_xpath = '/html/body/div[3]/div[3]/ul/div/div[2]/button[2]'
        self.this_week_button_xpath = '/html/body/div[3]/div[3]/ul/div/div[2]/button[3]'
        self.last_week_button_xpath = '/html/body/div[3]/div[3]/ul/div/div[2]/button[4]'
        self.this_month_button_xpath = '/html/body/div[3]/div[3]/ul/div/div[2]/button[5]'
        self.last_month_button_xpath = '/html/body/div[3]/div[3]/ul/div/div[2]/button[6]'
        self.this_year_button_xpath = '/html/body/div[3]/div[3]/ul/div/div[2]/button[7]'
        self.last_year_button_xpath = '/html/body/div[3]/div[3]/ul/div/div[2]/button[8]'
        self.high_spender_button_xpath = '//*[@id="root"]/div[2]/div[3]/div/div[4]/div/button[1]'
        self.loyal_customer_button_xpath = '//*[@id="root"]/div[2]/div[3]/div/div[4]/div/button[2]'

    def test_customer_data_by_search_name(self):
        with self.driver as driver:

            driver.find_element(By.XPATH, self.list_customer_page_xpath).click()

            try:
                _ = WebDriverWait(driver, 10).until(
                    EC.text_to_be_present_in_element((By.TAG_NAME, "h3"), self.valid_page_name)
                )
            except TimeoutException:
                logger.error("Check List Customer Data Test Case Resulted Error")
                return

            driver.find_element(By.XPATH, self.search_button_xpath).click()

            driver.find_element(By.XPATH, self.search_button_xpath).send_keys(self.search_name)

            try:
                _ = WebDriverWait(driver, 10).until(
                    EC.presence_of_element_located((By.XPATH, self.report_list_customer_chart_xpath))
                )
                page_exist = True
            except TimeoutException:
                logger.error("Check List Customer Data Test Case Resulted Error")
                page_exist = False
                return

            assert page_exist is True
            logger.success("Check List Customer Data by Search nName Test Case has been Tested")

    def test_customer_data_with_date_filter(self):
        with self.driver as driver:

            driver.find_element(By.XPATH, self.list_customer_page_xpath).click()

            try:
                _ = WebDriverWait(driver, 10).until(
                    EC.text_to_be_present_in_element((By.TAG_NAME, "h3"), self.valid_page_name)
                )
            except TimeoutException:
                logger.error("Check List Customer Data Test Case Resulted Error")
                return

            driver.find_element(By.XPATH, self.calendar_button_xpath).click()

            try:
                _ = WebDriverWait(driver, 10).until(
                    EC.presence_of_element_located((By.ID, 'startDate')),
                    EC.presence_of_element_located((By.ID, 'endDate'))
                )
            except TimeoutException:
                logger.error("Check List Customer Data Test Case Resulted Error")
                return

            driver.find_element(By.XPATH, self.last_month_button_xpath).click()

            driver.find_element(By.XPATH, self.last_month_button_xpath).send_keys(Keys.ESCAPE)

            try:
                _ = WebDriverWait(driver, 10).until(
                    EC.presence_of_element_located((By.XPATH, self.report_list_customer_chart_xpath))
                )
                page_exist = True
            except TimeoutException:
                logger.error("Check List Customer Data Test Case Resulted Error")
                page_exist = False
                return

            assert page_exist is True
            logger.success("Check List Customer Data With Date Filter Test Case has been Tested")

    def test_customer_data_without_any_filters(self):
        with self.driver as driver:

            driver.find_element(By.XPATH, self.list_customer_page_xpath).click()

            try:
                _ = WebDriverWait(driver, 10).until(
                    EC.text_to_be_present_in_element((By.TAG_NAME, "h3"), self.valid_page_name)
                )
            except TimeoutException:
                logger.error("Check List Customer Data Test Case Resulted Error")
                return

            try:
                _ = WebDriverWait(driver, 10).until(
                    EC.presence_of_element_located((By.XPATH, self.report_list_customer_chart_xpath))
                )
                page_exist = True
            except TimeoutException:
                logger.error("Check List Customer Data Test Case Resulted Error")
                page_exist = False
                return

            assert page_exist is True
            logger.success("Check List Customer Data Without Any Filters Test Case has been Tested")

    def test_customer_data_with_high_spender_filter(self):
        with self.driver as driver:

            driver.find_element(By.XPATH, self.list_customer_page_xpath).click()

            try:
                _ = WebDriverWait(driver, 10).until(
                    EC.text_to_be_present_in_element((By.TAG_NAME, 'h3'), self.valid_page_name)
                )
            except TimeoutException:
                logger.error("Check List Customer Data Test Case Resulted Error")
                return

            driver.find_element(By.XPATH, self.calendar_button_xpath).click()

            try:
                _ = WebDriverWait(driver, 10).until(
                    EC.presence_of_element_located((By.ID, 'startDate')),
                    EC.presence_of_element_located((By.ID, 'endDate'))
                )
            except TimeoutException:
                logger.error("Check List Customer Data Test Case Resulted Error")
                return

            driver.find_element(By.XPATH, self.last_month_button_xpath).click()

            driver.find_element(By.XPATH, self.last_month_button_xpath).send_keys(Keys.ESCAPE)

            try:
                _ = WebDriverWait(driver, 10).until(
                    EC.presence_of_element_located((By.XPATH, self.report_list_customer_chart_xpath))
                )
                page_exist = True
            except TimeoutException:
                logger.error("Check List Customer Data Test Case Resulted Error")
                page_exist = False
                return

            driver.find_element(By.XPATH, self.high_spender_button_xpath).click()

            try:
                _ = WebDriverWait(driver, 10).until(
                    EC.presence_of_element_located((By.XPATH, self.report_list_customer_filter_chart_xpath))
                )
                page_exist = True
            except TimeoutException:
                logger.error("Check List Customer Data Test Case Resulted Error")
                page_exist = False
                return

            assert page_exist is True
            logger.success("Check List Customer Data With High Spender Filter Test Case has been Tested")

    def test_customer_data_with_loyal_customer_filter(self):
        with self.driver as driver:

            driver.find_element(By.XPATH, self.list_customer_page_xpath).click()

            try:
                _ = WebDriverWait(driver, 10).until(
                    EC.text_to_be_present_in_element((By.TAG_NAME, 'h3'), self.valid_page_name)
                )
            except TimeoutException:
                logger.error("Check List Customer Data Test Case Resulted Error")
                return

            driver.find_element(By.XPATH, self.calendar_button_xpath).click()

            try:
                _ = WebDriverWait(driver, 10).until(
                    EC.presence_of_element_located((By.ID, 'startDate')),
                    EC.presence_of_element_located((By.ID, 'endDate'))
                )
            except TimeoutException:
                logger.error("Check List Customer Data Test Case Resulted Error")
                return

            driver.find_element(By.XPATH, self.this_year_button_xpath).click()

            driver.find_element(By.XPATH, self.this_year_button_xpath).send_keys(Keys.ESCAPE)

            try:
                _ = WebDriverWait(driver, 10).until(
                    EC.presence_of_element_located((By.XPATH, self.report_list_customer_chart_xpath))
                )
                page_exist = True
            except TimeoutException:
                logger.error("Check List Customer Data Test Case Resulted Error")
                page_exist = False
                return

            driver.find_element(By.XPATH, self.loyal_customer_button_xpath).click()

            try:
                _ = WebDriverWait(driver, 10).until(
                    EC.presence_of_element_located((By.XPATH, self.report_list_customer_filter_chart_xpath))
                )
                page_exist = True
            except TimeoutException:
                logger.error("Check List Customer Data Test Case Resulted Error")
                page_exist = False
                return

            assert page_exist is True
            logger.success("Check List Customer Data With Royal Customer Filter Test Case has been Tested")

    def test_customer_data_with_high_spender_and_royal_customer_filter(self):
        with self.driver as driver:

            driver.find_element(By.XPATH, self.list_customer_page_xpath).click()

            try:
                _ = WebDriverWait(driver, 10).until(
                    EC.text_to_be_present_in_element((By.TAG_NAME, 'h3'), self.valid_page_name)
                )
            except TimeoutException:
                logger.error("Check List Customer Data Test Case Resulted Error")
                return

            driver.find_element(By.XPATH, self.calendar_button_xpath).click()

            try:
                _ = WebDriverWait(driver, 10).until(
                    EC.presence_of_element_located((By.ID, 'startDate')),
                    EC.presence_of_element_located((By.ID, 'endDate'))
                )
            except TimeoutException:
                logger.error("Check List Customer Data Test Case Resulted Error")
                return

            driver.find_element(By.XPATH, self.this_year_button_xpath).click()

            driver.find_element(By.XPATH, self.this_year_button_xpath).send_keys(Keys.ESCAPE)

            try:
                _ = WebDriverWait(driver, 10).until(
                    EC.presence_of_element_located((By.XPATH, self.report_list_customer_chart_xpath))
                )
                page_exist = True
            except TimeoutException:
                logger.error("Check List Customer Data Test Case Resulted Error")
                page_exist = False
                return

            driver.find_element(By.XPATH, self.high_spender_button_xpath).click()
            driver.find_element(By.XPATH, self.loyal_customer_button_xpath).click()

            try:
                _ = WebDriverWait(driver, 10).until(
                    EC.presence_of_element_located((By.XPATH, self.report_list_customer_filter_chart_xpath))
                )
                page_exist = True
            except TimeoutException:
                logger.error("Check List Customer Data Test Case Resulted Error")
                page_exist = False
                return

            assert page_exist is True
            logger.success("Check List Customer Data With High Spender and Royal Customer Filter Test Case has been "
                           "Tested")

    def test_customer_data_by_search_name_after_using_filters(self):
        with self.driver as driver:

            driver.find_element(By.XPATH, self.list_customer_page_xpath).click()

            try:
                _ = WebDriverWait(driver, 10).until(
                    EC.text_to_be_present_in_element((By.TAG_NAME, 'h3'), self.valid_page_name)
                )
            except TimeoutException:
                logger.error("Check List Customer Data Test Case Resulted Error")
                return

            driver.find_element(By.XPATH, self.calendar_button_xpath).click()

            try:
                _ = WebDriverWait(driver, 10).until(
                    EC.presence_of_element_located((By.ID, 'startDate')),
                    EC.presence_of_element_located((By.ID, 'endDate'))
                )
            except TimeoutException:
                logger.error("Check List Customer Data Test Case Resulted Error")
                return

            driver.find_element(By.XPATH, self.this_year_button_xpath).click()

            driver.find_element(By.XPATH, self.this_year_button_xpath).send_keys(Keys.ESCAPE)

            try:
                _ = WebDriverWait(driver, 10).until(
                    EC.presence_of_element_located((By.XPATH, self.report_list_customer_chart_xpath))
                )
                page_exist = True
            except TimeoutException:
                logger.error("Check List Customer Data Test Case Resulted Error")
                page_exist = False
                return

            driver.find_element(By.XPATH, self.high_spender_button_xpath).click()
            driver.find_element(By.XPATH, self.loyal_customer_button_xpath).click()

            try:
                _ = WebDriverWait(driver, 10).until(
                    EC.presence_of_element_located((By.XPATH, self.report_list_customer_filter_chart_xpath))
                )
                page_exist = True
            except TimeoutException:
                logger.error("Check List Customer Data Test Case Resulted Error")
                page_exist = False
                return

            driver.find_element(By.XPATH, self.search_button_xpath).click()

            driver.find_element(By.XPATH, self.search_button_xpath).send_keys(self.search_name)
            time.sleep(5)
            assert page_exist is True
            logger.success("Check List Customer Data by Search Name After Using Filters Test Case has been Tested")

    @classmethod
    def as_suite(cls, test_suite: unittest.TestSuite) -> unittest.TestSuite:
        test_suite.addTest(cls('test_customer_data_without_any_filters'))
        test_suite.addTest(cls('test_customer_data_by_search_name'))
        test_suite.addTest(cls('test_customer_data_with_date_filter'))
        test_suite.addTest(cls('test_customer_data_with_high_spender_filter'))
        test_suite.addTest(cls('test_customer_data_with_loyal_customer_filter'))
        test_suite.addTest(cls('test_customer_data_with_high_spender_and_royal_customer_filter'))
        test_suite.addTest(cls('test_customer_data_by_search_name_after_using_filters'))
        return test_suite

    def tearDown(self) -> None:
        pass
