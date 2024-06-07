import pytest

@pytest.fixture(scope='function')
def dbconnection():
    print("open the db connection")
    yield
    print("close db connection")

@pytest.mark.usefixtures("dbconnection")
def test_create_table():
    print("created table")

@pytest.mark.usefixtures("dbconnection")
def test_delete_table():
    print("deleted table")

