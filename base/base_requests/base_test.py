from requests_html import HTMLSession

from base.base_requests.base import SessionBase


class URL(object):
    def __init__(self, url):
        self.url = url

    def __str__(self):
        return self.url


class BaseElement(object):
    """
        Class Element: represent element on the website
    """

    def __init__(self, name, url, root):
        self.name = name
        self.url = url
        self.session = HTMLSession().get(self.url)
        self.root = SessionBase(self.session).get_element(root[0], root[1])

    def __str__(self):
        return '{} has name: \t{}'.format(self.__class__.__name__, self.name)


class ElementList(BaseElement):
    """
    Class ElementList: represents list of element on the website
    """

    def __init__(self, name, url, root, title, **kwargs):
        super(ElementList, self).__init__(name, url, root)
        self.title = title
        for key, value in kwargs.items():
            if key == 'avatar':
                self.avatar = value
            if key == 'sapo':
                self.sapo = value

    @property
    def title(self):
        return self._title

    @title.setter
    def title(self, value):
        if value is True:
            li = self.root.find('li')
            titles = []
            for item in li:
                title_doc = item.xpath('//a[not(img)]')
                titles.append(title_doc[0].text)
            self._title = titles

    @property
    def avatar(self):
        return self._avatar

    @avatar.setter
    def avatar(self, value):
        if value is True:
            avatar_doc = self.root.xpath('//img')
            self._avatar = avatar_doc

    @property
    def sapo(self):
        return self._sapo

    @sapo.setter
    def sapo(self, value):
        if value is True:
            sapo_docs = self.root.xpath('//p')
            sapo = [item.text for item in sapo_docs]
            self._sapo = sapo


class BoxMetaClass(type):
    """
    Metaclass for all boxs.
    """

    def __new__(cls, name, bases, attrs):
        _url = None

        # Also ensure initialization is only performed for subclasses of Model.
        # (excluding Box class itself).
        parents = [b for b in bases if isinstance(b, BoxMetaClass)]
        if not parents:
            return super(BoxMetaClass, cls).__new__(cls, name, bases, attrs)

        # Check does class have URL object?
        # If does: using requests to get html content
        # If does not: get <html> content to verify
        flag = True
        for key, value in attrs.items():
            if isinstance(value, URL):
                flag = False

        if not flag:
            for key, value in attrs.items():
                if isinstance(value, BaseElement):
                    pass

        mappings = dict()
        removes = dict()
        for key, value in attrs.items():
            # If attribute is URL object, attach url for Box class as an attribute.
            if isinstance(value, URL):
                attrs['url'] = value.url
                _url = value.url
                removes[key] = value
            # Get all attrs that are instances of Element class.
            # And store them into ``mappings``.
            if isinstance(value, BaseElement):
                mappings[key] = value
                value.url = _url
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

            The Box class will automatically generate method named ``verify_text_of_box_title`` if you call this.
        """

        for key, value in self.__mappings__.items():
            if item == 'verify_text_list' + key:
                return lambda: self.base_verify_list_text(value)

    @staticmethod
    def base_verify_list_text(element_list):
        list_text = element_list.sapo
        return list_text
