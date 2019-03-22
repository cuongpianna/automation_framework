from base.selenium_driver import SeleniumDriver
from tests.config_test import get_driver


class ElementMetaClass(type):
    def __new__(cls, name, bases, attrs):
        element_name = name.lower()
        attrs['__name__'] = element_name
        return super(ElementMetaClass, cls).__new__(cls, name, bases, attrs)


class Element(object, metaclass=ElementMetaClass):
    """
    Class Element: represent on the website
    """

    def __init__(self, name, locator, verify='text'):
        """
        Init a new element
        :param name: name of element
        :param locator: => List:  this is a list that contains 2 items.
                item1: => Str:  locator of element
                items2: => Str: locator type of element
                Ex. ['box', 'classname']
        :param verify:
        """
        self.name = name
        self.locator = locator[0]
        self.locator_type = locator[1]
        self.verify = verify

    def __str__(self):
        return '{} has name: \t{}'.format(self.__class__.__name__, self.name)

    def go_to_page(self):
        """ Go to this page"""
        # Setting Driver Implicit Time out for An Element
        self.wdf.implicitly_wait(3)
        # Maximize the window
        self.wdf.maximize_window()
        # Loading browser with App URL
        self.wdf.get(self.base_url)

    def quit_driver(self):
        """ Get out from driver """
        self.wdf.quit()

    def get_this_element(self):
        """ Get this element """
        element = self.driver.get_element(self.locator, self.locator_type)
        return element

    def get_text_of_this_element(self):
        """ Get text of this element """
        this_element = self.get_this_element()
        return self.driver.get_text(element=this_element)

    def click_on_this_element(self):
        """ Click on this element """
        this_element = self.get_this_element()
        self.driver.element_click(element=this_element)


class LinkElement(Element):
    def __init__(self, name, locator):
        super(LinkElement, self).__init__(name, locator)

    def say(self):
        print(self.locator)


class BoxMetaClass(type):
    """Metaclass for all models."""
    def __init__(self, name, bases, attrs):
        super(BoxMetaClass, self).__init__(name, bases, attrs)
        self.name = name
        self.bases = bases
        self.attrs = attrs

    def __new__(cls, name, bases, attrs):
        _driver = None

        if name == 'Model':
            return super(BoxMetaClass, cls).__new__(cls, name, bases, attrs)

        # Also ensure initialization is only performed for subclasses of Model
        # (excluding Box class itself).
        parents = [b for b in bases if isinstance(b, BoxMetaClass)]
        if not parents:
            return super(BoxMetaClass, cls).__new__(cls, name, bases, attrs)

        # Get all attrs that is instance of Element class, and store them into ``mappings``
        mappings = dict()
        for k, v in attrs.items():
            if isinstance(v, Element):
                mappings[k] = v
            if isinstance(v, str):
                pass

        # Pass all necessary parameters for Element object. Ex: base_url, driver.
        for k, v in mappings.items():
            v.base_url = 'http://giadinh.net.vn/'
            v.wdf = get_driver()
            _driver = v.wdf
            v.driver = SeleniumDriver(v.wdf)
            attrs['driver'] = v.driver
            attrs.pop(k)

        # Pass all necessary parameters for Box class. Ex: base_url, driver.
        attrs['__mappings__'] = mappings
        attrs['__tabel__'] = name
        attrs['driver'] = _driver
        return super(BoxMetaClass, cls).__new__(cls, name, bases, attrs)


class Box(metaclass=BoxMetaClass):
    def __init__(self, **kwards):
        # super(Box, self).__init__(**kwards)
        # self.__table__ = self.__class__.__name__
        pass

    # def __getattr__(self, key):
    #     try:
    #         return self[key]
    #     except KeyError as e:
    #         raise AttributeError(f'{self.__name__} object has not attribute {key}')
    #
    # def __setattr__(self, key, value):
    #     self[key] = value

    @staticmethod
    def base_verify_text(element):
        element.go_to_page()
        text = element.get_text_of_this_element()
        element.quit_driver()
        return text

    def __getattr__(self, item):
        """
        Generate dynamic method for subclass when you call method.
        The method name depends on the attribute name of subclass.

        Example:
            class BoxTest(Box):
                _box_title = Element(name='box_title', locator=[])

            def test(self):
                return self.verify_text_of_box_title()

            The Box class will automatically generate method named ``verify_text_of_box_title``
        """

        for k, v in self.__mappings__.items():
            if item == 'verify_text_of' + k:
                return lambda: self.base_verify_text(v)

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

    # def test(self):
    #     for k, v in self.__mappings__.items():
    #         if isinstance(v, LinkElement):
    #             v.base_url = 'http://giadinh.net.vn/'
    #             v.wdf = get_driver()
    #             v.driver = SeleniumDriver(v.wdf)
    #             v.go_to_page()
    #             print(v.get_text_of_this_element())
    #             v.quit_driver()
        # driver.quit()

    @classmethod
    def saying(cls):
        print('sayiing......')

