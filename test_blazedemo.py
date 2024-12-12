

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.ui import Select
import pytest


@pytest.fixture()

def test_verifyURL():
    global driver
    options=webdriver.ChromeOptions()
    options.add_experimental_option("detach",True)
    s=Service('C:\\Users\\ankits.jain_infobean\\Downloads\\chromedriver-win64\\chromedriver-win64\\chromedriver.exe')
    driver=webdriver.Chrome(options=options,service=s)
    driver.get("https://blazedemo.com/")
    driver.maximize_window()

def test_destination(test_verifyURL):
    c1=driver.find_element("xpath", "//select[@name='fromPort']")
    sel1=Select(c1)
    sel1.select_by_value("Boston")

    c2=driver.find_element("xpath", "//select[@name='toPort']")
    sel2=Select(c2)
    sel2.select_by_value("Berlin")

    driver.find_element("xpath", "//input[@type='submit']").click()

def test_chooseflight():
    driver.find_element("xpath", "(//input[@type='submit'])[3]").click()

def test_personaldata():
    driver.find_element("id", "inputName").send_keys("Ankit")
    driver.find_element("id", "address").send_keys("Test")
    driver.find_element("id", "city").send_keys("Indore")
    driver.find_element("id", "state").send_keys("MP")
    driver.find_element("id", "zipCode").send_keys("452002")

    c3=driver.find_element("xpath", "//select[@name='cardType']")
    sel3=Select(c3)
    sel3.select_by_value("amex")

    driver.find_element("id", "creditCardNumber").send_keys("1234567890123456")
    driver.find_element("id", "creditCardMonth").send_keys("08")
    driver.find_element("id", "creditCardYear").send_keys("2030")
    driver.find_element("id", "nameOnCard").send_keys("Ankit Jain")

    driver.find_element("xpath", "//input[@type='submit']").click()