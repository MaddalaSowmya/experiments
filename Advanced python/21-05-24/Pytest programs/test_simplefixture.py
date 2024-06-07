import pytest

@pytest.fixture
def simple_data():
    return 42

# test simple fixture
def test_simple_data(simple_data):
    assert simple_data==42