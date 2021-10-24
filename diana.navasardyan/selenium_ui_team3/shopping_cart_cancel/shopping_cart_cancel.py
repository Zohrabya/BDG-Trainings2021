#This test case created by Vera Galstyan

#!/usr/bin/env python3

from selenium import webdriver
from selenium.webdriver.common import action_chains
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver import ActionChains
import time
browser = webdriver.Chrome(executable_path=r"C:\Users\Acer\Desktop\Webdriver\chromedriver.exe")
browser.get("https://www.saucedemo.com/")
username_form = username_form = browser.find_element_by_id("user-name")
login = browser.find_element_by_xpath('//*[@id="login_credentials"]').text.split()[3]
username_form.send_keys(login)
password_form = browser.find_element_by_id("password")
password = browser.find_element_by_xpath('//*[@class="login_password"]').text.split()[4]
password_form.send_keys(password)
login_button = browser.find_element_by_id("login-button").click()
actual = browser.find_element_by_id("add-to-cart-sauce-labs-backpack").send_keys("ADD TO CART")
browser.find_element_by_class_name( "shopping_cart_badge").click()
browser.find_element_by_id("checkout" ).click()
firstname_form = browser.find_element_by_xpath('//*[@id="first-name"]')
firstname_form.send_keys("Vera")
lastname_form = browser.find_element_by_xpath('//*[@id="last-name"]')
lastname_form.send_keys("Galstyan")
zipcode_form = browser.find_element_by_xpath('//*[@id="postal-code"]')
zipcode_form.send_keys("1111")
browser.find_element_by_xpath ('//*[@id="cancel"]').click()
cur_url = browser.current_url
expected_url = "https://www.saucedemo.com/cart.html"
if  cur_url == expected_url:
    print("Test case is passed.")
else:
    print("Test case is failed.")
