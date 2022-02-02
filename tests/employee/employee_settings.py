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


class EmployeeSettingTests(unittest.TestCase):
    def setUp(self) -> None:
        load_dotenv()
        warnings.filterwarnings("ignore", category=DeprecationWarning)

        self.driver = LoginDriver().driver

        # data
        fake = Faker('id-ID')

        self.valid_page_name = 'Karyawan'
        self.valid_merchant_name = 'Samsan Tech Restoran!!'
        self.valid_recruit_employee_name = 'Selenium'
        self.valid_recruit_employee_email = 'seleniumflick@mailnesia.com'
        self.valid_recruit_employee_number = 87741331517
        self.employee_name = 'Agus Harry'
        self.employee_position = 'Finance'

        self.invalid_phone_number = fake.language_name()
        self.invalid_email = fake.name()

        # Xpath
        self.set_employee_page_xpath = '//*[@id="root"]/div[2]/div[2]/div[10]/div[2]/div[2]'
        self.employee_chart_xpath = '/html/body/div[1]/div[2]/div[3]/div/div[2]/div[3]/div/div[2]'
        self.table_row_xpath = '//*[@id="root"]/div[2]/div[3]/div/div[2]/div[3]/div/div[2]/div'
        self.position_row_xpath = '/html/body/div[3]/div[3]/ul'
        self.modal_confirmation_xpath = '/html/body/div[4]/div[3]/div'
        self.field_recruit_employee_xpath = '//*[@id="recruitmentForm"]/div[3]/div/div/div'
        self.recruit_position_employee = '/html/body/div[4]/div[3]/ul'

        self.button_accept_xpath = '/html/body/div[4]/div[3]/div/div[3]/button[2]'
        self.button_decline_xpath = '/html/body/div[4]/div[3]/div/div[3]/button[1]'
        self.button_recruit_employee_xpath = '//*[@id="root"]/div[2]/div[3]/div/div[2]/div[2]/button'
        self.button_save_recruit_xpath = '//*[@id="root"]/div[2]/div[3]/div/div[1]/div[2]/div[1]/button[2]'

        # etc
        self.context = {}

    def test_set_position_to_employee(self):
        with self.driver as driver:

            # scroll down until element clicked
            driver.execute_script("window.scrollTo(0,document.body.scrollHeight)")

            driver.find_element(By.XPATH, self.set_employee_page_xpath).click()

            try:
                _ = WebDriverWait(driver, 10).until(
                    EC.text_to_be_present_in_element((By.TAG_NAME, "h3"), self.valid_page_name)
                )
            except TimeoutException:
                logger.error("Set Employee Position Test Case Resulted Error")
                return

            try:
                _ = WebDriverWait(driver, 10).until(
                    EC.presence_of_element_located((By.XPATH, self.employee_chart_xpath))
                )
                chart_exist = True
            except TimeoutException:
                logger.error("Set Employee Position Test Case Resulted Error")
                chart_exist = False
                return

            table_row_elements = driver.find_elements(By.XPATH, self.table_row_xpath)
            for row_element in table_row_elements:
                if row_element.find_element(By.TAG_NAME, 'strong').text == self.employee_name:
                    row_element.find_element(By.TAG_NAME, 'button').click()

            table_row_elements = driver.find_element(By.XPATH, self.position_row_xpath)
            for row_element in table_row_elements.find_elements(By.TAG_NAME, 'li'):
                if row_element.text == self.employee_position:
                    row_element.click()

            try:
                _ = WebDriverWait(driver, 10).until(
                    EC.presence_of_element_located((By.XPATH, self.modal_confirmation_xpath))
                )
            except TimeoutException:
                logger.error("Set Employee Position Test Case Resulted Error")
                return

            try:
                _ = WebDriverWait(driver, 10).until(
                    EC.element_to_be_clickable((By.XPATH, self.button_accept_xpath))
                ).click()
            except TimeoutException:
                logger.error("Set Employee Position Test Case Resulted Error")
                return

            assert chart_exist is True
            logger.success("Set Employee Position Test Case has been Tested")

    def test_canceling_set_position_to_employee(self):
        with self.driver as driver:

            # scroll down until element clicked
            driver.execute_script("window.scrollTo(0,document.body.scrollHeight)")

            driver.find_element(By.XPATH, self.set_employee_page_xpath).click()

            try:
                _ = WebDriverWait(driver, 10).until(
                    EC.text_to_be_present_in_element((By.TAG_NAME, "h3"), self.valid_page_name)
                )
            except TimeoutException:
                logger.error("Set Employee Position Test Case Resulted Error")
                return

            try:
                _ = WebDriverWait(driver, 10).until(
                    EC.presence_of_element_located((By.XPATH, self.employee_chart_xpath))
                )
                chart_exist = True
            except TimeoutException:
                logger.error("Set Employee Position Test Case Resulted Error")
                chart_exist = False
                return

            table_row_elements = driver.find_elements(By.XPATH, self.table_row_xpath)
            for row_element in table_row_elements:
                if row_element.find_element(By.TAG_NAME, 'strong').text == self.employee_name:
                    row_element.find_element(By.TAG_NAME, 'button').click()

            table_row_elements = driver.find_element(By.XPATH, self.position_row_xpath)
            for row_element in table_row_elements.find_elements(By.TAG_NAME, 'li'):
                if row_element.text == self.employee_position:
                    row_element.click()

            try:
                _ = WebDriverWait(driver, 10).until(
                    EC.presence_of_element_located((By.XPATH, self.modal_confirmation_xpath))
                )
            except TimeoutException:
                logger.error("Set Employee Position Test Case Resulted Error")
                return

            try:
                _ = WebDriverWait(driver, 10).until(
                    EC.element_to_be_clickable((By.XPATH, self.button_decline_xpath))
                ).click()
            except TimeoutException:
                logger.error("Set Employee Position Test Case Resulted Error")
                return

            assert chart_exist is True
            logger.success("Canceling Set Employee Position Test Case has been Tested")

    def test_recruit_employee_with_all_valid_data(self):
        with self.driver as driver:
            driver.execute_script("window.scrollTo(0,document.body.scrollHeight)")

            driver.find_element(By.XPATH, self.set_employee_page_xpath).click()

            try:
                _ = WebDriverWait(driver, 10).until(
                    EC.text_to_be_present_in_element((By.TAG_NAME, "h3"), self.valid_page_name)
                )
            except TimeoutException:
                logger.error("Recruit Employee Position Test Case Resulted Error")
                return

            try:
                _ = WebDriverWait(driver, 10).until(
                    EC.presence_of_element_located((By.XPATH, self.employee_chart_xpath))
                )
                chart_exist = True
            except TimeoutException:
                logger.error("Recruit Employee Position Test Case Resulted Error")
                chart_exist = False
                return

            try:
                _ = WebDriverWait(driver, 10).until(
                    EC.element_to_be_clickable((By.XPATH, self.button_recruit_employee_xpath))
                ).click()
            except TimeoutException:
                logger.error("Recruit Employee Position Test Case Resulted Error")
                return

            driver.find_element(By.ID, 'name').send_keys(self.valid_recruit_employee_name)
            driver.find_element(By.ID, 'email').send_keys(self.valid_recruit_employee_email)
            driver.find_element(By.ID, 'phoneNumber').send_keys(self.valid_recruit_employee_number)

            try:
                _ = WebDriverWait(driver, 10).until(
                    EC.element_to_be_clickable((By.XPATH, self.field_recruit_employee_xpath))
                ).click()
            except TimeoutException:
                logger.error("Recruit Employee Position Test Case Resulted Error")
                return

            table_row_elements = driver.find_element(By.XPATH, self.recruit_position_employee)
            for row_element in table_row_elements.find_elements(By.TAG_NAME, 'li'):
                if row_element.text == self.employee_position:
                    row_element.click()

            try:
                _ = WebDriverWait(driver, 10).until(
                    EC.element_to_be_clickable((By.XPATH, self.button_save_recruit_xpath))
                ).click()
            except TimeoutException:
                logger.error("Recruit Employee Position Test Case Resulted Error")
                return

            assert chart_exist is True
            logger.success("Recruit Employee Position with All Valid Data Test Case has been Tested")

    def test_recruit_employee_with_empty_data(self):
        with self.driver as driver:
            driver.execute_script("window.scrollTo(0,document.body.scrollHeight)")

            driver.find_element(By.XPATH, self.set_employee_page_xpath).click()

            try:
                _ = WebDriverWait(driver, 10).until(
                    EC.text_to_be_present_in_element((By.TAG_NAME, "h3"), self.valid_page_name)
                )
            except TimeoutException:
                logger.error("Recruit Employee Position Test Case Resulted Error")
                return

            try:
                _ = WebDriverWait(driver, 10).until(
                    EC.presence_of_element_located((By.XPATH, self.employee_chart_xpath))
                )
                chart_exist = True
            except TimeoutException:
                logger.error("Recruit Employee Position Test Case Resulted Error")
                chart_exist = False
                return

            try:
                _ = WebDriverWait(driver, 10).until(
                    EC.element_to_be_clickable((By.XPATH, self.button_recruit_employee_xpath))
                ).click()
            except TimeoutException:
                logger.error("Recruit Employee Position Test Case Resulted Error")
                return

            try:
                _ = WebDriverWait(driver, 10).until(
                    EC.element_to_be_clickable((By.XPATH, self.button_save_recruit_xpath))
                ).click()
            except TimeoutException:
                logger.error("Recruit Employee Position Test Case Resulted Error")
                return

            assert chart_exist is True
            logger.success("Recruit Employee Position with Empty Data Test Case has been Tested")

    def test_recruit_employee_with_invalid_format_phone_number(self):
        with self.driver as driver:
            driver.execute_script("window.scrollTo(0,document.body.scrollHeight)")

            driver.find_element(By.XPATH, self.set_employee_page_xpath).click()

            try:
                _ = WebDriverWait(driver, 10).until(
                    EC.text_to_be_present_in_element((By.TAG_NAME, "h3"), self.valid_page_name)
                )
            except TimeoutException:
                logger.error("Recruit Employee Position Test Case Resulted Error")
                return

            try:
                _ = WebDriverWait(driver, 10).until(
                    EC.presence_of_element_located((By.XPATH, self.employee_chart_xpath))
                )
                chart_exist = True
            except TimeoutException:
                logger.error("Recruit Employee Position Test Case Resulted Error")
                chart_exist = False
                return

            try:
                _ = WebDriverWait(driver, 10).until(
                    EC.element_to_be_clickable((By.XPATH, self.button_recruit_employee_xpath))
                ).click()
            except TimeoutException:
                logger.error("Recruit Employee Position Test Case Resulted Error")
                return

            driver.find_element(By.ID, 'name').send_keys(self.valid_recruit_employee_name)
            driver.find_element(By.ID, 'email').send_keys(self.valid_recruit_employee_email)
            driver.find_element(By.ID, 'phoneNumber').send_keys(self.invalid_phone_number)

            try:
                _ = WebDriverWait(driver, 10).until(
                    EC.element_to_be_clickable((By.XPATH, self.field_recruit_employee_xpath))
                ).click()
            except TimeoutException:
                logger.error("Recruit Employee Position Test Case Resulted Error")
                return

            table_row_elements = driver.find_element(By.XPATH, self.recruit_position_employee)
            for row_element in table_row_elements.find_elements(By.TAG_NAME, 'li'):
                if row_element.text == self.employee_position:
                    row_element.click()

            try:
                _ = WebDriverWait(driver, 10).until(
                    EC.element_to_be_clickable((By.XPATH, self.button_save_recruit_xpath))
                ).click()
            except TimeoutException:
                logger.error("Recruit Employee Position Test Case Resulted Error")
                return

            assert chart_exist is True
            logger.success("Recruit Set Employee Position with Invalid Format Phone Number Test Case has been Tested")

    def test_recruit_employee_when_position_is_empty(self):
        with self.driver as driver:
            driver.execute_script("window.scrollTo(0,document.body.scrollHeight)")

            driver.find_element(By.XPATH, self.set_employee_page_xpath).click()

            try:
                _ = WebDriverWait(driver, 10).until(
                    EC.text_to_be_present_in_element((By.TAG_NAME, "h3"), self.valid_page_name)
                )
            except TimeoutException:
                logger.error("Recruit Employee Position Test Case Resulted Error")
                return

            try:
                _ = WebDriverWait(driver, 10).until(
                    EC.presence_of_element_located((By.XPATH, self.employee_chart_xpath))
                )
                chart_exist = True
            except TimeoutException:
                logger.error("Recruit Employee Position Test Case Resulted Error")
                chart_exist = False
                return

            try:
                _ = WebDriverWait(driver, 10).until(
                    EC.element_to_be_clickable((By.XPATH, self.button_recruit_employee_xpath))
                ).click()
            except TimeoutException:
                logger.error("Recruit Employee Position Test Case Resulted Error")
                return

            driver.find_element(By.ID, 'name').send_keys('Selenium')
            driver.find_element(By.ID, 'email').send_keys('seleniumflick@mailnesia.com')
            driver.find_element(By.ID, 'phoneNumber').send_keys(87741331517)

            try:
                _ = WebDriverWait(driver, 10).until(
                    EC.element_to_be_clickable((By.XPATH, self.button_save_recruit_xpath))
                ).click()
            except TimeoutException:
                logger.error("Recruit Employee Position Test Case Resulted Error")
                return

            assert chart_exist is True
            logger.success("Recruit Set Employee Position when Position is Empty Test Case has been Tested")

    def test_recruit_employee_with_invalid_format_email(self):
        with self.driver as driver:
            driver.execute_script("window.scrollTo(0,document.body.scrollHeight)")

            driver.find_element(By.XPATH, self.set_employee_page_xpath).click()

            try:
                _ = WebDriverWait(driver, 10).until(
                    EC.text_to_be_present_in_element((By.TAG_NAME, "h3"), self.valid_page_name)
                )
            except TimeoutException:
                logger.error("Recruit Employee Position Test Case Resulted Error")
                return

            try:
                _ = WebDriverWait(driver, 10).until(
                    EC.presence_of_element_located((By.XPATH, self.employee_chart_xpath))
                )
                chart_exist = True
            except TimeoutException:
                logger.error("Recruit Employee Position Test Case Resulted Error")
                chart_exist = False
                return

            try:
                _ = WebDriverWait(driver, 10).until(
                    EC.element_to_be_clickable((By.XPATH, self.button_recruit_employee_xpath))
                ).click()
            except TimeoutException:
                logger.error("Recruit Employee Position Test Case Resulted Error")
                return

            driver.find_element(By.ID, 'name').send_keys(self.valid_recruit_employee_name)
            driver.find_element(By.ID, 'email').send_keys(self.invalid_email)
            driver.find_element(By.ID, 'phoneNumber').send_keys(self.valid_recruit_employee_number)

            try:
                _ = WebDriverWait(driver, 10).until(
                    EC.element_to_be_clickable((By.XPATH, self.field_recruit_employee_xpath))
                ).click()
            except TimeoutException:
                logger.error("Recruit Employee Position Test Case Resulted Error")
                return

            table_row_elements = driver.find_element(By.XPATH, self.recruit_position_employee)
            for row_element in table_row_elements.find_elements(By.TAG_NAME, 'li'):
                if row_element.text == self.employee_position:
                    row_element.click()

            try:
                _ = WebDriverWait(driver, 10).until(
                    EC.element_to_be_clickable((By.XPATH, self.button_save_recruit_xpath))
                ).click()
            except TimeoutException:
                logger.error("Recruit Employee Position Test Case Resulted Error")
                return

            assert chart_exist is True
            logger.success("Recruit Set Employee Position with Invalid Format Email Test Case has been Tested")

    @classmethod
    def as_suite(cls, test_suite: unittest.TestSuite) -> unittest.TestSuite:
        test_suite.addTest(cls('test_recruit_employee_with_all_valid_data'))
        test_suite.addTest(cls('test_recruit_employee_when_position_is_empty'))
        test_suite.addTest(cls('test_set_position_to_employee'))
        test_suite.addTest(cls('test_canceling_set_position_to_employee'))
        test_suite.addTest(cls('test_recruit_employee_with_empty_data'))
        test_suite.addTest(cls('test_recruit_employee_with_invalid_format_phone_number'))
        test_suite.addTest(cls('test_recruit_employee_with_invalid_format_email'))
        return test_suite

    def tearDown(self) -> None:
        pass