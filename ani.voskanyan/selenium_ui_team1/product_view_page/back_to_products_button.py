#The test case was written by Ani Voskanyan
#!/usr/bin/env python3

from selenium import webdriver
import time

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
    time.sleep(2)
    #go to the product view page
    browser.find_element_by_xpath('//div[@class = "inventory_item_name"]').click()
    time.sleep(2)
    #Test case N1. Test if there is the "Back to products" button on the product view page
    back_button = browser.find_element_by_id("back-to-products")
    button_text = back_button.text

    try:
        assert button_text.lower() == "back to products"
        print("Test case N1 passed")
    except AssertionError:
        print("Failed. Wrong name of the button")
    time.sleep(2)
    #Test case N2. Test if the button "Back to products" works properly
    back_button.click()
    time.sleep(2)
    page_title = browser.find_element_by_class_name("title").text
    try:
        assert page_title.lower() == "products"
        print("Test case N2 passed")
    except AssertionError:
        print("Failed")

finally:
    time.sleep(2)
    browser.quit()
