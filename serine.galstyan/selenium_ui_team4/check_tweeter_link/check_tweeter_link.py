# This test case was created by Serine Galstyan
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.options import Options
import time

chrome_user_options = Options()
chrome_user_options.add_argument("--start-maximized")

chrome_driver = webdriver.Chrome(chrome_options = chrome_user_options, executable_path=r"C:/Users/Orchid/OneDrive/Desktop/chrome/chromedriver_win32 (1)/chromedriver.exe")
chrome_driver.get("https://www.saucedemo.com/")
time.sleep(2)
chrome_driver.find_element(By.XPATH, "//input[@id='user-name']").send_keys('standard_user')
chrome_driver.find_element(By.XPATH, "//input[@id='password']").send_keys('secret_sauce')
chrome_driver.find_element(By.XPATH, "//input[@id='login-button']").click()
time.sleep(2)
chrome_driver.find_element(By.XPATH, "//a[@href='https://twitter.com/saucelabs']").click()
time.sleep(5)
chrome_driver.switch_to.window(chrome_driver.window_handles[1])
time.sleep(2)
get_title = chrome_driver.title
print(get_title)
if get_title == "Sauce Labs (@saucelabs) / Twitter":
    print("Test case PASSED.")
else:
    print("Test case FAILED.")
time.sleep(2)
chrome_driver.quit()