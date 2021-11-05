#The test case was Written by Ani Voskanyan
#!/usr/bin/env python3
import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

browser = webdriver.Chrome()
browser.implicitly_wait(3)

#Test case: Test if there are working Twitter, Facebook, LinkedIn links on the footer 
@pytest.mark.parametrize("link_name_input", ["Twitter", "Facebook", "LinkedIn"])
def test_twitter_link(link_name_input):
    link = "https://www.saucedemo.com/"
    browser.get(link)
    username_input_field = browser.find_element_by_css_selector('input[placeholder = "Username"]')
    username_input_field.send_keys('standard_user') 
    password_input_field = browser.find_element_by_css_selector('input[placeholder = "Password"]')
    password_input_field.send_keys('secret_sauce')
    browser.find_element_by_class_name('submit-button').click()
    first_window = browser.window_handles[0]
    link_button = browser.find_element_by_link_text(link_name_input)
    browser.execute_script("return arguments[0].scrollIntoView(true);", link_button)
    link_button.click()
    link_window = browser.window_handles[1]
    browser.switch_to.window(link_window)
    WebDriverWait(browser, 10).until(EC.title_contains(link_name_input))
    assert link_name_input.lower() in browser.title.lower() 
    browser.switch_to.window(first_window)
    browser.execute_script("window.scrollTo(0, -document.body.scrollHeight);")
    sidebar_button = browser.find_element(By.ID, "react-burger-menu-btn")
    sidebar_button.click()
    browser.find_element_by_id("logout_sidebar_link").click()
    