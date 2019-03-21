from base.selenium_driver import SeleniumDriver
from tests.config_test import get_driver


class ElementMetaClass(type):
    def __new__(cls, name, bases, attrs):
        element_name = name.lower()
        attrs['__name__'] = element_name
        return super(ElementMetaClass, cls).__new__(cls, name, bases, attrs)


class Element(object, metaclass=ElementMetaClass):
    """
    docstring for Element
    """

    def __init__(self, name, locator, verify='text'):
        self.name = name
        self.locator = locator[0]
        self.locator_type = locator[1]
        self.verify = verify

    def __str__(self):
        return '{} has name: \t{}'.format(self.__class__.__name__, self.name)

    def go_to_page(self):
        # Setting Driver Implicit Time out for An Element
        self.wdf.implicitly_wait(3)
        # Maximize the window
        self.wdf.maximize_window()
        # Loading browser with App URL
        self.wdf.get(self.base_url)

    def quit_driver(self):
        self.wdf.quit()

    def get_this_element(self):
        element = self.driver.get_element(self.locator, self.locator_type)
        return element

    def get_text_of_this_element(self):
        this_element = self.get_this_element()
        return self.driver.get_text(element=this_element)


class LinkElement(Element):
    def __init__(self, name, locator):
        super(LinkElement, self).__init__(name, locator)

    def say(self):
        print(self.locator)


class ModelMetaClass(type):
    def __init__(self, name, bases, attrs):
        super(ModelMetaClass, self).__init__(name, bases, attrs)
        self.name = name
        self.bases = bases
        self.attrs = attrs

    def __new__(cls, name, bases, attrs):
        if name == 'Model':
            return super(ModelMetaClass, cls).__new__(cls, name, bases, attrs)
        # print(f'Found model{name}')
        mappings = dict()
        for k, v in attrs.items():
            if isinstance(v, Element):
                mappings[k] = v
            if isinstance(v, str):
                pass

        for k, v in mappings.items():
            # v.base_url = 'http://giadinh.net.vn/'
            # v.wdf = get_driver()
            # v.driver = SeleniumDriver(v.wdf)
            # attrs['driver'] = v.driver
            attrs.pop(k)
        attrs['__mappings__'] = mappings
        attrs['__tabel__'] = name
        # attrs['driver'] = get_driver()
        return super(ModelMetaClass, cls).__new__(cls, name, bases, attrs)


class Box(dict, metaclass=ModelMetaClass):
    """docstring for Box"""
    def __init__(self, **kwards):
        super(Box, self).__init__(**kwards)
        # self.__table__ = self.__class__.__name__

    # def __getattr__(self, key):
    #     try:
    #         return self[key]
    #     except KeyError as e:
    #         raise AttributeError(f'{self.__name__} object has not attribute {key}')

    def __getattribute__(self, item):
        super(Box, self).__getattribute__(item)

    def __setattr__(self, key, value):
        self[key] = value

    def save(self):
        fields = []
        params = []
        args = []
        for k, v in self.__mappings__.items():
            fields.append(v.name)
            params.append('?')
            args.append(getattr(self, k, None))
        sql = f"insert into {self.__table__}  ({','.join(fields)}) values ({ ','.join(str(x) for x in args)})"
        print(f'SQL:{sql}')
        print(f'ARGS:{str(args)}')

    def test(self):
        for k, v in self.__mappings__.items():
            if isinstance(v, LinkElement):
                v.base_url = 'http://giadinh.net.vn/'
                v.wdf = get_driver()
                v.driver = SeleniumDriver(v.wdf)
                v.go_to_page()
                print(v.get_text_of_this_element())
                v.quit_driver()
        # driver.quit()

    @classmethod
    def saying(cls):
        print('sayiing......')

    def verify_text_of_element(self):
        # for k, v in self.__mappings__.items():
        #     func_name = 'verify_text' + k
        #     setattr(self.__class__, 'g', 'f')
        pass
#
# class User(Box):
#     driver = 'this is driver'
#     id = LinkElement('id', 'ggg')
#     tesst = [1, 4, 2]
#
#
# if __name__ == '__main__':
#     u = User(id=12345)
#     u.test()


