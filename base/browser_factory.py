"""
@package base

WebDriver Factory class implementation
It creates a webdriver instance based on browser configurations

Example:
    wdf = WebDriverFactory(browser)
    wdf.getWebDriverInstance()
"""
import os
import traceback
from selenium import webdriver
from selenium.webdriver.firefox.firefox_binary import FirefoxBinary
from selenium.webdriver.chrome.options import Options


class WebDriverFactory:

    def __init__(self, browser):
        """
        Inits WebDriverFactory class

        Returns:
            None
        """
        self.browser = browser
    """
        Set chrome driver and iexplorer environment based on OS

        chromedriver = "C:/.../chromedriver.exe"
        os.environ["webdriver.chrome.driver"] = chromedriver
        self.driver = webdriver.Chrome(chromedriver)

        PREFERRED: Set the path on the machine where browser will be executed
    """

    # def get_web_driver_instance(self, base_url):
    #     """
    #    Get WebDriver Instance based on the browser configuration
    #
    #     Returns:
    #         'WebDriver Instance'
    #     """
    #
    #     cwd = os.getcwd()
    #     if self.browser == "iexplorer":
    #         # Set ie driver
    #         driver = webdriver.Ie()
    #     elif self.browser == "firefox":
    #         firefox_path = os.path.join(cwd, 'base', 'geckodriver.exe')
    #         options = webdriver.FirefoxOptions()
    #         # options.set_headless(True)
    #         driver = webdriver.Firefox(executable_path=firefox_path, service_log_path='NUL', options=options)
    #     elif self.browser == "chrome":
    #         # Set chrome driver
    #         chrome_path = os.path.join(cwd, 'base', 'chromedriver.exe')
    #         driver = webdriver.Chrome(chrome_path)
    #     else:
    #         driver = webdriver.Firefox()
    #     # Setting Driver Implicit Time out for An Element
    #     driver.implicitly_wait(3)
    #     # Maximize the window
    #     driver.maximize_window()
    #     # Loading browser with App URL
    #     driver.get(base_url)
    #     return driver

    def get_web_driver_instance(self):
        """
       Get WebDriver Instance based on the browser configuration

        Returns:
            'WebDriver Instance'
        """

        cwd = os.getcwd()
        if self.browser == "iexplorer":
            # Set ie driver
            driver = webdriver.Ie()
        elif self.browser == "firefox":
            firefox_path = os.path.join(cwd, 'base', 'geckodriver.exe')
            options = webdriver.FirefoxOptions()
            # options.set_headless(True)
            driver = webdriver.Firefox(executable_path=firefox_path, service_log_path='NUL', options=options)
        elif self.browser == "chrome":
            # Set chrome driver
            chrome_path = os.path.join(cwd, 'base', 'chromedriver.exe')
            driver = webdriver.Chrome(chrome_path)
        else:
            driver = webdriver.Firefox()
        # Setting Driver Implicit Time out for An Element
        # driver.implicitly_wait(3)
        # Maximize the window
        # driver.maximize_window()
        # Loading browser with App URL
        # driver.get(base_url)
        return driver
