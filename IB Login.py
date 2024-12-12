import time

from selenium.webdriver.edge.service import Service
from selenium.webdriver.support import expected_conditions as EC

from selenium import webdriver
from selenium.webdriver import ActionChains
# from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.alert import Alert
from selenium.webdriver.support.ui import Select
from selenium.webdriver.support.wait import WebDriverWait

options=webdriver.EdgeOptions()
# options.add_experimental_option("detach",True)
s=Service('C:\\Users\\ankits.jain_infobean\\Downloads\\edgedriver_win64\\msedgedriver.exe')
driver=webdriver.Edge(options=options,service=s)

driver.implicitly_wait(5)
time.sleep(2)
driver.get("http://www.yahoo.com")
time.sleep(5)
driver.find_element("id", "ft_un").send_keys("ankits.jain")
driver.find_element("id", "ft_pd").send_keys("info@123")
driver.find_element("xpath", "//button[@type='submit']").click()