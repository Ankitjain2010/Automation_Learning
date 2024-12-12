import time

from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.alert import Alert
from selenium.webdriver.support.ui import Select

from webdriver_manager.chrome import ChromeDriverManager

options=webdriver.ChromeOptions()
options.add_experimental_option("detach",True)
s=Service('C:\\Users\\ankits.jain_infobean\\Downloads\\chromedriver-win64\\chromedriver-win64\\chromedriver.exe')
driver=webdriver.Chrome(options=options,service=s)

driver.get("https://dev1-validation-iqviaconsent.compltech.iqvia.com/landing?lab-code=iqvia")
driver.maximize_window()
driver.implicitly_wait(5)

driver.find_element("id", "butAcceptCookie-AcceptAll").click()
driver.find_element("xpath", "//div[@class ='btn btn-light ads-land-btn ']").click()
driver.find_element("id", "butAcceptCookie-AcceptAll").click()

salutation=driver.find_element("id", "salutation")
sel1=Select(salutation)
sel1.select_by_value("216")

driver.find_element("id", "firstname").send_keys("Test004")
driver.find_element("id", "lastname").send_keys("Yellow")
driver.find_element("id", "doctor_specialty_1").send_keys("Physician")
driver.find_element("id", "tax_idObfuscated").send_keys("Tax@004")
driver.find_element("id", "npi_idObfuscated").send_keys("UCI@004")
driver.find_element("id", "hcp_username").send_keys("Test004")

AddTyp=driver.find_element("id", "address_type")
sel1=Select(AddTyp)
sel1.select_by_value("213")

driver.find_element("id", "postal_code").send_keys("SW1W 0NY")
driver.find_element("id", "city").send_keys("Hyderabad")
driver.find_element("id", "state").send_keys("Hydera")
driver.find_element("id", "address_line").send_keys("320 MG Road")
driver.find_element("id", "workplace_name").send_keys("RAW")
driver.find_element("xpath", "(//button[@class='btn btn-primary sadmin-search-btn-padclass'])[1]").click()
driver.find_element("id", "channel_value").send_keys("test4@tester.com")
driver.find_element("xpath", "(//button[@class='btn btn-primary sadmin-search-btn-padclass'])[2]").click()
driver.find_element("id", "show-legal-message-block").click()
driver.find_element("xpath", "(//button[@class='btn btn-primary'])[1]").click()
driver.find_element("id", "btn_sign_action").click()