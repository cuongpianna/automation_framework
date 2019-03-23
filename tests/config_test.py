import unittest
from base.browser_factory import WebDriverFactory


def get_driver():
    wdf = WebDriverFactory('firefox').get_web_driver_instance()
    # driver = wdf.get_web_driver_instance('http://giadinh.net.vn/')
    return wdf


class BaseTest(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        # cls.driver = get_driver()
        pass

    @classmethod
    def tearDownClass(cls):
        # cls.driver.quit()
        pass
