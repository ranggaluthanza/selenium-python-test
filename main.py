import os
import unittest

from loguru import logger

from tests.auth.login import LoginTests
from tests.report.sales.sales_summary import SalesSummaryTests
from tests.report.sales.payment_method import PaymentMethodTests
from tests.report.sales.menu import SalesPerMenuTests

# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    logger.info(f"Starting {os.getcwd()}")
    unittest.main()

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
