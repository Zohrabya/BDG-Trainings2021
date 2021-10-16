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
    #Fill the form
    first_name = browser.find_element_by_id("first-name")
    first_name.send_keys("Ani")
    last_name = browser.find_element_by_id("last-name")
    last_name.send_keys("Voskanyan")
    zip_post_code = browser.find_element_by_id("postal-code")  
    zip_post_code.send_keys("0054")
    #Test case 1. Test if a user is rederected to the checkout second page after clicking on the "Continue" button
    continue_button = browser.find_element_by_id("continue")
    continue_button.click()
    time.sleep(3)
    try:
        assert "checkout: overview" in browser.find_element_by_class_name("title").text.lower()
        print("Test case N1 passed")
    except AssertionError:
        print("Test case N1 failed")
    
finally:
    time.sleep(3)
    browser.quit()
    