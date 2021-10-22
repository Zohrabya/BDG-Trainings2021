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
chrome_driver.find_element(By.XPATH, "//button[@id='add-to-cart-sauce-labs-backpack']").click()
chrome_driver.find_element(By.XPATH, "//button[@id='add-to-cart-sauce-labs-bike-light']").click()
chrome_driver.find_element(By.XPATH, "//a[@class='shopping_cart_link']").click()
chrome_driver.find_element(By.XPATH, "//button[@id='checkout']").click()
time.sleep(2)
chrome_driver.find_element(By.XPATH, "//input[@id='first-name']").send_keys('Serine')
chrome_driver.find_element(By.XPATH, "//input[@id='last-name']").send_keys('Galstyan')
chrome_driver.find_element(By.XPATH, "//input[@id='postal-code']").send_keys('12345')
chrome_driver.find_element(By.XPATH, "//input[@id='continue']").click()
first_value = chrome_driver.find_element(By.XPATH, "//div[@class='summary_subtotal_label']").text
item_total = first_value[13:18]
second_value = chrome_driver.find_element(By.XPATH, "//div[@class='summary_tax_label']").text
tax = second_value[6:10]
last_value = chrome_driver.find_element(By.XPATH, "//div[@class='summary_total_label']").text
total = last_value[8:13]
if float(item_total) + float(tax) == float(total):
    print('Overview is True.')
else:
    print('Overview is False')
chrome_driver.find_element(By.XPATH, "//button[@id='finish']").click()
if chrome_driver.find_element(By.XPATH, "//span[text()='Checkout: Complete!']")!= None:
    print("Checkout complete.")
else:
    print("Checkout fail.")
chrome_driver.find_element(By.XPATH, "//button[@id='back-to-products']").click()
if chrome_driver.find_element(By.XPATH, "//span[text()='Products']")!= None:
    print("Test case PASSED.")
else:
    print("Test case FAILED.")
time.sleep(2)
chrome_driver.quit()