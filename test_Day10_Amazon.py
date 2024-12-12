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



@pytest.fixture()

def test_verifyURL():
    global driver
    options=webdriver.ChromeOptions()
    options.add_experimental_option("detach",True)
    s=Service('C:\\Users\\ankits.jain_infobean\\Downloads\\chromedriver-win64\\chromedriver-win64\\chromedriver.exe')
    driver=webdriver.Chrome(options=options,service=s)
    driver.implicitly_wait(10)
    driver.get("https://www.amazon.in/")
    driver.maximize_window()
    time.sleep(10)

def test_captcha(test_verifyURL):
    driver.find_element("xpath", "//button[@class='a-button-text']").click()

def test_login():
    driver.find_element("id", "nav-link-accountList-nav-line-1").click()
    driver.find_element("id", "ap_email").send_keys("Dummy@Test.com")
    driver.find_element("id", "continue").click()
    driver.find_element("id", "ap_password").send_keys("Dummy@12345")
    driver.find_element("id", "signInSubmit").click()

def test_addtocart():
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
    driver.switch_to.frame("ApxSecureIframe")
    driver.find_element("xpath", "//input[@name='addCreditCardNumber']").send_keys("374245455400126")
    driver.find_element("xpath", "//input[@name='ppw-accountHolderName']").send_keys("Test Man")
    exp_date= driver.find_element("xpath", "//select[@name='ppw-expirationDate_month']")
    sel=Select(exp_date)
    sel.select_by_visible_text("05")
    exp_year= driver.find_element("xpath", "//select[@name='ppw-expirationDate_year']")
    sel=Select(exp_year)
    sel.select_by_visible_text("2026")
    driver.find_element("xpath", "//input[@name='ppw-widgetEvent:AddCreditCardEvent']").click()

