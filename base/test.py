import sys
from os.path import dirname, abspath
sys.path.insert(0, dirname(dirname(abspath(__file__))))
from tests.config_test import get_driver

a = get_driver()
b = get_driver()


