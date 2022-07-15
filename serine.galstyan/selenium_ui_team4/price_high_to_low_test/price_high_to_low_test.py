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
time.sleep(2)
chrome_driver.find_element(By.XPATH, "//input[@id='user-name']").send_keys('standard_user')
chrome_driver.find_element(By.XPATH, "//input[@id='password']").send_keys('secret_sauce')
chrome_driver.find_element(By.XPATH, "//input[@id='login-button']").click()
time.sleep(2)
chrome_driver.find_element(By.XPATH, "//select[@class='product_sort_container']").click()
chrome_driver.find_element(By.XPATH, "//option[@value='hilo']").click()
time.sleep(2)
first_item_price = chrome_driver.find_element(By.XPATH, "//div[text()='49.99']").text
second_item_price = chrome_driver.find_element(By.XPATH, "//div[text()='29.99']").text
print(first_item_price)
print(second_item_price)
if first_item_price > second_item_price:
    print("Test case PASSED.")
else:
    print("Test case FAILED.")
time.sleep(2)
chrome_driver.quit()