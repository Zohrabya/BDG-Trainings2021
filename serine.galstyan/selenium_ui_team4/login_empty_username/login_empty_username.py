#!/usr/bin/env python3

# This test case was created by Hayk Poghosyan

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
import time

chrome_user_options = Options()
chrome_user_options.add_argument("--start-maximized")
# chrome_user_options.add_argument("--headless")
chrome_user_options.add_argument("--log-level=3")
chrome_user_options.add_experimental_option("prefs", {"profile.default_content_settings_values.notifications": 2 })

browser = webdriver.Chrome(chrome_options = chrome_user_options, executable_path=r"C:\Users\Hayk Poghosyan\Downloads\chromedriver.exe")
browser.get("https://www.saucedemo.com/")

valid_password = browser.find_element(By.ID, "password").send_keys("secret_sauce")
time.sleep(3)
click_login_button = browser.find_element(By.ID, "login-button").click()
time.sleep(3)
empty_login_error_message = "Epic sadface: Username is required"
opened_error_message = browser.find_element(By.XPATH, "//h3[@data-test='error']").text

if empty_login_error_message == opened_error_message:
    print("Test case PASSED")
else:
    print("Test case FAILED")
browser.close() 