import pytest

def testcase1():
    print("testcase1 is executed")

def testcase2():
    print("testcase2 is executed")

def test_case3():
    print("testcase3 is executed")

def case_test():
    print("testcase4 is executed")

def case_test5():
    print("testcase5 is executed")

def login():
    print("testcase6 is executed")

def test_case7():
    assert 1==2
    print("testcase7 is executed")

# pytest -v .\test_dicovery.py