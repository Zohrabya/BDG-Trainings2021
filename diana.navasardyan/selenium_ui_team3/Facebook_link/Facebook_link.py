#This test case created by Diana Navasardyan

#!/usr/bin/env python3

from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import time
chrome_options = Options()
chrome_driver = webdriver.Chrome(executable_path=r"C:\Users\Acer\Desktop\Webdriver\chromedriver.exe", options= chrome_options)
chrome_driver.get("https://www.saucedemo.com/")
username_form = chrome_driver.find_element_by_id("user-name")
username_form.send_keys("standard_user")
password_form = chrome_driver.find_element_by_id("password")
password_form.send_keys("secret_sauce")
login_button = chrome_driver.find_element_by_id("login-button").click()
time.sleep(3)
chrome_driver.execute_script("window.scrollTo(0, document.body.scrollHeight)")
time.sleep(3)
chrome_driver.find_element_by_xpath("//a[contains(text(), 'Facebook')]").click()
cur_url = chrome_driver.current_url
expected_url = "https://www.facebook.com/saucelabs"
if  cur_url == expected_url:
     print("Test case is passed.")
else:
    print("Test case is failed.")