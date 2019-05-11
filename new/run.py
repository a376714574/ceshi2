import unittest

from new import HQ

a=unittest.TestSuite()
a.addTest(unittest.TestLoader().loadTestsFromModule(HQ))
unittest.TextTestRunner().run(a)