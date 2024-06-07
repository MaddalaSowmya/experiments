import pytest

def setup_function(function):
    print("\nOpening the browser")

def teardown_function(function):
    print("\nClosing the browser")

def testcase1():
    print("testcase1 is executed")

def testcase2():
    print("testcase2 is executed")

def testcase3():
    print("testcase3 is executed")