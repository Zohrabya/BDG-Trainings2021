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
    #go to the product view page
    browser.find_element_by_xpath('//div[@class = "inventory_item_name"]').click()
    time.sleep(5)
    product_name = browser.find_element_by_class_name("inventory_details_name").text
    #Test case N1. Test if there is the "Add to cart" button on the product view page
    try:
        add_button = browser.find_element_by_xpath('//button[text()="Add to cart"]')
        print("Test N1 passed")
    except NoSuchElementException:
        print("Test N1 failed")
    #Test case N2. Test if after clicking on the "Add to cart" button it changes to "Remove" button
    add_button.click()
    time.sleep(3)
    try:
        remove_button = browser.find_element_by_xpath('//button[text()="Remove"]')
        print("Test N2 passed")
    except NoSuchElementException:
        print("Test N2 failed")
    #Test case N3. Test if after clicking on the "Add to cart" button it appears in the shopping cart
    shopping_cart_link = browser.find_element_by_class_name("shopping_cart_link")
    shopping_cart_link.click()
    time.sleep(5)
    added_products_names = browser.find_elements_by_class_name("inventory_item_name")
    for n in range(0, len(added_products_names)):
        added_products_names[n] = added_products_names[n].text
    try:           
        assert product_name in added_products_names
        print("Test N3 passed")
    except AssertionError:
        print("Test N3 failed")
    #Test case N4. Test if after clicking on the "Remove" button on the product view page it changes to "Add to cart" button
    browser.execute_script("window.history.go(-1)")
    time.sleep(3)
    browser.find_element_by_xpath('//button[text()="Remove"]').click()
    try:
        add_button = browser.find_element_by_xpath('//button[text()="Add to cart"]')
        print("Test N4 passed")
    except NoSuchElementException:
        print("Test N4 failed")
    #Test case N5. Test if after clicking on the "Remove" button on the product view page the product dissapears from the shopping cart
    browser.find_element_by_class_name("shopping_cart_link").click()
    time.sleep(5)
    added_products_names = browser.find_elements_by_class_name("inventory_item_name")
    for n in range(0, len(added_products_names)):
        added_products_names[n] = added_products_names[n].text
    try:           
        assert product_name not in added_products_names
        print("Test N5 passed")
    except AssertionError:
        print("Test N5 failed")

finally:
    time.sleep(3)
    browser.quit()
