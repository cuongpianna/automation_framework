from requests_html import HTMLSession

from base.base_requests.base import SessionBase


class URL(object):
    def __init__(self, url):
        self.url = url

    def __str__(self):
        return self.url


class Element(object):
    """
        Class Element: represent element on the website
    """
    def __init__(self, name, locator):
        self.name = name
        self.locator = locator[0]
        self.locator_type = locator[1]

    def __str__(self):
        return '{} has name: \t{}'.format(self.__class__.__name__, self.name)

    def get_response(self):
        session = self.session.get(self.url)
        html = SessionBase(session)
        return html


class ElementList(Element):
    """
    Class ElementList: represents list of element on the website
    """

    def __init__(self, name, locator):
        super(ElementList, self).__init__(name, locator)

    def get_this_element_list(self):
        html = self.get_response()
        return html.get_element_list(self.locator, self.locator_type)

    def get_text_of_element_list(self):
        element_list = self.get_this_element_list()
        result = []
        for item in element_list:
            result.append(item.text)
        return result


class BoxMetaClass(type):
    """
    Metaclass for all boxs.
    """
    def __new__(cls, name, bases, attrs):
        _session = None
        _url = None

        # Also ensure initialization is only performed for subclasses of Model.
        # (excluding Box class itself).
        parents = [b for b in bases if isinstance(b, BoxMetaClass)]
        if not parents:
            return super(BoxMetaClass, cls).__new__(cls, name, bases, attrs)
        mappings = dict()
        removes = dict()
        for key, value in attrs.items():
            # If attribute is URL object, attach url for Box class as an attribute.
            if isinstance(value, URL):
                attrs['url'] = value.url
                _url = value.url
                removes[key] = value
            # Get all attrs that is instance of Element class.
            # And store them into ``mappings``.
            if isinstance(value, Element):
                _session = HTMLSession()
                mappings[key] = value
                value.url = _url
                value.session = _session
                removes[key] = value

        for key, value in removes.items():
            attrs.pop(key)

        attrs['__mappings__'] = mappings
        return super(BoxMetaClass, cls).__new__(cls, name, bases, attrs)


class Box(metaclass=BoxMetaClass):
    def test(self):
        for k, v in self.__mappings__.items():
            print(v.get_this_element_list())

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

        for key, value in self.__mappings__.items():
            if item == 'verify_text_list' + key:
                return lambda: self.base_verify_list_text(value)

    @staticmethod
    def base_verify_list_text(element_list):
        list_text = element_list.get_text_of_element_list()
        return list_text
