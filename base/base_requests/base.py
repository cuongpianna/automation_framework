import logging

from utilities.custom_logger import custom_logger


class SessionBase:
    log = custom_logger(logging.DEBUG)

    def __init__(self, session):
        self.session = session
        self.html = session.html

    @staticmethod
    def get_text_of_element_list(elements):
        """
        Returns list that contains text of element list
        """
        result = []
        for item in elements:
            text_of_item = item.text
            result.append(text_of_item)
        return result

    def get_element(self, locator, locator_type):
        """
        Get element
        """
        if locator_type == 'xpath':
            return self.get_element_by_xpath(locator)
        elif locator_type == 'classname':
            return self.get_element_by_classname(locator)
        elif locator_type == 'id':
            return self.get_element_by_id()
        elif locator_type == 'tagname':
            return self.get_element_by_tag_name()

    def get_element_list(self, locator, locator_type):
        """
        Get element list
        """
        if locator_type == 'xpath':
            return self.get_element_list_by_xpath(locator)
        elif locator_type == 'classname':
            return self.get_element_list_by_classname(locator)
        elif locator_type == 'tagname':
            return self.get_element_list_by_tag_name()

    def get_element_by_id(self, element_id):
        pattern = '#' + element_id
        element = self.html.find(selector=element_id, first=True)
        if element:
            self.log.info('Element found with id: ' + pattern)
        else:
            self.log.info('Element not found with id: ' + pattern)
        return element

    def get_element_by_classname(self, class_name):
        pattern = '.' + class_name
        element = self.html.find(selector=class_name, first=True)
        if element:
            self.log.info('Element found with class name: ' + pattern)
        else:
            self.log.info('Element not found with class name: ' + pattern)
        return element

    def get_element_list_by_classname(self, class_name):
        pattern = '.' + class_name
        elements = self.html.find(selector=class_name)
        if elements:
            self.log.info('Element list found with class name: ' + pattern)
        else:
            self.log.info('Element list not found class name: ' + pattern)
        return elements

    def get_element_by_xpath(self, xpath):
        element = self.html.xpath(selector=xpath, first=True)
        if element:
            self.log.info('Element found with xpath: ' + xpath)
        else:
            self.log.info('Element not found with xpath: ' + xpath)
        return element

    def get_element_list_by_xpath(self, xpath):
        elements = self.html.xpath(selector=xpath)
        if elements:
            self.log.info('Element found with xpath: ' + xpath)
        else:
            self.log.info('Element not found with xpath: ' + xpath)
        return elements

    def get_element_by_tag_name(self, tag_name):
        element = self.html.find(selector=tag_name, first=True)
        if element:
            self.log.info('Element found with tag name: ' + tag_name)
        else:
            self.log.info('Element not found with tag name: ' + tag_name)
        return element

    def get_element_list_by_tag_name(self, tag_name):
        elements = self.html.find(selector=tag_name)
        if elements:
            self.log.info('Element found with tag name: ' + tag_name)
        else:
            self.log.info('Element not found with tag name: ' + tag_name)
        return elements



