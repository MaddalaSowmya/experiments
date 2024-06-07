import pytest

def setup_module(module):
    print("DB Connection is opened")

def teardown_module(module):
    print("DB Connection is closed")


def testcase1():
    print("testcase1 is executed")

def testcase2():
    print("testcase2 is executed")

def testcase3():
    print("testcase3 is executed")