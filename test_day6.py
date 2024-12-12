import time
from selenium.webdriver.support import expected_conditions as EC

from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.alert import Alert
from selenium.webdriver.support.ui import Select
from selenium.webdriver.support.wait import WebDriverWait

from webdriver_manager.chrome import ChromeDriverManager

import pytest
import allure

@pytest.mark.smoke
@pytest.fixture()
def test_verifyURL():
    global driver
    options=webdriver.ChromeOptions()
    options.add_experimental_option("detach",True)
    s=Service('C:\\Users\\ankits.jain_infobean\\Downloads\\chromedriver-win64\\chromedriver-win64\\chromedriver.exe')
    driver=webdriver.Chrome(options=options,service=s)
    driver.get("https://demowebshop.tricentis.com/")
# --------------------------------------------------------------------------------------------------
# pytest

@allure.feature("Additional")
@pytest.mark.Regression
@pytest.mark.login
def test_clickBooks(test_verifyURL):
    driver.find_element("xpath","(//a[contains(text(),'Books')])[1]").click()

@pytest.mark.skip("skipping")
def test_clicklogout():
    print("this is just sample one")

@pytest.mark.skip("skipping")
def test_clicklogout():
    print("this is just sample one")

@pytest.mark.smoke
def test_clickComputers():
    driver.find_element('xpath', "(//a[contains(text(),'Computers')])[1]").click()

