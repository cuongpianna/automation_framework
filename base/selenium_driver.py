import os
import time
import logging
from traceback import print_stack
from selenium.webdriver import ActionChains
from selenium.common import exceptions
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import *
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.expected_conditions import element_to_be_clickable
from utilities.custom_logger import custom_logger
from utilities.base import convert_text, convert_file_name


class SeleniumDriver:
    log = custom_logger(logging.DEBUG)

    def __init__(self, driver):
        self.driver = driver

    def screen_shot(self, result_message):
        """
        Take screenshot of the current open webpage
        """
        result_message = convert_text(result_message)
        file_name = convert_file_name(result_message)
        file_name = file_name + '.' + str(round(time.time()*1000)) + '.png'
        screen_directory = 'screenshots'
        relative_file_name = os.path.join(screen_directory, file_name)
        current_directory = os.path.dirname(__file__)
        destination_file = os.path.join(current_directory, relative_file_name)
        destination_directory = os.path.join(current_directory, screen_directory)
        try:
            if not os.path.exists(destination_directory):
                os.makedirs(destination_directory)
            self.driver.save_screenshot(destination_file)
            self.log.info('Screenshot save to directory: ' + destination_file)
        except:
            self.log.error('### Exception Occured')
            # print_stack()

    def get_by_type(self, locator_type):
        locator_type = locator_type.lower()
        if locator_type == 'id':
            return By.ID
        elif locator_type == 'name':
            return By.NAME
        elif locator_type == 'xpath':
            return By.XPATH
        elif locator_type == 'css':
            return By.CSS_SELECTOR
        elif locator_type == 'classname':
            return By.CLASS_NAME
        elif locator_type == 'link':
            return By.LINK_TEXT
        elif locator_type == 'tagname':
            return By.TAG_NAME
        else:
            self.log.info('Locator type ' + locator_type + 'not supported')
        return False

    def get_element(self, locator, locator_type='id'):
        element = None
        try:
            locator_type = locator_type.lower()
            by_type = self.get_by_type(locator_type)
            element = self.driver.find_element(by_type, locator)
            self.log.info('Element Found with locator: ' + locator + 'and locator_type: ' + locator_type)
        except:
            self.log.info('Element not found: ' + locator + 'and locator_type: ' + locator_type)
        return element

    def get_element_list(self, locator, locator_type="id"):
        """
        Get list of elements
        """
        element = None
        try:
            locator_type = locator_type.lower()
            by_type = self.get_by_type(locator_type)
            element = self.driver.find_elements(by_type, locator)
            self.log.info("Element list found with locator: " + locator +
                          " and  locatorType: " + locator_type)
        except:
            self.log.info("Element list not found with locator: " + locator +
                          " and  locatorType: " + locator_type)
        return element

    def get_title(self):
        return self.driver.title

    def get_element_attr(self, locator, locator_type, attr):
        attr_value = None
        try:
            element = self.get_element(locator, locator_type)
            self.log.info("Element list found with locator: " + locator + " and  locatorType: " + locator_type)
            attr_value = self.driver.get_attribute(attr)
        except:
            self.log.info("Element list not found with locator: " + locator +
                          " and  locatorType: " + locator_type)
        return attr_value

    def get_text(self, locator="", locator_type="id", element=None, info=""):
        """
        Get 'Text' on an element
        Either provide element or a combination of locator and locatorType
        """
        try:
            if locator:  # This means if locator is not empty
                self.log.debug("In locator condition")
                element = self.get_element(locator, locator_type)
            self.log.debug("Before finding text")
            text = element.text
            self.log.debug("After finding element, size is: " + str(len(text)))
            if len(text) == 0:
                text = element.get_attribute("innerText")
            if len(text) != 0:
                self.log.info("Getting text on element :: " + info)
                self.log.info("The text is :: '" + text + "'")
                text = text.strip()
        except:
            self.log.error("Failed to get text on element " + info)
            # print_stack()
            text = None
        return text

    def get_element_text(self, element):
        return element.text.strip()

    def element_click(self, locator='', locator_type="id", element=None):
        try:
            if locator:
                element = self.get_element(locator, locator_type)
                element.click()
            if element:
                element.click()
            self.log.info("Clicked on element with locator: " + locator + " locatorType: " + locator_type)
            return True
        except:
            self.log.info("Cannot click on the element with locator: " + locator + " locatorType: " + locator_type)
            return False
            # print_stack()

    def send_keys(self, data, locator=None, locator_type="id", element=None):
        try:
            if locator:
                element = self.get_element(locator, locator_type)
            element.clear()
            element.send_keys(data)
            self.log.info("Sent on element with locator: " + locator + " locatorType: " + locator_type)
        except:
            self.log.info("Cannot send on the element with locator: " + locator + " locatorType: " + locator_type)
            # print_stack()

    def is_element_present(self, locator, locator_type='id', element=None):
        try:
            if locator:
                element = self.get_element(locator, locator_type)
            if element is not None:
                self.log.info("Element Found: " + locator + 'with locator_type: ' + locator_type)
                return True
            else:
                self.log.info("Element not found: " + locator + 'with locator_type: ' + locator_type)
                return False
        except:
            self.log.info("Element not found: " + locator + 'with locator_type: ' + locator_type)
            return False

    def is_element_displayed(self, locator="", locator_type="id", element=None):
        """
        Check if element is displayed
        Either provide element or a combination of locator and locatorType
        """
        is_displayed = False
        try:
            if locator:
                element = self.get_element(locator, locator_type)
            if element is not None:
                is_displayed = element.is_displayed()
                self.log.info("Element is displayed with locator: " + locator +
                              " locatorType: " + locator_type)
            else:
                self.log.info("Element not displayed with locator: " + locator +
                              " locatorType: " + locator_type)
            return is_displayed
        except:
            print("Element not found")
            return False

    def element_presence_check(self, locator, locator_type='id'):
        """
            Check if element is present
        """
        try:
            element_list = self.get_element(locator, locator_type)
            if len(element_list) > 0:
                self.log.info("Element Found")
                return True
            else:
                self.log.info("Element not found")
                return False
        except:
            self.log.info("Element not found")
            return False

    def wait_for_element(self, locator, locator_type="id", time_out=10, poll_frequency=0.5):
        element = None
        try:
            by_type = self.get_by_type(locator_type)
            self.log.info("Waiting for maximum :: " + str(time_out) +
                          " :: seconds for element to be clickable")
            wait = WebDriverWait(self.driver, 10, poll_frequency=1,
                                 ignored_exceptions=[NoSuchElementException,
                                                     ElementNotVisibleException,
                                                     ElementNotSelectableException])
            element = wait.until(EC.element_to_be_clickable((by_type,
                                                             "stopFilter_stops-0")))
            self.log.info("Element appeared on the web page")
        except:
            self.log.info("Element not appeared on the web page")
            # print_stack()
        return element

    def web_scroll(self, direction="up"):
        """
        Scroll method
        """
        if direction == "up":
            # Scroll Up
            self.driver.execute_script("window.scrollBy(0, -1000);")

        if direction == "down":
            # Scroll Down
            self.driver.execute_script("window.scrollBy(0, 500);")

    def scroll_to_element_and_click(self, element):
        # actions = ActionChains(self.driver)
        # try:
        #     actions.move_to_element(element).click().perform()
        # except exceptions.StaleElementReferenceException:
        #     actions.move_to_element(element).click().perform()
        self.driver.execute_script("arguments[0].scrollIntoView();", element)
        element.click()

    def scroll_to_element(self, element):
        self.driver.execute_script("arguments[0].scrollIntoView();", element)

    def scroll_slowly(self):
        for second in range(20):
            if second >= 11:
                break
            time.sleep(0.1)
            self.driver.execute_script('window.scrollBy(arguments[0],400)', second)

    def scroll_to_position(self, position):
        for second in range(20):
            if second >= 11:
                break
            time.sleep(0.1)
            self.driver.execute_script('window.scrollBy(arguments[0],{})'.format(position), second)

    def mouse_hover(self, locator=None, locator_type='id', element=None):
        try:
            if locator:
                element = self.get_element(locator, locator_type)
            actions = ActionChains(self.driver)
            actions.move_to_element(element).perform()
            self.log.info("Hovered on element with locator: " + locator + " locatorType: " + locator_type)
        except:
            self.log.info("Can't hover on element with locator: " + locator + 'locatorType' + locator_type)

    def mouse_hover_and_click(self, locator1, locator_type1, locator2, locator_type2):
        """
        Mouse hover and move to element that you want to click
        :param locator1: locator of hover element
        :param locator_type1: locatorType of hover element
        :param locator2: locator of click element
        :param locator_type2: locatorType of click element
        """
        hover_element = None
        click_element = None
        try:
            hover_element = self.get_element(locator1, locator_type1)
        except:
            self.log.info("Can't found element with: " + locator1 + " locatorType: " + locator_type1)

        try:
            click_element = self.get_element(locator2, locator_type2)
        except:
            self.log.info("Can't found element with: " + locator2 + " locatorType: " + locator_type2)

        try:
            actions = ActionChains(self.driver)
            actions.move_to_element(hover_element).perform()
            actions.move_to_element(click_element).click().perform()
        except:
            pass

    def hover_on_hidden_element(self, e1, e2):
        actions = ActionChains(self.driver)
        actions.move_to_element(e1).perform()
        actions.move_to_element(e2).perform()

    def hover_on_element(self, element):
        actions = ActionChains(self.driver)
        actions.move_to_element(element).perform()

    def drag_and_drop_element(self, locator1, locator_type1, locator2, locator_type2):
        """
        Drag and drop element
        """
        from_element = None
        to_element = None
        try:
            from_element = self.get_element('//*[@id="admWrapsite"]/div[1]/div[3]/div/div[2]/div[2]/div[2]/ul/li[1]', 'xpath')
            # from_element = self.get_element(locator1, locator_type1)
            # self.log.info(self.is_element_displayed(locator=locator1, locator_type=locator_type1))
            self.driver.execute_script("arguments[0].setAttribute('style', 'border:red 1px solid')", from_element)
        except:
            self.log.info("Can't found element with: " + locator1 + " locatorType: " + locator_type1)
        try:
            # to_element = self.get_element(locator2, locator_type2)
            to_element = self.get_element('//*[@id="admWrapsite"]/div[1]/div[3]/div/div[2]/div[2]/div[1]/div', locator_type2)
            self.driver.execute_script("arguments[0].setAttribute('style', 'border: 1px solid green')", to_element)
            self.log.warning(to_element)
        except:
            self.log.info("Can't found element with: " + locator2 + " locatorType: " + locator_type2)
        try:
            self.driver.implicitly_wait(3)
            actions = ActionChains(self.driver)
            actions.drag_and_drop(from_element, to_element).perform()
            # alert = self.driver.switch_to.alert()
            # alert.accept()
            time.sleep(5)
        except:
            self.log.error('Drag fail!')

    def open_news_tab(self):
        main_window = self.driver.current_window_handle
        self.driver.find_element_by_tag_name('body').send_keys(Keys.CONTROL + 't')
        self.driver.get('https://cnnd.vn/')

    def check_element_clickable(self, locator):
        return element_to_be_clickable(locator)

    @staticmethod
    def get_css_attr(element, attr):
        return element.value_of_css_property(attr)

    def get_css_property(self, element):
        properties = self.driver.execute_script('return window.getComputedStyle(arguments[0], null);', element)
        return properties

    def get_line_text_of_element(self, element):
        result = self.driver.execute_script("return arguments[0].getClientRects();", element)
        return result['length']

    def get_offset_height(self, element):
        result = self.driver.execute_script("return arguments[0].offsetHeight;", element)
        return result

    def paste_to_element(self, element):
        element.click()
        element.send_keys(Keys.CONTROL, 'v')

    def cut_from_element(self, element):
        element.click()
        element.send_keys(Keys.CONTROL, 'a')
        element.send_keys(Keys.CONTROL, 'x')

    def chain_click_on_element(self, element):
        actions = ActionChains(self.driver)
        actions.click(element)
        actions.perform()

    def refresh_driver(self):
        self.driver.refresh()
