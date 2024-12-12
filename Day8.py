import time

import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.keys import Keys

@pytest.fixture()
def test_URL():
    # Set up WebDriver
    global driver

    options = webdriver.ChromeOptions()
    options.add_experimental_option("detach", True)
    s=Service('C:\\Users\\ankits.jain_infobean\\Downloads\\chromedriver-win64\\chromedriver-win64\\chromedriver.exe')
    driver = webdriver.Chrome(options=options, service=s)
    driver.get("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")
    driver.maximize_window()
    time.sleep(3)

# Parameterize test with different usernames and passwords
@pytest.mark.parametrize(
    "username, password",
    [
        ("Admin", "admin123"),       # Valid credentials
        ("invalid_user", "admin123"), # Invalid username
        ("Admin", "wrongpassword"),  # Invalid password
        ("", ""),                    # Empty credentials
    ]
)
def test_login(test_URL, username, password):
    # Locate and interact with username field
    username_field = driver.find_element("name", "username")
    username_field.send_keys(username)

    # Locate and interact with password field
    password_field = driver.find_element("name", "password")
    #password_field.clear()
    password_field.send_keys(password)

    # Click login button
    login_button = driver.find_element("xpath", "//button[@type='submit']")
    login_button.click()