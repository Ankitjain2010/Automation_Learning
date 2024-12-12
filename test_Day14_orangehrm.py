import pytest
from selenium import webdriver
from LoginPage import LoginPage
from selenium.webdriver.chrome.service import Service


@pytest.fixture(scope="module")
def test_verifyURL():
    options=webdriver.ChromeOptions()
    options.add_experimental_option("detach",True)
    s=Service('C:\\Users\\ankits.jain_infobean\\Downloads\\chromedriver-win64\\chromedriver-win64\\chromedriver.exe')
    driver=webdriver.Chrome(options=options,service=s)
    driver.get("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")
    driver.maximize_window()


def test_valid_login(test_verifyURL):
    driver = test_verifyURL
    login_page = LoginPage(driver)

    login_page.enter_username("Admin")
    login_page.enter_password("admin123")
    login_page.click_login_button()
    # Perform valid login
    # login_page.login("Admin", "admin123")