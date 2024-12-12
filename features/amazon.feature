Feature: Login to Amazon and add item
  Scenario:Login to Amazon and add a card for payment
    Given open Amzaom
    When enter valid credental username1 "ankitjain201089@gmail.com" and password1 "Ankit@12345"
    Then Search a item and add to cart
    And Add credit card