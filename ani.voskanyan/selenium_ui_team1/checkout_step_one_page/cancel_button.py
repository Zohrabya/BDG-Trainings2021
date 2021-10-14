#The test case was written by Ani Voskanyan
#!/usr/bin/env python3

from selenium import webdriver
import time
from selenium.common.exceptions import NoSuchElementException

browser = webdriver.Chrome()
link = "https://www.saucedemo.com/"
browser.get(link)

try:
    #log in 
    username_input_field = browser.find_element_by_css_selector('input[placeholder = "Username"]')
    username_input_field.send_keys('standard_user')
    password_input_field = browser.find_element_by_css_selector('input[placeholder = "Password"]')
    password_input_field.send_keys('secret_sauce')
    browser.find_element_by_class_name('submit-button').click()
    time.sleep(3)
    #Add a product into the shopping cart
    browser.find_element_by_xpath("//button[text() = 'Add to cart']").click()
    time.sleep(5)
    #Open the shopping cart page
    shopping_cart_link = browser.find_element_by_class_name("shopping_cart_link")
    shopping_cart_link.click()
    time.sleep(5)
    #Go to the checkout first page
    checkout_button = browser.find_element_by_id("checkout")
    checkout_button.click()
    time.sleep(3)
    #Test case N1. Test if there is the "Cancel" button on the checkout first page
    try:
        cancel_button = browser.find_element_by_xpath("//button[text() = 'Cancel']")
        print("Test case N1 passed")
    except NoSuchElementException:
        print("Test case N2 failed")
    #Test case N2. Test if after clicking on the the "Cancel" a user is redirected back to the shopping cart page
    cancel_button.click()
    time.sleep(3)
    page_title = browser.find_element_by_class_name("title").text.lower()
    try:
        assert page_title == 'your cart'
        print("Test case N2 passed")
    except AssertionError:
        print("Test case N2 failed")

finally:
    time.sleep(3)
    browser.quit()
