from tests.config_test import get_driver
from base.models import Box, LinkElement, Element


class User(Box):
    def __init__(self):
        Box.__init__(self)

    _box_title = LinkElement(name=123,
                             locator=['//*[@id="TotalBox1"]/div[1]/div[1]/h2/a', 'xpath'])

    def verify_text(self):
        print(self.verify_text_of_box_title())

