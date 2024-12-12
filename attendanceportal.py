import time

from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.ui import Select

from webdriver_manager.chrome import ChromeDriverManager

options=webdriver.ChromeOptions()
options.add_experimental_option("detach",True)
s=Service('C:\\Users\\ankits.jain_infobean\\Downloads\\chromedriver-win64\\chromedriver-win64\\chromedriver.exe')
driver=webdriver.Chrome(options=options,service=s)

driver.get("https://attendance.creatingwow.in/#/login")
driver.maximize_window()
driver.implicitly_wait(5)

driver.find_element("id", "ius-userid").send_keys("ankits.jain@infobeans.com")
driver.find_element("id", "ius-password").send_keys("Ankit@123")
driver.find_element("id", "ius-sign-in-submit-btn-text").click()

driver.find_element("xpath", "//i[@class='fa fa-calendar-check-o']").click()