import pytest
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.microsoft import EdgeChromiumDriverManager

# testcase1
def testcase1():
    print("testcase1 executed")
    option = webdriver.EdgeOptions()
    driver = webdriver.Edge(options=option)
    driver.maximize_window()
    driver.get("https://www.facebook.com")

# testcase2
def testcase2():
    print("testcase2 executed")
    option = webdriver.EdgeOptions()
    driver = webdriver.Edge(options=option)
    driver.maximize_window()
    driver.get("https://www.instagram.com")

# testcase3
def testcase3():
    print("testcase3 executed")
    option = webdriver.EdgeOptions()
    driver = webdriver.Edge(options=option)
    driver.maximize_window()
    driver.get("https://twitter.com")

# testcase4
def testcase4():
    print("testcase1 executed")
    option = webdriver.EdgeOptions()
    driver = webdriver.Edge(options=option)
    driver.maximize_window()
    driver.get("https://www.google.com")
