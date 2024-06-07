import pytest

@pytest.mark.one
def test_1():
    print("test1 is executed")

@pytest.mark.one
def test_2():
    print("test2 is executed")

@pytest.mark.sanity
def test_3():
    print("test3 is executed")