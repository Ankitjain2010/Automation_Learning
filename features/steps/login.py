
from behave import *

import json
import time
import csv
import logging

import yaml
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
import pytest
from selenium.webdriver.common.by import By

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger()


@given(u'open  HRM browser')
def step_impl(context):
    global driver
    options = webdriver.ChromeOptions()
    options.add_argument('--headless')
    options.add_experimental_option("detach", True)
    s = Service("C:\\Users\\ankits.jain_infobean\\Downloads\\chromedriver-win64\\chromedriver-win64\\chromedriver.exe")
    driver = webdriver.Chrome(options=options, service=s)
    driver.implicitly_wait(10)
    driver.get("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")
    driver.maximize_window()


@when(u'enter valid credental username1 "Admin" and password1 "admin123"')
def step_impl(context):
    driver.find_element("name", "username").send_keys("Admin")
    driver.find_element("name", "password").send_keys("admin123")



@then(u'click login button1')
def step_impl(context):
    driver.find_element("xpath", "//button[@type='submit']").click()



@then(u'Home page loaded successfully1')
def step_impl(context):
    # logging.info("completed")
    # print("completed")
    logger.info("printed")


# -------------------------------------------------------------------