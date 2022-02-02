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


class EmployeeJobPositionTests(unittest.TestCase):
    def setUp(self) -> None:
        load_dotenv()
        warnings.filterwarnings("ignore", category=DeprecationWarning)

        self.driver = LoginDriver().driver

        # data
        fake = Faker('id-ID')

        self.valid_page_name = 'Posisi & Tugas Karyawan'
        self.valid_new_position_name = 'Bos'

        self.set_job_position_employee = 'Detach Employee'
        self.set_job_position_role = 'View Role Merchant'
        self.set_job_position_table = 'View Merchant Table'
        self.set_job_position_product_category = 'Delete Product Category'
        self.set_job_position_product = 'Edit Product'
        self.set_job_position_order = 'View Order'
        self.set_job_position_report = 'Download Report'
        self.set_job_position_discount = 'Edit Discount Merchant'
        self.set_job_position_billing = 'Get Billing'
        self.set_job_position_printer = 'Edit Printer'
        self.set_job_position_order_additional = 'Edit Order Additionals Fee'
        self.set_job_position_notification = 'New Order Notification'

        self.set_new_job_position_employee = 'Get Recruitment'
        self.set_new_job_position_role = 'Edit Role Merchant'
        self.set_new_job_position_table = 'Get Request Table'
        self.set_new_job_position_product_category = 'Create Product Category'
        self.set_new_job_position_product = 'Create Product'
        self.set_new_job_position_order = 'Create Order Cashier'
        self.set_new_job_position_report = 'View Report'
        self.set_new_job_position_discount = 'Delete Discount Merchant'
        self.set_new_job_position_billing = 'Pay Billing'
        self.set_new_job_position_printer = 'Edit Printer'
        self.set_new_job_position_order_additional = 'Create Order Additionals Fee'
        self.set_new_job_position_notification = 'New Order Notification'

        self.invalid_phone_number = fake.language_name()
        self.invalid_email = fake.name()

        # Xpath
        self.employee_position_page_xpath = '//*[@id="root"]/div[2]/div[2]/div[10]/div[1]/div[2]'
        self.employee_job_position_chart_xpath = '//*[@id="root"]/div[2]/div[3]/div/div[2]/div[3]/div/div[2]'
        self.table_row_xpath = '//*[@id="root"]/div[2]/div[3]/div/div[2]/div[3]/div/div[2]/div'
        self.modal_confirmation_xpath = '/html/body/div[9]/div[3]/div'

        # button
        self.button_create_position_xpath = '//*[@id="root"]/div[2]/div[3]/div/div[2]/div[2]/button'
        self.button_save_position_xpath = '/html/body/div[1]/div[2]/div[3]/div/div[1]/div[2]/div[3]/button'
        self.button_delete_job_position_xpath = '/html/body/div[{index}]/div[3]/ul/li[2]'
        self.button_edit_job_position_xpath = '/html/body/div[{index}]/div[3]/ul/li[1]'
        self.button_accept_confirmation_xpath = '/html/body/div[9]/div[3]/div/div[3]/button[2]'
        self.button_drop_down_report_xpath = '//*[@id="root"]/div[2]/div[2]/div[3]'
        self.button_access_back_office_xpath = '//*[@id="roleForm"]/div/div[2]/div/div[13]/label/span[2]/div'

        self.checkbox_row_job_employee_xpath = '//*[@id="roleForm"]/div/div[2]/div/div[1]/div'
        self.checkbox_row_job_role_xpath = '//*[@id="roleForm"]/div/div[2]/div/div[2]/div'
        self.checkbox_row_job_table_xpath = '//*[@id="roleForm"]/div/div[2]/div/div[3]/div'
        self.checkbox_row_job_product_category_xpath = '//*[@id="roleForm"]/div/div[2]/div/div[4]/div'
        self.checkbox_row_job_product_xpath = '//*[@id="roleForm"]/div/div[2]/div/div[5]/div'
        self.checkbox_row_job_order_xpath = '//*[@id="roleForm"]/div/div[2]/div/div[6]/div'
        self.checkbox_row_job_report_xpath = '//*[@id="roleForm"]/div/div[2]/div/div[7]/div'
        self.checkbox_row_job_discount_xpath = '//*[@id="roleForm"]/div/div[2]/div/div[8]/div'
        self.checkbox_row_job_billing_xpath = '//*[@id="roleForm"]/div/div[2]/div/div[9]/div'
        self.checkbox_row_job_printer_xpath = '//*[@id="roleForm"]/div/div[2]/div/div[10]'
        self.checkbox_row_job_order_additional_xpath = '//*[@id="roleForm"]/div/div[2]/div/div[11]/div'
        self.checkbox_row_job_notification_xpath = '//*[@id="roleForm"]/div/div[2]/div/div[12]/div'

        # etc
        self.context = {}

    def test_create_job_position(self):
        with self.driver as driver:

            driver.find_element(By.XPATH, self.button_drop_down_report_xpath).click()

            driver.execute_script("window.scrollTo(0,document.body.scrollHeight)")

            try:
                _ = WebDriverWait(driver, 10).until(
                    EC.element_to_be_clickable((By.XPATH, self.employee_position_page_xpath))
                ).click()
            except TimeoutException:
                logger.error("Set Employee Job Position Test Case Resulted Error")

            try:
                _ = WebDriverWait(driver, 10).until(
                    EC.text_to_be_present_in_element((By.TAG_NAME, "h3"), self.valid_page_name)
                )
            except TimeoutException:
                logger.error("Set Employee Job Position Test Case Resulted Error")
                return

            try:
                _ = WebDriverWait(driver, 10).until(
                    EC.presence_of_element_located((By.XPATH, self.employee_job_position_chart_xpath))
                )
                chart_exist = True
            except TimeoutException:
                logger.error("Set Employee Job Position Test Case Resulted Error")
                chart_exist = False
                return

            try:
                _ = WebDriverWait(driver, 10).until(
                    EC.element_to_be_clickable((By.XPATH, self.button_create_position_xpath))
                ).click()
            except TimeoutException:
                logger.error("Set Employee Job Position Test Case Resulted Error")

            driver.find_element(By.ID, 'name').send_keys(self.valid_new_position_name)

            # job employee
            try:
                _ = WebDriverWait(driver,10).until(
                    EC.presence_of_element_located((By.XPATH, self.checkbox_row_job_employee_xpath))
                )
                table_row_exist = True
            except TimeoutException:
                logger.error("Set Employee Job Position Test Case Resulted Error")
                table_row_exist = False
                return

            # job employee
            job_employee_elements = driver.find_element(By.XPATH, self.checkbox_row_job_employee_xpath)
            for row_element in job_employee_elements.find_elements(By.TAG_NAME, 'span'):
                if row_element.text == self.set_job_position_employee:
                    row_element.click()
                    break

            # job role
            job_role_elements = driver.find_element(By.XPATH, self.checkbox_row_job_role_xpath)
            for row_element in job_role_elements.find_elements(By.TAG_NAME, 'span'):
                if row_element.text == self.set_job_position_role:
                    row_element.click()
                    break

            # job table
            job_table_elements = driver.find_element(By.XPATH, self.checkbox_row_job_table_xpath)
            for row_element in job_table_elements.find_elements(By.TAG_NAME, 'span'):
                if row_element.text == self.set_job_position_table:
                    row_element.click()
                    break

            # job product category
            job_product_category_elements = driver.find_element(By.XPATH, self.checkbox_row_job_product_category_xpath)
            for row_element in job_product_category_elements.find_elements(By.TAG_NAME, 'span'):
                if row_element.text == self.set_job_position_product_category:
                    row_element.click()
                    break

            # job product
            job_product_elements = driver.find_element(By.XPATH, self.checkbox_row_job_product_xpath)
            for row_element in job_product_elements.find_elements(By.TAG_NAME, 'span'):
                if row_element.text == self.set_job_position_product:
                    row_element.click()
                    break

            # job order
            job_order_elements = driver.find_element(By.XPATH, self.checkbox_row_job_order_xpath)
            for row_element in job_order_elements.find_elements(By.TAG_NAME, 'span'):
                if row_element.text == self.set_job_position_order:
                    row_element.click()
                    break

            # job report
            job_report_elements = driver.find_element(By.XPATH, self.checkbox_row_job_report_xpath)
            for row_element in job_report_elements.find_elements(By.TAG_NAME, 'span'):
                if row_element.text == self.set_job_position_report:
                    row_element.click()
                    break

            # job discount
            job_discount_elements = driver.find_element(By.XPATH, self.checkbox_row_job_discount_xpath)
            for row_element in job_discount_elements.find_elements(By.TAG_NAME, 'span'):
                if row_element.text == self.set_job_position_discount:
                    row_element.click()
                    break

            # job billing
            job_billing_elements = driver.find_element(By.XPATH, self.checkbox_row_job_billing_xpath)
            for row_element in job_billing_elements.find_elements(By.TAG_NAME, 'span'):
                if row_element.text == self.set_job_position_billing:
                    row_element.click()
                    break

            # job printer
            job_printer_elements = driver.find_element(By.XPATH, self.checkbox_row_job_printer_xpath)
            for row_element in job_printer_elements.find_elements(By.TAG_NAME, 'span'):
                if row_element.text == self.set_job_position_printer:
                    row_element.click()
                    break

            # job order additional
            job_order_additional_elements = driver.find_element(By.XPATH, self.checkbox_row_job_order_additional_xpath)
            for row_element in job_order_additional_elements.find_elements(By.TAG_NAME, 'span'):
                if row_element.text == self.set_job_position_order_additional:
                    row_element.click()
                    break

            # job notification
            job_notification_elements = driver.find_element(By.XPATH, self.checkbox_row_job_notification_xpath)
            for row_element in job_notification_elements.find_elements(By.TAG_NAME, 'span'):
                if row_element.text == self.set_job_position_notification:
                    row_element.click()
                    break

            try:
                _ = WebDriverWait(driver, 10).until(
                    EC.element_to_be_clickable((By.XPATH, self.button_save_position_xpath))
                ).click()
            except TimeoutException:
                logger.error("Set Employee Job Position Test Case Resulted Error")

            assert chart_exist is True
            assert table_row_exist is True
            logger.success("Create Employee Job Position Test Case has been Tested")

    def test_delete_job_position(self):
        with self.driver as driver:

            driver.find_element(By.XPATH, self.button_drop_down_report_xpath).click()

            driver.execute_script("window.scrollTo(0,document.body.scrollHeight)")

            try:
                _ = WebDriverWait(driver, 10).until(
                    EC.element_to_be_clickable((By.XPATH, self.employee_position_page_xpath))
                ).click()
            except TimeoutException:
                logger.error("Delete Employee Job Position Test Case Resulted Error")

            try:
                _ = WebDriverWait(driver, 10).until(
                    EC.text_to_be_present_in_element((By.TAG_NAME, "h3"), self.valid_page_name)
                )
            except TimeoutException:
                logger.error("Delete Employee Job Position Test Case Resulted Error")
                return

            try:
                _ = WebDriverWait(driver, 10).until(
                    EC.presence_of_element_located((By.XPATH, self.employee_job_position_chart_xpath))
                )
                chart_exist = True
            except TimeoutException:
                logger.error("Delete Employee Job Position Test Case Resulted Error")
                chart_exist = False
                return

            table_row_elements = driver.find_elements(By.XPATH, self.table_row_xpath)
            for index, row_element in enumerate(table_row_elements):
                if row_element.find_element(By.TAG_NAME, 'strong').text == self.valid_new_position_name:
                    row_element.find_element(By.TAG_NAME, 'button').click()
                    break

            driver.find_element(By.XPATH, self.button_delete_job_position_xpath.format(index=index+3)).click()

            try:
                _ = WebDriverWait(driver, 10).until(
                    EC.element_to_be_clickable((By.XPATH, self.button_accept_confirmation_xpath))
                ).click()
            except TimeoutException:
                logger.error("Delete Employee Job Position Test Case Resulted Error")

            assert chart_exist is True
            logger.success("Delete Employee Job Position Test Case has been Tested")

    def test_edit_job_position(self):
        with self.driver as driver:

            driver.find_element(By.XPATH, self.button_drop_down_report_xpath).click()

            driver.execute_script("window.scrollTo(0,document.body.scrollHeight)")

            try:
                _ = WebDriverWait(driver, 10).until(
                    EC.element_to_be_clickable((By.XPATH, self.employee_position_page_xpath))
                ).click()
            except TimeoutException:
                logger.error("Edit Employee Job Position Test Case Resulted Error")

            try:
                _ = WebDriverWait(driver, 10).until(
                    EC.text_to_be_present_in_element((By.TAG_NAME, "h3"), self.valid_page_name)
                )
            except TimeoutException:
                logger.error("Edit Employee Job Position Test Case Resulted Error")
                return

            try:
                _ = WebDriverWait(driver, 10).until(
                    EC.presence_of_element_located((By.XPATH, self.employee_job_position_chart_xpath))
                )
                chart_exist = True
            except TimeoutException:
                logger.error("Edit Employee Job Position Test Case Resulted Error")
                chart_exist = False
                return

            table_row_elements = driver.find_elements(By.XPATH, self.table_row_xpath)
            for index, row_element in enumerate(table_row_elements):
                if row_element.find_element(By.TAG_NAME, 'strong').text == self.valid_new_position_name:
                    row_element.find_element(By.TAG_NAME, 'button').click()
                    break

            driver.find_element(By.XPATH, self.button_edit_job_position_xpath.format(index=index + 3)).click()

            try:
                _ = WebDriverWait(driver, 10).until(
                    EC.presence_of_element_located((By.XPATH, self.checkbox_row_job_employee_xpath))
                )
                table_row_exist = True
            except TimeoutException:
                logger.error("Edit Employee Job Position Test Case Resulted Error")
                table_row_exist = False
                return

            # job employee
            job_employee_elements = driver.find_element(By.XPATH, self.checkbox_row_job_employee_xpath)
            for row_element in job_employee_elements.find_elements(By.TAG_NAME, 'span'):
                if row_element.text == self.set_job_position_employee:
                    row_element.click()
                    break

            for row_element in job_employee_elements.find_elements(By.TAG_NAME, 'span'):
                if row_element.text == self.set_new_job_position_employee:
                    row_element.click()
                    break

            # job role
            job_role_elements = driver.find_element(By.XPATH, self.checkbox_row_job_role_xpath)
            for row_element in job_role_elements.find_elements(By.TAG_NAME, 'span'):
                if row_element.text == self.set_job_position_role:
                    row_element.click()
                    break

            for row_element in job_role_elements.find_elements(By.TAG_NAME, 'span'):
                if row_element.text == self.set_new_job_position_role:
                    row_element.click()
                    break

            # job table
            job_table_elements = driver.find_element(By.XPATH, self.checkbox_row_job_table_xpath)
            for row_element in job_table_elements.find_elements(By.TAG_NAME, 'span'):
                if row_element.text == self.set_job_position_table:
                    row_element.click()
                    break

            for row_element in job_table_elements.find_elements(By.TAG_NAME, 'span'):
                if row_element.text == self.set_new_job_position_table:
                    row_element.click()
                    break

            # job product category
            job_product_category_elements = driver.find_element(By.XPATH, self.checkbox_row_job_product_category_xpath)
            for row_element in job_product_category_elements.find_elements(By.TAG_NAME, 'span'):
                if row_element.text == self.set_job_position_product_category:
                    row_element.click()
                    break

            for row_element in job_product_category_elements.find_elements(By.TAG_NAME, 'span'):
                if row_element.text == self.set_new_job_position_product_category:
                    row_element.click()
                    break

            # job product
            job_product_elements = driver.find_element(By.XPATH, self.checkbox_row_job_product_xpath)
            for row_element in job_product_elements.find_elements(By.TAG_NAME, 'span'):
                if row_element.text == self.set_job_position_product:
                    row_element.click()
                    break

            for row_element in job_product_elements.find_elements(By.TAG_NAME, 'span'):
                if row_element.text == self.set_new_job_position_product:
                    row_element.click()
                    break

            # job order
            job_order_elements = driver.find_element(By.XPATH, self.checkbox_row_job_order_xpath)
            for row_element in job_order_elements.find_elements(By.TAG_NAME, 'span'):
                if row_element.text == self.set_job_position_order:
                    row_element.click()
                    break

            for row_element in job_order_elements.find_elements(By.TAG_NAME, 'span'):
                if row_element.text == self.set_new_job_position_order:
                    row_element.click()
                    break

            # job report
            job_report_elements = driver.find_element(By.XPATH, self.checkbox_row_job_report_xpath)
            for row_element in job_report_elements.find_elements(By.TAG_NAME, 'span'):
                if row_element.text == self.set_job_position_report:
                    row_element.click()
                    break

            for row_element in job_report_elements.find_elements(By.TAG_NAME, 'span'):
                if row_element.text == self.set_new_job_position_report:
                    row_element.click()
                    break

            # job discount
            job_discount_elements = driver.find_element(By.XPATH, self.checkbox_row_job_discount_xpath)
            for row_element in job_discount_elements.find_elements(By.TAG_NAME, 'span'):
                if row_element.text == self.set_job_position_discount:
                    row_element.click()
                    break

            for row_element in job_discount_elements.find_elements(By.TAG_NAME, 'span'):
                if row_element.text == self.set_new_job_position_discount:
                    row_element.click()
                    break

            # job billing
            job_billing_elements = driver.find_element(By.XPATH, self.checkbox_row_job_billing_xpath)
            for row_element in job_billing_elements.find_elements(By.TAG_NAME, 'span'):
                if row_element.text == self.set_job_position_billing:
                    row_element.click()
                    break

            for row_element in job_billing_elements.find_elements(By.TAG_NAME, 'span'):
                if row_element.text == self.set_new_job_position_billing:
                    row_element.click()
                    break

            # job printer
            job_printer_elements = driver.find_element(By.XPATH, self.checkbox_row_job_printer_xpath)
            for row_element in job_printer_elements.find_elements(By.TAG_NAME, 'span'):
                if row_element.text == self.set_job_position_printer:
                    row_element.click()
                    break

            for row_element in job_printer_elements.find_elements(By.TAG_NAME, 'span'):
                if row_element.text == self.set_new_job_position_printer:
                    row_element.click()
                    break

            # job order additional
            job_order_additional_elements = driver.find_element(By.XPATH, self.checkbox_row_job_order_additional_xpath)
            for row_element in job_order_additional_elements.find_elements(By.TAG_NAME, 'span'):
                if row_element.text == self.set_job_position_order_additional:
                    row_element.click()
                    break

            for row_element in job_order_additional_elements.find_elements(By.TAG_NAME, 'span'):
                if row_element.text == self.set_new_job_position_order_additional:
                    row_element.click()
                    break

            # job notification
            job_notification_elements = driver.find_element(By.XPATH, self.checkbox_row_job_notification_xpath)
            for row_element in job_notification_elements.find_elements(By.TAG_NAME, 'span'):
                if row_element.text == self.set_job_position_notification:
                    row_element.click()
                    break

            for row_element in job_notification_elements.find_elements(By.TAG_NAME, 'span'):
                if row_element.text == self.set_new_job_position_notification:
                    row_element.click()
                    break

            try:
                _ = WebDriverWait(driver, 10).until(
                    EC.element_to_be_clickable((By.XPATH, self.button_save_position_xpath))
                ).click()
            except TimeoutException:
                logger.error("Edit Employee Job Position Test Case Resulted Error")

            assert chart_exist is True
            assert table_row_exist is True
            logger.success("Edit Employee Job Position Test Case Test Case has been Tested")

    def test_edit_job_position_enable_access_back_office(self):
        with self.driver as driver:

            driver.find_element(By.XPATH, self.button_drop_down_report_xpath).click()

            driver.execute_script("window.scrollTo(0,document.body.scrollHeight)")

            try:
                _ = WebDriverWait(driver, 10).until(
                    EC.element_to_be_clickable((By.XPATH, self.employee_position_page_xpath))
                ).click()
            except TimeoutException:
                logger.error("Edit Enable Access Back Office Test Case Resulted Error")

            try:
                _ = WebDriverWait(driver, 10).until(
                    EC.text_to_be_present_in_element((By.TAG_NAME, "h3"), self.valid_page_name)
                )
            except TimeoutException:
                logger.error("Edit Enable Access Back Office Test Case Resulted Error")
                return

            try:
                _ = WebDriverWait(driver, 10).until(
                    EC.presence_of_element_located((By.XPATH, self.employee_job_position_chart_xpath))
                )
                chart_exist = True
            except TimeoutException:
                logger.error("Edit Enable Access Back Office Test Case Resulted Error")
                chart_exist = False
                return

            table_row_elements = driver.find_elements(By.XPATH, self.table_row_xpath)
            for index, row_element in enumerate(table_row_elements):
                if row_element.find_element(By.TAG_NAME, 'strong').text == self.valid_new_position_name:
                    row_element.find_element(By.TAG_NAME, 'button').click()
                    break

            driver.find_element(By.XPATH, self.button_edit_job_position_xpath.format(index=index + 3)).click()

            try:
                _ = WebDriverWait(driver, 10).until(
                    EC.presence_of_element_located((By.XPATH, self.checkbox_row_job_employee_xpath))
                )
                table_row_exist = True
            except TimeoutException:
                logger.error("Edit Enable Access Back Office Test Case Resulted Error")
                table_row_exist = False
                return

            try:
                _ = WebDriverWait(driver, 10).until(
                    EC.element_to_be_clickable((By.XPATH, self.button_access_back_office_xpath))
                ).click()
            except TimeoutException:
                logger.error("Edit Enable Access Back Office Test Case Resulted Error")
                return

            try:
                _ = WebDriverWait(driver, 10).until(
                    EC.element_to_be_clickable((By.XPATH, self.button_save_position_xpath))
                ).click()
            except TimeoutException:
                logger.error("Edit Enable Access Back Office Test Case Resulted Error")

            assert chart_exist is True
            assert table_row_exist is True
            logger.success("Edit Enable Access Back Office Test Case Test Case has been Tested")

    @classmethod
    def as_suite(cls, test_suite: unittest.TestSuite) -> unittest.TestSuite:
        test_suite.addTest(cls('test_create_job_position'))
        test_suite.addTest(cls('test_edit_job_position'))
        test_suite.addTest(cls('test_edit_job_position_enable_access_back_office'))
        test_suite.addTest(cls('test_delete_job_position'))
        return test_suite

    def tearDown(self) -> None:
        pass
