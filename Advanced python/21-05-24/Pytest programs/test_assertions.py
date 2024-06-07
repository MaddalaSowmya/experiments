import pytest

def test_simple_assertion():
    assert 1+1==2

def testequal_assertion():
    x=5
    y=5
    assert x==y

def test_not_equal_assertion():
    x=5
    y=7
    assert x!=y

def test_in_assertion():
    x=[78,56,324,90,67]
    assert 56 in x

def test_not_in_assertion():
    x = [78, 56, 324, 90, 67]
    assert 516 not in x

def test_identity_assertion():
    a = ['a','e','i','o','u']
    b = a
    assert a is b