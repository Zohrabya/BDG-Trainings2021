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
    products = browser.find_elements_by_xpath("//button[text() = 'Add to cart']")
    for p in products:
        p.click()
    time.sleep(5)
    #Open the shopping cart page
    shopping_cart_link = browser.find_element_by_class_name("shopping_cart_link")
    shopping_cart_link.click()
    time.sleep(5)
    products_in_the_cart = browser.find_elements_by_class_name("inventory_item_name")
    for i in range(0, len(products_in_the_cart)):
        products_in_the_cart[i] = products_in_the_cart[i].text
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
    #Click the "Continue" button and go to the checkout second page
    continue_button = browser.find_element_by_id("continue")
    continue_button.click()
    time.sleep(3)
    #Test case N1. Test if the all added to the cart products are correctly shown on the checkout second page
    products_checkout = browser.find_elements_by_class_name("inventory_item_name")
    for i in range(0, len(products_checkout)):
        products_checkout[i] = products_checkout[i].text
    print(products_checkout)
    print(products_in_the_cart)  
    try:
        assert products_checkout == products_in_the_cart
        print("Test case N1 passed")
    except AssertionError:
        print("Test case N1 failed")
    #Test case N2. Test if the total price is shown correctly on the checkout second page
    item_prices = browser.find_elements_by_class_name("inventory_item_price")
    for i in range(0, len(item_prices)):
        item_prices[i] = float(item_prices[i].text[1:])
    items_total = browser.find_element_by_class_name("summary_subtotal_label").text[13:]
    items_total = int(items_total)
    
    try:
        assert sum(item_prices) == items_total
        print("Test case N2 passed")
    except:
        print("Test case N2 failed")
    
finally:
    time.sleep(3)
    browser.quit()
    