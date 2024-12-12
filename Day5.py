import time
from selenium.webdriver.support import expected_conditions as EC

from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.alert import Alert
from selenium.webdriver.support.ui import Select
from selenium.webdriver.support.wait import WebDriverWait

from webdriver_manager.chrome import ChromeDriverManager

options=webdriver.ChromeOptions()
options.add_experimental_option("detach",True)
s=Service('C:\\Users\\ankits.jain_infobean\\Downloads\\chromedriver-win64\\chromedriver-win64\\chromedriver.exe')
driver=webdriver.Chrome(options=options,service=s)
# --------------------------------------------------------------------------------------------------
#Synchronization
'''
driver.implicitly_wait(5)
driver.get("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")
driver.maximize_window()
driver.find_element("xpath", "//input[@name='username']").send_keys("Admin")
driver.find_element("xpath", "//input[@name='password']").send_keys("admin123")
driver.find_element("xpath", "//button[@type='submit']").click()

clickable_element= WebDriverWait(driver, 10)
try:
    clickable_element.until(EC.title_contains("OrangeM"))
    print("Action completed")
except:
    print("Action not completed")
finally:
    print("Action done")
'''
#-----------------------------------------------------------------------------------------------------
driver.implicitly_wait(5)
driver.get("https://toolsqa.com/")
driver.maximize_window()

driver.find_element("link text", "DEMO SITE").click()

main_window_handle = driver.current_window_handle

# Get all window handles (including the main window and the new tab)
all_window_handles = driver.window_handles
# if len(all_window_handles) > 1:
# # Find the handle of the new tab (excluding the main window handle)
new_tab_handle = [handle for handle in all_window_handles if handle != main_window_handle][0]
#
# # Switch to the new tab
driver.switch_to.window(new_tab_handle)

driver.find_element("xpath", "//img[@alt='Selenium Online Training']").click()
# main_window_handle = driver.current_window_handle
# all_window_handles = driver.window_handles
# new_tab_handle = [handle for handle in all_window_handles if handle != main_window_handle][0]
driver.switch_to.window(new_tab_handle)

all_window_handles = driver.window_handles
current_window_handle = driver.current_window_handle
new_tab_handle = [handle for handle in all_window_handles if handle != current_window_handle and handle != main_window_handle][0]
driver.switch_to.window(new_tab_handle)

driver.find_element("xpath", "//a[@class='btn btn-primary-shadow btn-block']").click()


