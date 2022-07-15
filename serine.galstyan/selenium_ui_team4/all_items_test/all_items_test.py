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
chrome_driver.find_element(By.XPATH, "//a[@class='shopping_cart_link']").click()
chrome_driver.find_element(By.XPATH, "//button[@id='react-burger-menu-btn']").click()
time.sleep(1)
chrome_driver.find_element(By.XPATH, "//a[@id='inventory_sidebar_link']").click()
if chrome_driver.find_element(By.XPATH, "//span[text()='Products']")!= None:
    print("Test case PASSED.")
else:
    print("Test case FAILED.")
time.sleep(2)
chrome_driver.quit()