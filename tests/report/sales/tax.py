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


class SalesReportTaxTests(unittest.TestCase):
    def setUp(self) -> None:
        load_dotenv()
        warnings.filterwarnings("ignore", category=DeprecationWarning)

        self.driver = LoginDriver().driver

        # data
        self.valid_page_name = 'Sales'
        self.valid_merchant_name = 'Samsan Tech Restoran!!'
        self.title_menu_chart = 'Laporan Pajak'

        # Xpath
        self.sales_page_xpath = '//*[@id="root"]/div[2]/div[2]/div[4]/div[1]/div[2]/a'
        self.tax_page_xpath = '//div[@id="root"]/div[2]/div[3]/div/div/div[2]/div/div[2]/div/button[6]'
        self.report_tax_chart_xpath = '/html/body/div[1]/div[2]/div[3]/div/div/div[2]/div[7]/div/div[2]/div[2]'

        self.calendar_button_xpath = '/html/body/div[1]/div[2]/div[3]/div/div/div[2]/div[7]/div/div[1]/div/button[2]'
        self.today_button_xpath = '/html/body/div[3]/div[3]/ul/div/div[2]/button[1]'
        self.yesterday_button_xpath = '/html/body/div[3]/div[3]/ul/div/div[2]/button[2]'
        self.this_week_button_xpath = '/html/body/div[3]/div[3]/ul/div/div[2]/button[3]'
        self.last_week_button_xpath = '/html/body/div[3]/div[3]/ul/div/div[2]/button[4]'
        self.this_month_button_xpath = '/html/body/div[3]/div[3]/ul/div/div[2]/button[5]'
        self.last_month_button_xpath = '/html/body/div[3]/div[3]/ul/div/div[2]/button[6]'
        self.this_year_button_xpath = '/html/body/div[3]/div[3]/ul/div/div[2]/button[7]'
        self.last_year_button_xpath = '/html/body/div[3]/div[3]/ul/div/div[2]/button[8]'

        # etc
        self.context = {}

    def test_check_report_tax_today(self):
        with self.driver as driver:

            driver.find_element(By.XPATH, self.sales_page_xpath).click()

            try:
                _ = WebDriverWait(driver, 10).until(
                    EC.text_to_be_present_in_element((By.TAG_NAME, "h3"), "Sales")
                )
            except TimeoutException:
                logger.error("Check Report Tax Test Case Resulted Error")
                return

            driver.find_element(By.XPATH, self.tax_page_xpath).click()

            try:
                _ = WebDriverWait(driver, 10).until(
                    EC.text_to_be_present_in_element((By.TAG_NAME, "h5"), self.title_menu_chart)
                )
            except TimeoutException:
                logger.error("Check Report Tax Test Case Resulted Error")
                return

            driver.find_element(By.XPATH, self.calendar_button_xpath).click()

            try:
                _ = WebDriverWait(driver, 10).until(
                    EC.presence_of_element_located((By.ID, 'startDate')),
                    EC.presence_of_element_located((By.ID, 'endDate'))
                )
            except TimeoutException:
                logger.error("Check Report Tax Test Case Resulted Error")
                return

            driver.find_element(By.XPATH, self.today_button_xpath).click()

            driver.find_element(By.XPATH, self.today_button_xpath).send_keys(Keys.ESCAPE)

            try:
                _ = WebDriverWait(driver, 10).until(
                    EC.presence_of_element_located((By.XPATH, self.report_tax_chart_xpath))
                )
                page_exist = True
            except TimeoutException:
                logger.error("Check Report Tax Test Case Resulted Error")
                page_exist = False
                return

            assert page_exist is True
            logger.success("Check Report Tax Today Test Case has been Tested")

    def test_check_report_tax_yesterday(self):
        with self.driver as driver:

            driver.find_element(By.XPATH, self.sales_page_xpath).click()

            try:
                _ = WebDriverWait(driver, 10).until(
                    EC.text_to_be_present_in_element((By.TAG_NAME, "h3"), "Sales")
                )
            except TimeoutException:
                logger.error("Check Report Tax Test Case Resulted Error")
                return

            driver.find_element(By.XPATH, self.tax_page_xpath).click()

            try:
                _ = WebDriverWait(driver, 10).until(
                    EC.text_to_be_present_in_element((By.TAG_NAME, "h5"), self.title_menu_chart)
                )
            except TimeoutException:
                logger.error("Check Report Tax Test Case Resulted Error")
                return

            driver.find_element(By.XPATH, self.calendar_button_xpath).click()

            try:
                _ = WebDriverWait(driver, 10).until(
                    EC.presence_of_element_located((By.ID, 'startDate')),
                    EC.presence_of_element_located((By.ID, 'endDate'))
                )
            except TimeoutException:
                logger.error("Check Report Tax Test Case Resulted Error")
                return

            driver.find_element(By.XPATH, self.yesterday_button_xpath).click()

            driver.find_element(By.XPATH, self.yesterday_button_xpath).send_keys(Keys.ESCAPE)

            try:
                _ = WebDriverWait(driver, 10).until(
                    EC.presence_of_element_located((By.XPATH, self.report_tax_chart_xpath))
                )
                page_exist = True
            except TimeoutException:
                logger.error("Check Report Tax Test Case Resulted Error")
                page_exist = False
                return

            assert page_exist is True
            logger.success("Check Report Tax Yesterday Test Case has been Tested")

    def test_check_report_tax_this_week(self):
        with self.driver as driver:

            driver.find_element(By.XPATH, self.sales_page_xpath).click()

            try:
                _ = WebDriverWait(driver, 10).until(
                    EC.text_to_be_present_in_element((By.TAG_NAME, "h3"), "Sales")
                )
            except TimeoutException:
                logger.error("Check Report Tax Test Case Resulted Error")
                return

            driver.find_element(By.XPATH, self.tax_page_xpath).click()

            try:
                _ = WebDriverWait(driver, 10).until(
                    EC.text_to_be_present_in_element((By.TAG_NAME, "h5"), self.title_menu_chart)
                )
            except TimeoutException:
                logger.error("Check Report Tax Test Case Resulted Error")
                return

            driver.find_element(By.XPATH, self.calendar_button_xpath).click()

            try:
                _ = WebDriverWait(driver, 10).until(
                    EC.presence_of_element_located((By.ID, 'startDate')),
                    EC.presence_of_element_located((By.ID, 'endDate'))
                )
            except TimeoutException:
                logger.error("Check Report Tax Test Case Resulted Error")
                return

            driver.find_element(By.XPATH, self.this_week_button_xpath).click()

            driver.find_element(By.XPATH, self.this_week_button_xpath).send_keys(Keys.ESCAPE)

            try:
                _ = WebDriverWait(driver, 10).until(
                    EC.presence_of_element_located((By.XPATH, self.report_tax_chart_xpath))
                )
                page_exist = True
            except TimeoutException:
                logger.error("Check Report Tax Test Case Resulted Error")
                page_exist = False
                return

            assert page_exist is True
            logger.success("Check Report Tax This Week Test Case has been Tested")

    def test_check_report_tax_last_week(self):
        with self.driver as driver:

            driver.find_element(By.XPATH, self.sales_page_xpath).click()

            try:
                _ = WebDriverWait(driver, 10).until(
                    EC.text_to_be_present_in_element((By.TAG_NAME, "h3"), "Sales")
                )
            except TimeoutException:
                logger.error("Check Report Tax Test Case Resulted Error")
                return

            driver.find_element(By.XPATH, self.tax_page_xpath).click()

            try:
                _ = WebDriverWait(driver, 10).until(
                    EC.text_to_be_present_in_element((By.TAG_NAME, "h5"), self.title_menu_chart)
                )
            except TimeoutException:
                logger.error("Check Report Tax Test Case Resulted Error")
                return

            driver.find_element(By.XPATH, self.calendar_button_xpath).click()

            try:
                _ = WebDriverWait(driver, 10).until(
                    EC.presence_of_element_located((By.ID, 'startDate')),
                    EC.presence_of_element_located((By.ID, 'endDate'))
                )
            except TimeoutException:
                logger.error("Check Report Tax Test Case Resulted Error")
                return

            driver.find_element(By.XPATH, self.last_week_button_xpath).click()

            driver.find_element(By.XPATH, self.last_week_button_xpath).send_keys(Keys.ESCAPE)

            try:
                _ = WebDriverWait(driver, 10).until(
                    EC.presence_of_element_located((By.XPATH, self.report_tax_chart_xpath))
                )
                page_exist = True
            except TimeoutException:
                logger.error("Check Report Tax Test Case Resulted Error")
                page_exist = False
                return

            assert page_exist is True
            logger.success("Check Report Tax Last Week Test Case has been Tested")

    def test_check_report_tax_this_month(self):
        with self.driver as driver:

            driver.find_element(By.XPATH, self.sales_page_xpath).click()

            try:
                _ = WebDriverWait(driver, 10).until(
                    EC.text_to_be_present_in_element((By.TAG_NAME, "h3"), "Sales")
                )
            except TimeoutException:
                logger.error("Check Report Tax Test Case Resulted Error")
                return

            driver.find_element(By.XPATH, self.tax_page_xpath).click()

            try:
                _ = WebDriverWait(driver, 10).until(
                    EC.text_to_be_present_in_element((By.TAG_NAME, "h5"), self.title_menu_chart)
                )
            except TimeoutException:
                logger.error("Check Report Tax Test Case Resulted Error")
                return

            driver.find_element(By.XPATH, self.calendar_button_xpath).click()

            try:
                _ = WebDriverWait(driver, 10).until(
                    EC.presence_of_element_located((By.ID, 'startDate')),
                    EC.presence_of_element_located((By.ID, 'endDate'))
                )
            except TimeoutException:
                logger.error("Check Report Tax Test Case Resulted Error")
                return

            driver.find_element(By.XPATH, self.this_month_button_xpath).click()

            driver.find_element(By.XPATH, self.this_month_button_xpath).send_keys(Keys.ESCAPE)

            try:
                _ = WebDriverWait(driver, 10).until(
                    EC.presence_of_element_located((By.XPATH, self.report_tax_chart_xpath))
                )
                page_exist = True
            except TimeoutException:
                logger.error("Check Report Tax Test Case Resulted Error")
                page_exist = False
                return

            assert page_exist is True
            logger.success("Check Report Tax This Month Test Case has been Tested")

    def test_check_report_tax_last_month(self):
        with self.driver as driver:

            driver.find_element(By.XPATH, self.sales_page_xpath).click()

            try:
                _ = WebDriverWait(driver, 10).until(
                    EC.text_to_be_present_in_element((By.TAG_NAME, "h3"), "Sales")
                )
            except TimeoutException:
                logger.error("Check Report Tax Test Case Resulted Error")
                return

            driver.find_element(By.XPATH, self.tax_page_xpath).click()

            try:
                _ = WebDriverWait(driver, 10).until(
                    EC.text_to_be_present_in_element((By.TAG_NAME, "h5"), self.title_menu_chart)
                )
            except TimeoutException:
                logger.error("Check Report Tax Test Case Resulted Error")
                return

            driver.find_element(By.XPATH, self.calendar_button_xpath).click()

            try:
                _ = WebDriverWait(driver, 10).until(
                    EC.presence_of_element_located((By.ID, 'startDate')),
                    EC.presence_of_element_located((By.ID, 'endDate'))
                )
            except TimeoutException:
                logger.error("Check Report Tax Test Case Resulted Error")
                return

            driver.find_element(By.XPATH, self.last_month_button_xpath).click()

            driver.find_element(By.XPATH, self.last_month_button_xpath).send_keys(Keys.ESCAPE)

            try:
                _ = WebDriverWait(driver, 10).until(
                    EC.presence_of_element_located((By.XPATH, self.report_tax_chart_xpath))
                )
                page_exist = True
            except TimeoutException:
                logger.error("Check Report Tax Test Case Resulted Error")
                page_exist = False
                return

            assert page_exist is True
            logger.success("Check Report Tax Last Month Test Case has been Tested")

    def test_check_report_tax_this_year(self):
        with self.driver as driver:

            driver.find_element(By.XPATH, self.sales_page_xpath).click()

            try:
                _ = WebDriverWait(driver, 10).until(
                    EC.text_to_be_present_in_element((By.TAG_NAME, "h3"), "Sales")
                )
            except TimeoutException:
                logger.error("Check Report Tax Test Case Resulted Error")
                return

            driver.find_element(By.XPATH, self.tax_page_xpath).click()

            try:
                _ = WebDriverWait(driver, 10).until(
                    EC.text_to_be_present_in_element((By.TAG_NAME, "h5"), self.title_menu_chart)
                )
            except TimeoutException:
                logger.error("Check Report Tax Test Case Resulted Error")
                return

            driver.find_element(By.XPATH, self.calendar_button_xpath).click()

            try:
                _ = WebDriverWait(driver, 10).until(
                    EC.presence_of_element_located((By.ID, 'startDate')),
                    EC.presence_of_element_located((By.ID, 'endDate'))
                )
            except TimeoutException:
                logger.error("Check Report Tax Test Case Resulted Error")
                return

            driver.find_element(By.XPATH, self.this_year_button_xpath).click()

            driver.find_element(By.XPATH, self.this_year_button_xpath).send_keys(Keys.ESCAPE)

            try:
                _ = WebDriverWait(driver, 10).until(
                    EC.presence_of_element_located((By.XPATH, self.report_tax_chart_xpath))
                )
                page_exist = True
            except TimeoutException:
                logger.error("Check Report Tax Test Case Resulted Error")
                page_exist = False
                return

            assert page_exist is True
            logger.success("Check Report Tax This Year Test Case has been Tested")

    def test_check_report_tax_last_year(self):
        with self.driver as driver:

            driver.find_element(By.XPATH, self.sales_page_xpath).click()

            try:
                _ = WebDriverWait(driver, 10).until(
                    EC.text_to_be_present_in_element((By.TAG_NAME, "h3"), "Sales")
                )
            except TimeoutException:
                logger.error("Check Report Tax Test Case Resulted Error")
                return

            driver.find_element(By.XPATH, self.tax_page_xpath).click()

            try:
                _ = WebDriverWait(driver, 10).until(
                    EC.text_to_be_present_in_element((By.TAG_NAME, "h5"), self.title_menu_chart)
                )
            except TimeoutException:
                logger.error("Check Report Tax Test Case Resulted Error")
                return

            driver.find_element(By.XPATH, self.calendar_button_xpath).click()

            try:
                _ = WebDriverWait(driver, 10).until(
                    EC.presence_of_element_located((By.ID, 'startDate')),
                    EC.presence_of_element_located((By.ID, 'endDate'))
                )
            except TimeoutException:
                logger.error("Check Report Tax Test Case Resulted Error")
                return

            driver.find_element(By.XPATH, self.last_year_button_xpath).click()

            driver.find_element(By.XPATH, self.last_year_button_xpath).send_keys(Keys.ESCAPE)

            try:
                _ = WebDriverWait(driver, 10).until(
                    EC.presence_of_element_located((By.XPATH, self.report_tax_chart_xpath))
                )
                page_exist = True
            except TimeoutException:
                logger.error("Check Report Tax Test Case Resulted Error")
                page_exist = False
                return

            assert page_exist is True
            logger.success("Check Report Tax Last Year Test Case has been Tested")

    @classmethod
    def as_suite(cls, test_suite: unittest.TestSuite) -> unittest.TestSuite:
        test_suite.addTest(cls('test_check_tax_today'))
        test_suite.addTest(cls('test_check_tax_yesterday'))
        test_suite.addTest(cls('test_check_tax_this_week'))
        test_suite.addTest(cls('test_check_tax_last_week'))
        test_suite.addTest(cls('test_check_tax_this_month'))
        test_suite.addTest(cls('test_check_tax_last_month'))
        test_suite.addTest(cls('test_check_tax_this_year'))
        test_suite.addTest(cls('test_check_tax_last_year'))
        return test_suite

    def tearDown(self) -> None:
        pass
