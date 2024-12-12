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
# -------------------------------------------------------------------------------------------
# driver.get("https://www.amazon.in/")
# driver.maximize_window()
# driver.implicitly_wait(5)
# # driver.save_screenshot("C:\\Users\\ankits.jain_infobean\\Documents\\Python Learning\\test1.jpeg")
#
# # driver.execute_script("window.scrollBy(0,1000);")
# # driver.execute_script("window.scrollBy(0,-1000);")
#
# driver.find_element("id", "twotabsearchtextbox").send_keys("Iphone 15")
# time.sleep(3)
# driver.find_element("id", "nav-search-submit-button").click()
#
# a = driver.find_element("xpath", "//span[contains(text(),'Apple iPhone 15 (128 GB) - Black')]")
# # driver.execute_script("window.scrollBy(0,a)")
# driver.execute_script("arguments[0].scrollIntoView();", a)

# ------------------------------------------------------------------------------------------
'''
driver.get("https://the-internet.herokuapp.com/nested_frames")
driver.maximize_window()
# driver.implicitly_wait(5)
driver.switch_to.frame("frame-top")
print("shifted to top")

driver.switch_to.frame("frame-left")
print("shifted to left")

driver.switch_to.parent_frame()
print("parent")

driver.switch_to.frame("frame-middle")
print("shifted to middle")

driver.switch_to.parent_frame()
print("parent2")

driver.switch_to.frame("frame-right")
print("shifted to right")

driver.switch_to.default_content()
print("default")

driver.switch_to.frame("frame-bottom")
print("shifted to bottom")

driver.switch_to.parent_frame()
print("parent4")
'''

driver.get("https://the-internet.herokuapp.com/iframe")
driver.maximize_window()
driver.implicitly_wait(5)
driver.switch_to.frame("mce_0_ifr")
driver.find_element("xpath", "//button[@class='tox-notification__dismiss tox-button tox-button--naked tox-button--icon']").click()
driver.switch_to.frame("mce_0_ifr")
print("switched")
