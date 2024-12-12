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
# --------------------------------------------------------------------------------------------------
# dropdown: we use Select function and imports "from selenium.webdriver.support.ui import Select"
'''
driver.get("https://demowebshop.tricentis.com/books")
driver.maximize_window()
driver.implicitly_wait(5)
x=driver.find_element("id", "products-orderby")
sel=Select(x)
time.sleep(2)
# sel.select_by_value("https://demowebshop.tricentis.com/books?orderby=6")
# sel.select_by_visible_text("Created on")
sel.select_by_index(1)
'''
# --------------------------------------------------------------------------------------------------
#multiple selection in dropdown
'''
driver.get("https://www.softwaretestingmaterial.com/sample-webpage-to-automate/")
driver.maximize_window()
driver.implicitly_wait(5)
y = driver.find_element("xpath", "(//select[@class ='spTextField'])[1]")
sele=Select(y)
sele.select_by_index(1)
sele.select_by_index(2)
time.sleep(4)
sele.deselect_by_index(2)
'''
# --------------------------------------------------------------------------------------------------
# move to element(hovering) and context click(right click) we use .perform() instead of .click() and
# we import "from selenium.webdriver import ActionChains"
'''
driver.get("https://demowebshop.tricentis.com/")
driver.maximize_window()
driver.implicitly_wait(5)
x=driver.find_element("xpath", "(//a[contains(text(),'Computers')])[1]")
act=ActionChains(driver)
# act.move_to_element(x).perform()
# driver.find_element("xpath", "(//a[contains(text(),'Notebooks')])[1]").click()
act.context_click(x).perform()
'''

# --------------------------------------------------------------------------------------------------
# double click and Alert for OK we use "Accept" and for Cancel we use "dismiss" button in popup
'''
driver.get("https://demo.guru99.com/test/simple_context_menu.html")
driver.maximize_window()
driver.implicitly_wait(5)
db= driver.find_element("xpath", "//button[@ondblclick='myFunction()']")
at=ActionChains(driver)
at.double_click(db).perform()
alert=Alert(driver)
alert.accept()
# alert.dismiss()
'''
# --------------------------------------------------------------------------------------------------
# Drag and Drop
'''
driver.get("https://demo.automationtesting.in/Static.html")
driver.maximize_window()
driver.implicitly_wait(5)
drag= driver.find_element("id", "angular")
drop= driver.find_element("id", "droparea")
ac=ActionChains(driver)
ac.drag_and_drop(drag,drop).perform()
'''

# --------------------------------------------------------------------------------------------------
#