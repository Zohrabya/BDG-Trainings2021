# This test case was created by Serine Galstyan

#!/usr/bin/env python3

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
import time

chrome_user_options = Options()
chrome_user_options.add_argument("--start-maximized")
chrome_user_options.add_argument("--log-level=3")


chrome_driver = webdriver.Chrome(chrome_options = chrome_user_options, executable_path=r"C:/Users/Orchid/OneDrive/Desktop/chrome/chromedriver_win32 (1)/chromedriver.exe")
chrome_driver.get("https://www.saucedemo.com/")
chrome_driver.find_element(By.XPATH, "//input[@id='login-button']").click()
time.sleep(2)
error_message = chrome_driver.find_element(By.XPATH, "//div[@id='login_button_container']/div/form/div[3]/h3").text
time.sleep(2)
expected_message = "Epic sadface: Username and Password are required"
if error_message == expected_message:
    print("Test case PASSED.")
else:
    print("Test case FAILED.")
time.sleep(2)
chrome_driver.quit()