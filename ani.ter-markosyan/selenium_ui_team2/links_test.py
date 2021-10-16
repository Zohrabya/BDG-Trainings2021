#This test case was created by Ani Ter-Markosyan

#!/usr/bin/env python3

from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
import time

chrome_options = Options()

browser = webdriver.Chrome(executable_path = r"C:\Users\VG\Desktop\webdriver\chromedriver_win32\\chromedriver.exe", options = chrome_options)
browser.get("https://www.saucedemo.com/")
browser.find_element_by_id("user-name").send_keys("standard_user")
browser.find_element_by_id("password").send_keys("secret_sauce")
browser.find_element_by_id("login-button").click()
time.sleep(2)
browser.execute_script("window.scrollTo(0, document.body.scrollHeight)")
time.sleep(2)

#Twitter
browser.find_element_by_xpath("//a[contains(text(), 'Twitter')]").click()
time.sleep(4)
browser.switch_to_window(browser.window_handles[1])

actualUrl = browser.current_url
expectedUrl = "https://twitter.com/saucelabs"
if  actualUrl == expectedUrl:
    print("First test case is passed.")
else:
    print("Test case is failed.")

#Facebook
browser.switch_to_window(browser.window_handles[0])
time.sleep(2)
browser.find_element_by_xpath("//a[contains(text(), 'Facebook')]").click()
time.sleep(4)
browser.switch_to_window(browser.window_handles[2])

actualUrl = browser.current_url
expectedUrl = "https://www.facebook.com/saucelabs"
if  actualUrl == expectedUrl:
    print("Second test case is passed.")
else:
    print("Test case is failed.")

#LinkedIn
browser.switch_to_window(browser.window_handles[0])
time.sleep(2)
browser.find_element_by_xpath("//a[contains(text(), 'LinkedIn')]").click()
time.sleep(4)
browser.switch_to_window(browser.window_handles[3])

if  "LinkedIn" in browser.title:
        print("Third test case is passed.")
else:
    print("Test case is failed.")

browser.quit()