import unittest

from tests.config_test import BaseTest
from pages.home.box import User
from utilities.test_status import TestStatus
# from utilities.read_data import get_csv_data


class HomeTest(BaseTest):
    def setUp(self):
        self.page = User()
        # self.ts = TestStatus(self.driver)
        pass

    def test_domain(self):
        self.page.verify_text()


if __name__ == '__main__':
    unittest.main()
