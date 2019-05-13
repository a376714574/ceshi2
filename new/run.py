import unittest
import  HTMLTestRunnerNew
import sys

sys.path.append("././")
print(sys.path)

from new import HQ

with open("test.html","wb") as file:
    a=unittest.TestSuite()
    a.addTest(unittest.TestLoader().loadTestsFromModule(HQ))
    # unittest.TextTestRunner().run(a)
    HTMLTestRunnerNew.HTMLTestRunner(stream=file).run(a)

