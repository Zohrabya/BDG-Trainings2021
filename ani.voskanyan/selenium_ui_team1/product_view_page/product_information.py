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
    #find names, prices and photos of th eproducts on inventory page
    inventory_names = browser.find_elements_by_class_name("inventory_item_name")
    inventory_names_text = []
    for name in inventory_names:
        inventory_names_text.append(name.text)
    inventory_prices = browser.find_elements_by_class_name("inventory_item_price")
    inventory_prices_text = []
    for price in inventory_prices:
        inventory_prices_text.append(price.text)
    inventory_photos = browser.find_elements_by_css_selector("img.inventory_item_img")
    inventory_photos_text = []
    for photo in inventory_photos:
        inventory_photos_text.append(photo.get_attribute("src"))
    #find names, prices and photos of th eproducts on the product view page
    product_names = []
    product_prices = []
    product_photos = []

    for n in inventory_names_text:
        browser.find_element_by_xpath(f'//div[text() = "{n}"]').click()
        time.sleep(2)
        product_names.append(browser.find_element_by_class_name("inventory_details_name").text)
        product_prices.append(browser.find_element_by_class_name("inventory_details_price").text)
        product_photos.append(browser.find_element_by_class_name("inventory_details_img").get_attribute('src'))
        back_button = browser.find_element_by_id("back-to-products")
        back_button.click()
        time.sleep(2)

    #Test case N1. Check if names are the same on both pages
    try:
        assert inventory_names_text == product_names
        print("Test case N1 passed")
    except AssertionError:
        print("Test case N1 failed")
    #Test case N2. Check if names are the same on both pages
    try:
        assert inventory_photos_text == product_photos
        print("Test case N2 passed")
    except AssertionError:
        print("Test case N2 failed")
    #Test case N3. Check if names are the same on both pages
    try:
        assert inventory_prices_text == product_prices
        print("Test case N3 passed")
    except AssertionError:
        print("Test case N3 failed")

finally:
    time.sleep(2)
    browser.quit()
