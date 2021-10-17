#This test case created by Diana Navasardyan

#!/usr/bin/env python3

from selenium import webdriver
chrome_driver = webdriver.Chrome(executable_path=r"C:\Users\Acer\Desktop\Webdriver\chromedriver.exe")
chrome_driver.get("https://www.saucedemo.com/")
username_form = chrome_driver.find_element_by_id("user-name")
username_form.send_keys("")
password_form = chrome_driver.find_element_by_id("password")
password_form.send_keys("")
login_button = chrome_driver.find_element_by_id("login-button").click()
cur_url = chrome_driver.current_url
expected_url = "https://www.saucedemo.com/"
if cur_url == expected_url:
    print("test case PASSED")
else:
    print("test case FAILED")

