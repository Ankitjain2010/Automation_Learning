#For Captcha use time.sleep() and enter captcha manually
import time

from select import select
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select

from webdriver_manager.chrome import ChromeDriverManager
options=webdriver.ChromeOptions()
options.add_experimental_option("detach",True)
s=Service('C:\\Users\\ankits.jain_infobean\\Downloads\\chromedriver-win64\\chromedriver-win64\\chromedriver.exe')
driver=webdriver.Chrome(options=options,service=s)
driver.get("https://toolsqa.com/selenium-training?q=banner#enroll-form")
driver.maximize_window()

driver.find_element("id", "first-name").send_keys("Ankit")
driver.find_element("id", "last-name").send_keys("Jain")
driver.find_element("id", "email").send_keys("ankitjain@test.com")
driver.find_element("id", "mobile").send_keys("9876543210")
country = driver.find_element("id","country")
sel = Select(country)
sel.select_by_visible_text("India")
driver.find_element("id", "city").send_keys("Indore")
driver.find_element("id", "message").send_keys("Ticket Booking")
time.sleep(10)
driver.find_element("xpath", "//button[@class='btn btn-block btn-primary']").click()
