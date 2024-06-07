import pytest

class Testclass:

    def setup_class(cls):
        print("API Connection is opened")

    def teardown_class(cls):
        print("API Connection is closed")

    def setup_method(self, method):
        print("Open browser")

    def teardown_method(self, method):
        print("Close browser")

    def testcase1(self):
        print("testcase1 is executed")

    def testcase2(self):
        print("testcase2 is executed")

    def testcase3(self):
        print("testcase3 is executed")

