from traceback import print_stack
from base.selenium_driver import SeleniumDriver
from utilities.util import Util
from utilities.base import convert_pixel_to_number


class BasePage(SeleniumDriver):
    def __init__(self, driver):
        """
        Inits BasePage class
        Returns:
            None
        :param driver:
        """

        super(BasePage, self).__init__(driver)
        self.driver = driver
        self.util = Util()

    def verify_page_title(self, title_to_verify):
        """
        Verify page title

        :param title_to_verify: Title on the page that needs to be verified
        :return: True or False
        """
        try:
            actual_title = self.get_title()
            return self.util.verify_text_contains(actual_title, title_to_verify)
        except:
            self.log.error('Failed to get page title')
            print_stack()
            return False

    @staticmethod
    def get_tooltip(element):
        return element.get_attribute('title').strip()

    @staticmethod
    def get_background_color(element):
        return element.value_of_css_property('background-color')

    @staticmethod
    def get_attribute(element, attr):
        return element.get_attribute(attr)

    def get_news_title(self):
        return self.get_text('h1', 'tagname')

    def get_current_url(self):
        return self.driver.current_url

    def get_element_height(self, element):
        padding_top = convert_pixel_to_number(self.get_css_attr(element, 'padding-top'))
        padding_bottom = convert_pixel_to_number(self.get_css_attr(element, 'padding-bottom'))
        border_top = convert_pixel_to_number(self.get_css_attr(element, 'border-top')[0:3])
        border_bottom = convert_pixel_to_number(self.get_css_attr(element, 'border-top')[0:3])
        height = convert_pixel_to_number(self.get_css_attr(element, 'height'))
        return padding_top + padding_bottom + border_top + border_bottom + height

    def get_content_height(self, element):
        """
        Get height of element

        :param element: The element that you want to get height
        :return: Height of element -> int
        """
        return convert_pixel_to_number(self.get_css_attr(element, 'height'))

    def check_element_text_line(self, element, query_selector, line):
        height = self.driver.execute_script("return document.querySelector('{}').offsetHeight".format(query_selector))
        height = int(height)
        line_height = convert_pixel_to_number(self.get_css_attr(element, 'line-height'))
        return height/line_height <= line

    def go_home_page(self):
        """
        Go Home page
        """
        self.driver.get('http://giadinh.net.vn/')

    def compare_two_lists(self, lst1, lst2, error_msg, success_msg, pre_msg=''):
        error_list = []
        final_msg = ''

        for index, value in enumerate(lst1):
            if value != lst2[index]:
                error_list.append((value, lst2[index]))

        if error_list:
            for item in error_list:
                final_msg = final_msg + error_msg.format(*item)
            final_msg = final_msg + ' :: FAIL'
            if pre_msg:
                final_msg = pre_msg + final_msg
            return False, final_msg
        else:
            success_msg = pre_msg + success_msg
            return True, success_msg

    @staticmethod
    def get_width_height_of_element(element):
        dct = element.rect
        return dct['width'], dct['height']

    def get_current_url_without_http(self):
        current_url = self.driver.current_url
        if current_url[-1] == '/':
            current_url = current_url[:-1]
        if 'https' in current_url:
            return current_url[8:]
        else:
            return current_url[7:]
