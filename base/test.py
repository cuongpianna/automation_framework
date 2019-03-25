import sys
from os.path import dirname, abspath

sys.path.insert(0, dirname(dirname(abspath(__file__))))
from tests.config_test import get_driver

# a = get_driver()
# b = get_driver()


from base.base_requests.models import Box, ElementList, URL


class Test(Box):
    url = URL(url='https://tuoitre.vn/')
    _box_title = ElementList(name='test',
                             locator=['//*[@id="content"]/div/div[1]/div[2]/div[4]/ul/li/h2/a', 'xpath'])


class Test2(Box):
    url = URL(url='https://tuoitre.vn/')
    box_title = ElementList('name', 'test')


if __name__ == '__main__':
    t = Test()
    print(t.verify_text_list_box_title())
