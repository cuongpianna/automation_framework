import unittest
import sys
import os
import time
from os.path import dirname, abspath

sys.path.insert(0, dirname(dirname(abspath(__file__))))

from tests.home_test import HomeTest

tc1 = unittest.TestLoader().loadTestsFromTestCase(HomeTest)

smokeTest = unittest.TestSuite([tc1])
unittest.TextTestRunner(verbosity=2).run(smokeTest)
