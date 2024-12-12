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

@given(u'open demowebshop web')
def step_impl(context):
    global driver
    options = webdriver.ChromeOptions()
    options.add_experimental_option("detach", True)
    s = Service('C:\\Users\\ankits.jain_infobean\\Downloads\\chromedriver-win64\\chromedriver-win64\\chromedriver.exe')
    driver = webdriver.Chrome(options=options, service=s)
    driver.get("https://demowebshop.tricentis.com/")
    driver.maximize_window()
    driver.implicitly_wait(5)


@when(u'enter valid credental Email "Ankit_tester1@test.com" and Password "Ankit@123"')
def step_impl(context):
    driver.find_element("link text", 'Log in').click()
    driver.find_element("id", "Email").send_keys("Ankit_tester1@test.com")
    driver.find_element("id", "Password").send_keys("Ankit@123")
    driver.find_element("xpath", "(//input[@type='submit'])[2]").click()

@then(u'click on Computer and Desktop')
def step_impl(context):
    driver.find_element("xpath", "(//a[contains(text(), 'Computers')])[3]").click()
    driver.find_element("xpath", "(//a[contains(text(), 'Desktops')])[4]").click()


@then(u'click on Add to Cart')
def step_impl(context):
    driver.find_element("xpath", "(//input[@value ='Add to cart'])[1]").click()


@then(u'Add to cart')
def step_impl(context):
    driver.find_element("id", "add-to-cart-button-72").click()


@then(u'Go to Shopping Cart and Check out')
def step_impl(context):
    driver.find_element("xpath", "(//span[@class='cart-label'])[1]").click()
    driver.find_element("id", "termsofservice").click()
    driver.find_element("id", "checkout").click()


@then(u'Enter Details and Click on Continue')
def step_impl(context):
    driver.find_element("xpath","(//input[@type='button'])[2]").click()
    driver.find_element("xpath", "(//input[@type='button'])[3]").click()
    driver.find_element("xpath", "(//input[@type='button'])[4]").click()
    driver.find_element("xpath", "(//input[@type='button'])[5]").click()
    driver.find_element("xpath", "(//input[@type='button'])[6]").click()

@then(u'Click on Confirm')
def step_impl(context):
    driver.find_element("xpath","(//input[@type='button'])[7]").click()
    time.sleep(5)

@then(u'Click on Continue')
def step_impl(context):
    driver.find_element("xpath", "//input[@type='button']").click()

