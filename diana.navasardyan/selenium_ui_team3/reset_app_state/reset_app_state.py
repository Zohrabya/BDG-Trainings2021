#This test case created by Diana Navasardyan

#!/usr/bin/env python3

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
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
browser.find_element(By.ID, "add-to-cart-sauce-labs-backpack").click()
browser.find_element(By.ID, "react-burger-menu-btn").click()
browser.find_element(By.ID, "reset_sidebar_link").click()
shopping_cart =  browser.find_element(By.XPATH, "//div[@id = 'shopping_cart_container']/a/span")
if  shopping_cart == None:
    print("Test case is passed.")
else:
    print("Test case is failed.")