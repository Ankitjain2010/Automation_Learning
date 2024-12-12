import time

from selenium import webdriver
from selenium.webdriver.chrome.service import Service

from webdriver_manager.chrome import ChromeDriverManager

options=webdriver.ChromeOptions()
options.add_experimental_option("detach",True)
s=Service('C:\\Users\\ankits.jain_infobean\\Downloads\\chromedriver-win64\\chromedriver-win64\\chromedriver.exe')
driver=webdriver.Chrome(options=options,service=s)
driver.get("https://demowebshop.tricentis.com/")
driver.maximize_window()
driver.implicitly_wait(5)
# For Registration:
# driver.find_element("xpath", "//a[text()='Register']").click()
# driver.find_element("id", "gender-male").click()
# driver.find_element("id", "FirstName").send_keys("Ankit")
# driver.find_element("id", "LastName").send_keys("Jaim")
# driver.find_element("id", "Email").send_keys("Ankit_tester2@test.com")
# driver.find_element("id", "Password").send_keys("Ankit@123")
# driver.find_element("id", "ConfirmPassword").send_keys("Ankit@123")
# driver.find_element("id", "register-button").click()
# driver.find_element("xpath", "//input[@value='Continue']").click()

# For Login:
driver.find_element("link text", 'Log in').click()
driver.find_element("id", "Email").send_keys("Ankit_tester1@test.com")
driver.find_element("id", "Password").send_keys("Ankit@123")
driver.find_element("xpath", "(//input[@type='submit'])[2]").click()
driver.find_element("xpath", "(//a[contains(text(), 'Computers')])[3]").click()
driver.find_element("xpath", "(//a[contains(text(), 'Desktops')])[4]").click()
driver.find_element("xpath", "(//input[@value ='Add to cart'])[1]").click()
driver.find_element("id", "add-to-cart-button-72").click()
Tag=driver.find_element("partial link text", "Shopping cart")
print(Tag.text)
print(Tag.tag_name)
Tag.click()