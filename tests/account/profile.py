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


class AccountSettingProfileTests(unittest.TestCase):
    def setUp(self) -> None:
        load_dotenv()
        warnings.filterwarnings("ignore", category=DeprecationWarning)

        self.driver = LoginDriver().driver

        # data
        self.valid_page_name = 'Profil'
        self.photo_file_locate = 'C:\\Users\\bmass\\Downloads\\FlickApp PlayStore.png'
        self.day_operational_hour = 'Rabu'

        self.valid_business_name = 'Samsan Tech Restoran!!'
        self.valid_owner_name ='Muhammad Rangga Luthanza'
        self.valid_email_business = 'samsantechrestoran@mailnesia.com'
        self.valid_address_business = 'Bintaro, Pesanggrahan Jakarta Selatan DKI Jakarta, 12330'

        # Xpath
        self.profile_page_xpath = '//*[@id="root"]/div[2]/div[2]/div[14]/div[1]/div[2]/a'
        self.upload_photo_xpath = '//*[@id="restaurant-photo-input"]'
        self.banner_profile_xpath = '//*[@id="root"]/div[2]/div[3]/div/div[2]/div[2]/div[1]/div'
        self.table_operational_hours_xpath = '//*[@id="root"]/div[2]/div[3]/div/div[2]/div[2]/div[2]/div[4]/div[2]'
        self.table_row_xpath = '//*[@id="root"]/div[2]/div[3]/div/div[2]/div[2]/div[2]/div[4]/div[2]/div'
        self.modal_operational_xpath = '//*[@id="root"]/div[2]/div[3]/div/div[2]/div[2]/div[2]/div[3]/div[2]'
        self.time_row_xpath = '/html/body/div[3]/div[3]/div/div[1]/div/div[2]/div/div/span'
        self.open_twenty_hour_xpath = '//*[@id="root"]/div[2]/div[3]/div/div[2]/div[2]/div[2]/div[3]/div[2]/div[2]/div/div[1]'
        self.closed_xpath = '//*[@id="root"]/div[2]/div[3]/div/div[2]/div[2]/div[2]/div[3]/div[2]/div[2]/div/div[2]'

        self.button_change_information_business = '/html/body/div[1]/div[2]/div[3]/div/div[2]/div[2]/div[2]/div[1]/div[1]/div[2]/button'
        self.button_save_xpath = '/html/body/div[1]/div[2]/div[3]/div/div[1]/div[2]/div[1]/button[2]'
        self.button_open_twenty_hour_xpath = '//*[@id="root"]/div[2]/div[3]/div/div[2]/div[2]/div[2]/div[3]/div[2]/div[2]/div/div[1]/div/span'
        self.button_closed_xpath = '//*[@id="root"]/div[2]/div[3]/div/div[2]/div[2]/div[2]/div[3]/div[2]/div[2]/div/div[2]/div/span'
        self.button_set_time_xpath = '//*[@id="root"]/div[2]/div[3]/div/div[2]/div[2]/div[2]/div[3]/div[2]/div[2]/div/div[3]/div[1]/span'
        self.button_save_operational_hour_xpath = '//*[@id="root"]/div[2]/div[3]/div/div[2]/div[2]/div[2]/div[3]/div[2]/div[1]/button[2]'

        # etc
        self.context = {}

    def test_change_profile_cover(self):
        with self.driver as driver:

            driver.execute_script("window.scrollTo(0,document.body.scrollHeight)")

            try:
                _ = WebDriverWait(driver, 10).until(
                    EC.element_to_be_clickable((By.XPATH, self.profile_page_xpath))
                ).click()
            except TimeoutException:
                logger.error("Change Account Setting Profile Test Case Resulted Error")

            try:
                _ = WebDriverWait(driver, 10).until(
                    EC.text_to_be_present_in_element((By.TAG_NAME, "h3"), self.valid_page_name)
                )
            except TimeoutException:
                logger.error("Change Account Setting Profile Test Case Resulted Error")
                return

            try:
                _ = WebDriverWait(driver, 10).until(
                    EC.presence_of_element_located((By.XPATH, self.banner_profile_xpath))
                )
                page_exist = True
            except TimeoutException:
                logger.error("Change Account Setting Profile Test Case Resulted Error")
                page_exist = False
                return

            driver.find_element(By.XPATH, self.upload_photo_xpath).send_keys(self.photo_file_locate)

            assert page_exist is True
            logger.success("Change Profile Cover Test Case has been Tested")

    def test_change_business_information(self):
        with self.driver as driver:

            driver.execute_script("window.scrollTo(0,document.body.scrollHeight)")

            try:
                _ = WebDriverWait(driver, 10).until(
                    EC.element_to_be_clickable((By.XPATH, self.profile_page_xpath))
                ).click()
            except TimeoutException:
                logger.error("Change Account Setting Profile Test Case Resulted Error")

            try:
                _ = WebDriverWait(driver, 10).until(
                    EC.text_to_be_present_in_element((By.TAG_NAME, "h3"), self.valid_page_name)
                )
            except TimeoutException:
                logger.error("Change Account Setting Profile Test Case Resulted Error")
                return

            try:
                _ = WebDriverWait(driver, 10).until(
                    EC.presence_of_element_located((By.XPATH, self.banner_profile_xpath))
                )
                page_exist = True
            except TimeoutException:
                logger.error("Change Account Setting Profile Test Case Resulted Error")
                page_exist = False
                return

            try:
                _ = WebDriverWait(driver, 10).until(
                    EC.element_to_be_clickable((By.XPATH, self.button_change_information_business))
                ).click()
            except TimeoutException:
                logger.error("Change Account Setting Profile Test Case Resulted Error")
                return

            try:
               _ = WebDriverWait(driver, 10).until(
                   EC.presence_of_element_located((By.ID, 'name'))
               )
            except TimeoutException:
                logger.error("Change Account Setting Profile Test Case Resulted Error")
                return

            driver.find_element(By.ID, "name").send_keys(Keys.CONTROL + "a")
            driver.find_element(By.ID, "name").send_keys(Keys.DELETE)
            driver.find_element(By.ID, "name").send_keys(self.valid_business_name)

            driver.find_element(By.ID, "ownerName").send_keys(Keys.CONTROL + "a")
            driver.find_element(By.ID, "ownerName").send_keys(Keys.DELETE)
            driver.find_element(By.ID, "ownerName").send_keys(self.valid_owner_name)

            driver.find_element(By.ID, "email").send_keys(Keys.CONTROL + "a")
            driver.find_element(By.ID, "email").send_keys(Keys.DELETE)
            driver.find_element(By.ID, "email").send_keys(self.valid_email_business)

            driver.find_element(By.ID, "address").send_keys(Keys.CONTROL + "a")
            driver.find_element(By.ID, "address").send_keys(Keys.DELETE)
            driver.find_element(By.ID, "address").send_keys(self.valid_address_business)

            try:
                _ = WebDriverWait(driver, 10).until(
                    EC.element_to_be_clickable((By.XPATH, self.button_save_xpath))
                ).click()
            except TimeoutException:
                logger.error("Change Account Setting Profile Test Case Resulted Error")
                return

            assert page_exist is True
            logger.success("Change Business Information Test Case has been Tested")

    def test_set_twenty_four_operational_hour(self):
        with self.driver as driver:

            driver.execute_script("window.scrollTo(0,document.body.scrollHeight)")

            try:
                _ = WebDriverWait(driver, 10).until(
                    EC.element_to_be_clickable((By.XPATH, self.profile_page_xpath))
                ).click()
            except TimeoutException:
                logger.error("Set Operational Hour Test Case Resulted Error")

            try:
                _ = WebDriverWait(driver, 10).until(
                    EC.text_to_be_present_in_element((By.TAG_NAME, "h3"), self.valid_page_name)
                )
            except TimeoutException:
                logger.error("Set Operational Hour Test Case Resulted Error")
                return

            try:
                _ = WebDriverWait(driver, 10).until(
                    EC.presence_of_element_located((By.XPATH, self.table_operational_hours_xpath))
                )
            except TimeoutException:
                logger.error("Set Operational Hour Test Case Resulted Error")
                return

            table_row_elements = driver.find_elements(By.XPATH, self.table_row_xpath)
            for row_element in table_row_elements:
                if row_element.find_element(By.TAG_NAME, 'span').text == self.day_operational_hour:
                    row_element.find_element(By.TAG_NAME, 'button').click()
                    break

            try:
                _ = WebDriverWait(driver, 10).until(
                    EC.presence_of_element_located((By.XPATH, self.modal_operational_xpath))
                )
                modal_exist = True
            except TimeoutException:
                logger.error("Set Operational Hour Test Case Resulted Error")
                modal_exist = False
                return

            try:
                _ = WebDriverWait(driver, 10).until(
                    EC.element_to_be_clickable((By.XPATH, self.button_open_twenty_hour_xpath))
                ).click()
            except TimeoutException:
                logger.error("Set Operational Hour Test Case Resulted Error")

            try:
                _ = WebDriverWait(driver, 10).until(
                    EC.element_to_be_clickable((By.XPATH, self.button_save_operational_hour_xpath))
                ).click()
            except TimeoutException:
                logger.error("Set Operational Hour Test Case Resulted Error")

            toggle_status = driver.find_element(By.XPATH, self.open_twenty_hour_xpath).get_attribute('data-active')

            assert modal_exist is True
            assert toggle_status == 'true'
            logger.success("Set Open 24 hour Operational Hour Test Case has been Tested")

    def test_set_closed_operational_hour(self):
        with self.driver as driver:

            driver.execute_script("window.scrollTo(0,document.body.scrollHeight)")

            try:
                _ = WebDriverWait(driver, 10).until(
                    EC.element_to_be_clickable((By.XPATH, self.profile_page_xpath))
                ).click()
            except TimeoutException:
                logger.error("Set Operational Hour Test Case Resulted Error")

            try:
                _ = WebDriverWait(driver, 10).until(
                    EC.text_to_be_present_in_element((By.TAG_NAME, "h3"), self.valid_page_name)
                )
            except TimeoutException:
                logger.error("Set Operational Hour Test Case Resulted Error")
                return

            try:
                _ = WebDriverWait(driver, 10).until(
                    EC.presence_of_element_located((By.XPATH, self.table_operational_hours_xpath))
                )
                modal_exist = True
            except TimeoutException:
                logger.error("Set Operational Hour Test Case Resulted Error")
                modal_exist = False
                return

            table_row_elements = driver.find_elements(By.XPATH, self.table_row_xpath)
            for row_element in table_row_elements:
                if row_element.find_element(By.TAG_NAME, 'span').text == self.day_operational_hour:
                    row_element.find_element(By.TAG_NAME, 'button').click()
                    break

            try:
                _ = WebDriverWait(driver, 10).until(
                    EC.presence_of_element_located((By.XPATH, self.modal_operational_xpath))
                )
            except TimeoutException:
                logger.error("Set Operational Hour Test Case Resulted Error")
                return

            try:
                _ = WebDriverWait(driver, 10).until(
                    EC.element_to_be_clickable((By.XPATH, self.button_closed_xpath))
                ).click()
            except TimeoutException:
                logger.error("Set Operational Hour Test Case Resulted Error")

            try:
                _ = WebDriverWait(driver, 10).until(
                    EC.element_to_be_clickable((By.XPATH, self.button_save_operational_hour_xpath))
                ).click()
            except TimeoutException:
                logger.error("Set Operational Hour Test Case Resulted Error")

            toggle_status = driver.find_element(By.XPATH, self.closed_xpath).get_attribute('data-active')

            assert modal_exist is True
            assert toggle_status == 'true'
            logger.success("Set Closed Operational Hour Test Case has been Tested")

    def test_set_time_operational_hour(self):
        with self.driver as driver:

            driver.execute_script("window.scrollTo(0,document.body.scrollHeight)")

            try:
                _ = WebDriverWait(driver, 10).until(
                    EC.element_to_be_clickable((By.XPATH, self.profile_page_xpath))
                ).click()
            except TimeoutException:
                logger.error("Set Operational Hour Test Case Resulted Error")

            try:
                _ = WebDriverWait(driver, 10).until(
                    EC.text_to_be_present_in_element((By.TAG_NAME, "h3"), self.valid_page_name)
                )
            except TimeoutException:
                logger.error("Set Operational Hour Test Case Resulted Error")
                return

            try:
                _ = WebDriverWait(driver, 10).until(
                    EC.presence_of_element_located((By.XPATH, self.table_operational_hours_xpath))
                )
            except TimeoutException:
                logger.error("Set Operational Hour Test Case Resulted Error")
                return

            table_row_elements = driver.find_elements(By.XPATH, self.table_row_xpath)
            for row_element in table_row_elements:
                if row_element.find_element(By.TAG_NAME, 'span').text == self.day_operational_hour:
                    row_element.find_element(By.TAG_NAME, 'button').click()
                    break

            try:
                _ = WebDriverWait(driver, 10).until(
                    EC.presence_of_element_located((By.XPATH, self.modal_operational_xpath))
                )
            except TimeoutException:
                logger.error("Set Operational Hour Test Case Resulted Error")
                return

            try:
                _ = WebDriverWait(driver, 10).until(
                    EC.element_to_be_clickable((By.XPATH, self.button_set_time_xpath))
                ).click()
            except TimeoutException:
                logger.error("Set Operational Hour Test Case Resulted Error")

            driver.find_element(By.ID, 'openTime').click()

            time_row_elements = driver.find_elements(By.XPATH, '/html/body/div[3]/div[3]/div/div[1]/div/div[2]/div/div')
            for row_element in time_row_elements:
                if row_element.find_element(By.TAG_NAME, 'span').text == '1':
                    row_element.click()

            try:
                _ = WebDriverWait(driver, 10).until(
                    EC.element_to_be_clickable((By.XPATH, self.button_save_operational_hour_xpath))
                ).click()
            except TimeoutException:
                logger.error("Set Operational Hour Test Case Resulted Error")

            logger.success("Set Operational Hour Test Case has been Tested")

    @classmethod
    def as_suite(cls, test_suite: unittest.TestSuite) -> unittest.TestSuite:
        test_suite.addTest(cls('test_change_profile_cover'))
        test_suite.addTest(cls('test_change_business_information'))
        test_suite.addTest(cls('test_set_twenty_four_operational_hour'))
        test_suite.addTest(cls('test_set_closed_operational_hour'))
        test_suite.addTest(cls('test_set_time_operational_hour'))
        return test_suite

    def tearDown(self) -> None:
        pass
