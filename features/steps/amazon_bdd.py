
from behave import *

import json
import time
import csv
import logging

import yaml
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.ui import Select
import pytest
from selenium.webdriver.common.by import By

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger()


@given(u'open Amzaom')
def step_impl(context):
    global driver
    options = webdriver.ChromeOptions()
    options.add_experimental_option("detach", True)
    s = Service('C:\\Users\\ankits.jain_infobean\\Downloads\\chromedriver-win64\\chromedriver-win64\\chromedriver.exe')
    driver = webdriver.Chrome(options=options, service=s)
    driver.implicitly_wait(10)
    driver.get("https://www.amazon.in/")
    driver.maximize_window()
    time.sleep(10)

@when(u'enter valid credental username1 "ankitjain201089@gmail.com" and password1 "Ankit@12345"')
def step_impl(context):
    driver.find_element("xpath", "//button[@class='a-button-text']").click()
    driver.find_element("id", "nav-link-accountList-nav-line-1").click()
    driver.find_element("id", "ap_email").send_keys("ankitjain201089@gmail.com")
    driver.find_element("id", "continue").click()
    driver.find_element("id", "ap_password").send_keys("Ankit@12345")
    driver.find_element("id", "signInSubmit").click()


@then(u'Search a item and add to cart')
def step_impl(context):
    driver.find_element("id", "twotabsearchtextbox").send_keys("iphone 13 128gb")
    driver.find_element("id", "nav-search-submit-button").click()
    a = driver.find_element("xpath", "//span[contains(text(),'Apple iPhone 13 (128GB) - Starlight')]")
    # driver.execute_script("window.scrollBy(0,a)")
    driver.execute_script("arguments[0].scrollIntoView();", a)
    driver.find_element("id", "a-autoid-6-announce").click()
    driver.find_element("id", "nav-cart-count").click()
    driver.find_element("xpath", "//input[@name='proceedToRetailCheckout']").click()
    time.sleep(5)
    driver.find_element("xpath", "(//Input[@type='radio'])[8]").click()
    time.sleep(5)
    driver.find_element("link text", "Enter card details").click()



@then(u'Add credit card')
def step_impl(context):
    time.sleep(5)
    driver.switch_to.frame("ApxSecureIframe")
    driver.find_element("xpath", "//input[@name='addCreditCardNumber']").send_keys("374245455400126")
    driver.find_element("xpath", "//input[@name='ppw-accountHolderName']").send_keys("Test Man")
    exp_date = driver.find_element("xpath", "//select[@name='ppw-expirationDate_month']")
    sel = Select(exp_date)
    sel.select_by_visible_text("05")
    exp_year = driver.find_element("xpath", "//select[@name='ppw-expirationDate_year']")
    sel = Select(exp_year)
    sel.select_by_visible_text("2026")
    driver.find_element("xpath", "//input[@name='ppw-widgetEvent:AddCreditCardEvent']").click()