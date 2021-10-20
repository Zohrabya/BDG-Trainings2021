#This test case created by Diana Navasardyan

#!/usr/bin/env python3

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
chrome_driver = webdriver.Chrome(executable_path=r"C:\Users\Acer\Desktop\Webdriver\chromedriver.exe")
chrome_driver.get("https://www.saucedemo.com/")
username_form = username_form = chrome_driver.find_element_by_id("user-name")
login = chrome_driver.find_element_by_xpath('//*[@id="login_credentials"]').text.split()[4]
username_form.send_keys(login)
password_form = chrome_driver.find_element_by_id("password")
password = chrome_driver.find_element_by_xpath('//*[@class="login_password"]').text.split()[4]
password_form.send_keys(password)
login_button = chrome_driver.find_element_by_id("login-button").click()

if chrome_driver.find_element_by_xpath('//*[@class="error-button"]'):
    print("test case PASSED")
else:
    print("test case FAILED")