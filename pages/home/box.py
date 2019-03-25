from base.models import Box, LinkElement, ListElement


class User(Box):
    def __init__(self):
        Box.__init__(self)

    _box_title = LinkElement(
        name=123,
        locator=['//*[@id="TotalBox1"]/div[1]/div[1]/h2/a', 'xpath'])
    _news_list = ListElement(
        name='news_list',
        locator=['//*[@id="form1"]/div[3]/div[3]/div[4]/div[1]/div[1]/div[1]/div[3]/ul/li/h3/a', 'xpath'])

    def verify_text(self):
        print(self.verify_list_news_list())

    def test(self):
        print(self.verify_text_of_box_title())
