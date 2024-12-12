Feature: Executing first bdd tetscase
  Scenario:Login username and password validation
    Given open  HRM browser
    When enter valid credental username1 "Admin" and password1 "admin123"
    Then click login button1
    And Home page loaded successfully1

#Feature: Add item to cart
#  Scenario:Login with Email and Password and add item to cart
#    Given open demowebshop web
#    When enter valid credental Email "Ankit_tester1@test.com" and Password "Ankit@123"
#    Then click on Computer and Desktop
#    Then click on Add to Cart
#    Then Add to cart
#    Then Go to Shopping Cart and Check out
#    Then Enter Details and Click on Continue
#    Then Click on Confirm
#    And Click on Continue

