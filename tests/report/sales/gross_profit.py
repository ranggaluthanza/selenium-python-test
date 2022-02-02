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


class SalesReportGrossProfitTests(unittest.TestCase):
    def setUp(self) -> None:
        load_dotenv()
        warnings.filterwarnings("ignore", category=DeprecationWarning)

        self.driver = LoginDriver().driver

        # data
        self.valid_page_name = 'Sales'

        # Xpath
        self.gross_profit_chart_xpath = '/html/body/div[1]/div[2]/div[3]/div/div/div[2]/div[3]/div/div[2]'
        self.sales_page_xpath = '//*[@id="root"]/div[2]/div[2]/div[4]/div[1]/div[2]/a'
        self.gross_profit_page_xpath = '//div[@id="root"]/div[2]/div[3]/div/div/div[2]/div/div[2]/div/button[2]'

        self.calendar_button_xpath = '/html/body/div[1]/div[2]/div[3]/div/div/div[2]/div[3]/div/div[1]/div/button[2]'
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

    def test_check_report_gross_profit_today(self):
        with self.driver as driver:

            driver.find_element(By.XPATH, self.sales_page_xpath).click()

            try:
                _ = WebDriverWait(driver, 10).until(
                    EC.text_to_be_present_in_element((By.TAG_NAME, "h3"), self.valid_page_name)
                )
            except TimeoutException:
                logger.error("Check Gross Profit Test Case Resulted Error")
                return

            try:
                _ = WebDriverWait(driver, 10).until(
                    EC.element_to_be_clickable((By.XPATH, self.gross_profit_page_xpath))
                ).click()
            except TimeoutException:
                logger.error("Check Gross Profit Test Case Resulted Error")
                return

            try:
                _ = WebDriverWait(driver, 10).until(
                    EC.presence_of_element_located((By.XPATH, self.gross_profit_chart_xpath))
                )
            except TimeoutException:
                logger.error("Check Gross Profit Test Case Resulted Error")
                return

            driver.find_element(By.XPATH, self.calendar_button_xpath).click()

            try:
                _ = WebDriverWait(driver, 10).until(
                    EC.presence_of_element_located((By.ID, 'startDate')),
                    EC.presence_of_element_located((By.ID, 'endDate'))
                )
            except TimeoutException:
                logger.error("Check Gross Profit Test Case Resulted Error")
                return

            try:
                _ = WebDriverWait(driver, 10).until(
                    EC.element_to_be_clickable((By.XPATH, self.today_button_xpath))
                ).click()
            except TimeoutException:
                logger.error("Check Gross Profit Test Case Resulted Error")

            driver.find_element(By.XPATH, self.today_button_xpath).send_keys(Keys.ESCAPE)

            try:
                _ = WebDriverWait(driver, 10).until(
                    EC.presence_of_element_located((By.XPATH, self.gross_profit_chart_xpath))
                )
                page_exist = True
            except TimeoutException:
                logger.error("Check Gross Profit Test Case Resulted Error")
                page_exist = False
                return

            assert page_exist is True
            logger.success("Check Gross Profit Today Test Case has been Tested")

    def test_check_report_gross_profit_yesterday(self):
        with self.driver as driver:

            driver.find_element(By.XPATH, self.sales_page_xpath).click()

            try:
                _ = WebDriverWait(driver, 10).until(
                    EC.text_to_be_present_in_element((By.TAG_NAME, "h3"), self.valid_page_name)
                )
            except TimeoutException:
                logger.error("Check Gross Profit Test Case Resulted Error")
                return

            try:
                _ = WebDriverWait(driver, 10).until(
                    EC.element_to_be_clickable((By.XPATH, self.gross_profit_page_xpath))
                ).click()
            except TimeoutException:
                logger.error("Check Gross Profit Test Case Resulted Error")
                return

            try:
                _ = WebDriverWait(driver, 10).until(
                    EC.presence_of_element_located((By.XPATH, self.gross_profit_chart_xpath))
                )
            except TimeoutException:
                logger.error("Check Gross Profit Test Case Resulted Error")
                return

            driver.find_element(By.XPATH, self.calendar_button_xpath).click()

            try:
                _ = WebDriverWait(driver, 10).until(
                    EC.presence_of_element_located((By.ID, 'startDate')),
                    EC.presence_of_element_located((By.ID, 'endDate'))
                )
            except TimeoutException:
                logger.error("Check Gross Profit Test Case Resulted Error")
                return

            try:
                _ = WebDriverWait(driver, 10).until(
                    EC.element_to_be_clickable((By.XPATH, self.yesterday_button_xpath))
                ).click()
            except TimeoutException:
                logger.error("Check Gross Profit Test Case Resulted Error")

            driver.find_element(By.XPATH, self.yesterday_button_xpath).send_keys(Keys.ESCAPE)

            try:
                _ = WebDriverWait(driver, 10).until(
                    EC.presence_of_element_located((By.XPATH, self.gross_profit_chart_xpath))
                )
                page_exist = True
            except TimeoutException:
                logger.error("Check Gross Profit Test Case Resulted Error")
                page_exist = False
                return

            assert page_exist is True
            logger.success("Check Gross Profit Yesterday Test Case has been Tested")

    def test_check_report_gross_profit_this_week(self):
        with self.driver as driver:

            driver.find_element(By.XPATH, self.sales_page_xpath).click()

            try:
                _ = WebDriverWait(driver, 10).until(
                    EC.text_to_be_present_in_element((By.TAG_NAME, "h3"), self.valid_page_name)
                )
            except TimeoutException:
                logger.error("Check Gross Profit Test Case Resulted Error")
                return

            try:
                _ = WebDriverWait(driver, 10).until(
                    EC.element_to_be_clickable((By.XPATH, self.gross_profit_page_xpath))
                ).click()
            except TimeoutException:
                logger.error("Check Gross Profit Test Case Resulted Error")
                return

            try:
                _ = WebDriverWait(driver, 10).until(
                    EC.presence_of_element_located((By.XPATH, self.gross_profit_chart_xpath))
                )
            except TimeoutException:
                logger.error("Check Gross Profit Test Case Resulted Error")
                return

            driver.find_element(By.XPATH, self.calendar_button_xpath).click()

            try:
                _ = WebDriverWait(driver, 10).until(
                    EC.presence_of_element_located((By.ID, 'startDate')),
                    EC.presence_of_element_located((By.ID, 'endDate'))
                )
            except TimeoutException:
                logger.error("Check Gross Profit Test Case Resulted Error")
                return

            try:
                _ = WebDriverWait(driver, 10).until(
                    EC.element_to_be_clickable((By.XPATH, self.this_week_button_xpath))
                ).click()
            except TimeoutException:
                logger.error("Check Gross Profit Test Case Resulted Error")

            driver.find_element(By.XPATH, self.this_week_button_xpath).send_keys(Keys.ESCAPE)

            try:
                _ = WebDriverWait(driver, 10).until(
                    EC.presence_of_element_located((By.XPATH, self.gross_profit_chart_xpath))
                )
                page_exist = True
            except TimeoutException:
                logger.error("Check Gross Profit Test Case Resulted Error")
                page_exist = False
                return

            assert page_exist is True
            logger.success("Check Gross Profit This Week Test Case has been Tested")

    def test_check_report_gross_profit_last_week(self):
        with self.driver as driver:

            driver.find_element(By.XPATH, self.sales_page_xpath).click()

            try:
                _ = WebDriverWait(driver, 10).until(
                    EC.text_to_be_present_in_element((By.TAG_NAME, "h3"), self.valid_page_name)
                )
            except TimeoutException:
                logger.error("Check Gross Profit Test Case Resulted Error")
                return

            try:
                _ = WebDriverWait(driver, 10).until(
                    EC.element_to_be_clickable((By.XPATH, self.gross_profit_page_xpath))
                ).click()
            except TimeoutException:
                logger.error("Check Gross Profit Test Case Resulted Error")
                return

            try:
                _ = WebDriverWait(driver, 10).until(
                    EC.presence_of_element_located((By.XPATH, self.gross_profit_chart_xpath))
                )
            except TimeoutException:
                logger.error("Check Gross Profit Test Case Resulted Error")
                return

            driver.find_element(By.XPATH, self.calendar_button_xpath).click()

            try:
                _ = WebDriverWait(driver, 10).until(
                    EC.presence_of_element_located((By.ID, 'startDate')),
                    EC.presence_of_element_located((By.ID, 'endDate'))
                )
            except TimeoutException:
                logger.error("Check Gross Profit Test Case Resulted Error")
                return

            try:
                _ = WebDriverWait(driver, 10).until(
                    EC.element_to_be_clickable((By.XPATH, self.last_week_button_xpath))
                ).click()
            except TimeoutException:
                logger.error("Check Gross Profit Test Case Resulted Error")

            driver.find_element(By.XPATH, self.last_week_button_xpath).send_keys(Keys.ESCAPE)

            try:
                _ = WebDriverWait(driver, 10).until(
                    EC.presence_of_element_located((By.XPATH, self.gross_profit_chart_xpath))
                )
                page_exist = True
            except TimeoutException:
                logger.error("Check Gross Profit Test Case Resulted Error")
                page_exist = False
                return

            assert page_exist is True
            logger.success("Check Gross Profit Last Week Test Case has been Tested")

    def test_check_report_gross_profit_this_month(self):
        with self.driver as driver:

            driver.find_element(By.XPATH, self.sales_page_xpath).click()

            try:
                _ = WebDriverWait(driver, 10).until(
                    EC.text_to_be_present_in_element((By.TAG_NAME, "h3"), self.valid_page_name)
                )
            except TimeoutException:
                logger.error("Check Gross Profit Test Case Resulted Error")
                return

            try:
                _ = WebDriverWait(driver, 10).until(
                    EC.element_to_be_clickable((By.XPATH, self.gross_profit_page_xpath))
                ).click()
            except TimeoutException:
                logger.error("Check Gross Profit Test Case Resulted Error")
                return

            try:
                _ = WebDriverWait(driver, 10).until(
                    EC.presence_of_element_located((By.XPATH, self.gross_profit_chart_xpath))
                )
            except TimeoutException:
                logger.error("Check Gross Profit Test Case Resulted Error")
                return

            driver.find_element(By.XPATH, self.calendar_button_xpath).click()

            try:
                _ = WebDriverWait(driver, 10).until(
                    EC.presence_of_element_located((By.ID, 'startDate')),
                    EC.presence_of_element_located((By.ID, 'endDate'))
                )
            except TimeoutException:
                logger.error("Check Gross Profit Test Case Resulted Error")
                return

            try:
                _ = WebDriverWait(driver, 10).until(
                    EC.element_to_be_clickable((By.XPATH, self.this_month_button_xpath))
                ).click()
            except TimeoutException:
                logger.error("Check Gross Profit Test Case Resulted Error")

            driver.find_element(By.XPATH, self.this_month_button_xpath).send_keys(Keys.ESCAPE)

            try:
                _ = WebDriverWait(driver, 10).until(
                    EC.presence_of_element_located((By.XPATH, self.gross_profit_chart_xpath))
                )
                page_exist = True
            except TimeoutException:
                logger.error("Check Gross Profit Test Case Resulted Error")
                page_exist = False
                return

            assert page_exist is True
            logger.success("Check Gross Profit This Month Test Case has been Tested")

    def test_check_report_gross_profit_last_month(self):
        with self.driver as driver:

            driver.find_element(By.XPATH, self.sales_page_xpath).click()

            try:
                _ = WebDriverWait(driver, 10).until(
                    EC.text_to_be_present_in_element((By.TAG_NAME, "h3"), self.valid_page_name)
                )
            except TimeoutException:
                logger.error("Check Gross Profit Test Case Resulted Error")
                return

            try:
                _ = WebDriverWait(driver, 10).until(
                    EC.element_to_be_clickable((By.XPATH, self.gross_profit_page_xpath))
                ).click()
            except TimeoutException:
                logger.error("Check Gross Profit Test Case Resulted Error")
                return

            try:
                _ = WebDriverWait(driver, 10).until(
                    EC.presence_of_element_located((By.XPATH, self.gross_profit_chart_xpath))
                )
            except TimeoutException:
                logger.error("Check Gross Profit Test Case Resulted Error")
                return

            driver.find_element(By.XPATH, self.calendar_button_xpath).click()

            try:
                _ = WebDriverWait(driver, 10).until(
                    EC.presence_of_element_located((By.ID, 'startDate')),
                    EC.presence_of_element_located((By.ID, 'endDate'))
                )
            except TimeoutException:
                logger.error("Check Gross Profit Test Case Resulted Error")
                return

            try:
                _ = WebDriverWait(driver, 10).until(
                    EC.element_to_be_clickable((By.XPATH, self.last_month_button_xpath))
                ).click()
            except TimeoutException:
                logger.error("Check Gross Profit Test Case Resulted Error")

            driver.find_element(By.XPATH, self.last_month_button_xpath).send_keys(Keys.ESCAPE)

            try:
                _ = WebDriverWait(driver, 10).until(
                    EC.presence_of_element_located((By.XPATH, self.gross_profit_chart_xpath))
                )
                page_exist = True
            except TimeoutException:
                logger.error("Check Gross Profit Test Case Resulted Error")
                page_exist = False
                return

            assert page_exist is True
            logger.success("Check Gross Profit Last Month Test Case has been Tested")

    def test_check_report_gross_profit_this_year(self):
        with self.driver as driver:

            driver.find_element(By.XPATH, self.sales_page_xpath).click()

            try:
                _ = WebDriverWait(driver, 10).until(
                    EC.text_to_be_present_in_element((By.TAG_NAME, "h3"), self.valid_page_name)
                )
            except TimeoutException:
                logger.error("Check Gross Profit Test Case Resulted Error")
                return

            try:
                _ = WebDriverWait(driver, 10).until(
                    EC.element_to_be_clickable((By.XPATH, self.gross_profit_page_xpath))
                ).click()
            except TimeoutException:
                logger.error("Check Gross Profit Test Case Resulted Error")
                return

            try:
                _ = WebDriverWait(driver, 10).until(
                    EC.presence_of_element_located((By.XPATH, self.gross_profit_chart_xpath))
                )
            except TimeoutException:
                logger.error("Check Gross Profit Test Case Resulted Error")
                return

            driver.find_element(By.XPATH, self.calendar_button_xpath).click()

            try:
                _ = WebDriverWait(driver, 10).until(
                    EC.presence_of_element_located((By.ID, 'startDate')),
                    EC.presence_of_element_located((By.ID, 'endDate'))
                )
            except TimeoutException:
                logger.error("Check Gross Profit Test Case Resulted Error")
                return

            try:
                _ = WebDriverWait(driver, 10).until(
                    EC.element_to_be_clickable((By.XPATH, self.this_year_button_xpath))
                ).click()
            except TimeoutException:
                logger.error("Check Gross Profit Test Case Resulted Error")

            driver.find_element(By.XPATH, self.this_year_button_xpath).send_keys(Keys.ESCAPE)

            try:
                _ = WebDriverWait(driver, 10).until(
                    EC.presence_of_element_located((By.XPATH, self.gross_profit_chart_xpath))
                )
                page_exist = True
            except TimeoutException:
                logger.error("Check Gross Profit Test Case Resulted Error")
                page_exist = False
                return

            assert page_exist is True
            logger.success("Check Gross Profit This Year Test Case has been Tested")

    def test_check_report_gross_profit_last_year(self):
        with self.driver as driver:

            driver.find_element(By.XPATH, self.sales_page_xpath).click()

            try:
                _ = WebDriverWait(driver, 10).until(
                    EC.text_to_be_present_in_element((By.TAG_NAME, "h3"), self.valid_page_name)
                )
            except TimeoutException:
                logger.error("Check Gross Profit Test Case Resulted Error")
                return

            try:
                _ = WebDriverWait(driver, 10).until(
                    EC.element_to_be_clickable((By.XPATH, self.gross_profit_page_xpath))
                ).click()
            except TimeoutException:
                logger.error("Check Gross Profit Test Case Resulted Error")
                return

            try:
                _ = WebDriverWait(driver, 10).until(
                    EC.presence_of_element_located((By.XPATH, self.gross_profit_chart_xpath))
                )
            except TimeoutException:
                logger.error("Check Gross Profit Test Case Resulted Error")
                return

            driver.find_element(By.XPATH, self.calendar_button_xpath).click()

            try:
                _ = WebDriverWait(driver, 10).until(
                    EC.presence_of_element_located((By.ID, 'startDate')),
                    EC.presence_of_element_located((By.ID, 'endDate'))
                )
            except TimeoutException:
                logger.error("Check Gross Profit Test Case Resulted Error")
                return

            try:
                _ = WebDriverWait(driver, 10).until(
                    EC.element_to_be_clickable((By.XPATH, self.last_year_button_xpath))
                ).click()
            except TimeoutException:
                logger.error("Check Gross Profit Test Case Resulted Error")

            driver.find_element(By.XPATH, self.last_year_button_xpath).send_keys(Keys.ESCAPE)

            try:
                _ = WebDriverWait(driver, 10).until(
                    EC.presence_of_element_located((By.XPATH, self.gross_profit_chart_xpath))
                )
                page_exist = True
            except TimeoutException:
                logger.error("Check Gross Profit Test Case Resulted Error")
                page_exist = False
                return

            assert page_exist is True
            logger.success("Check Gross Profit Last Year Test Case has been Tested")

    @classmethod
    def as_suite(cls, test_suite: unittest.TestSuite) -> unittest.TestSuite:
        test_suite.addTest(cls('test_check_report_gross_profit_today'))
        test_suite.addTest(cls('test_check_report_gross_profit_yesterday'))
        test_suite.addTest(cls('test_check_report_gross_profit_this_week'))
        test_suite.addTest(cls('test_check_report_gross_profit_last_week'))
        test_suite.addTest(cls('test_check_report_gross_profit_this_month'))
        test_suite.addTest(cls('test_check_report_gross_profit_last_month'))
        test_suite.addTest(cls('test_check_report_gross_profit_this_year'))
        test_suite.addTest(cls('test_check_report_gross_profit_last_year'))
        return test_suite

    def tearDown(self) -> None:
        pass
