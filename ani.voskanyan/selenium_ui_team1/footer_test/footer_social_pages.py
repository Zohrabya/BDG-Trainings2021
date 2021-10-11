#The test case was Written by Ani Voskanyan
#!/usr/bin/env python3

from selenium import webdriver
import time

browser = webdriver.Chrome()
link = "https://www.saucedemo.com/"
browser.get(link)
try:
    #log in 
    username_input_field = browser.find_element_by_css_selector('input[placeholder = "Username"]')
    username_input_field.send_keys('standard_user')
    password_input_field = browser.find_element_by_css_selector('input[placeholder = "Password"]')
    password_input_field.send_keys('secret_sauce')
    browser.find_element_by_class_name('submit-button').click()
    time.sleep(2)
    first_window = browser.window_handles[0]
    #Test case N1: Test if there is working Twitter link on the footer 
    twitter_button = browser.find_element_by_link_text("Twitter")
    browser.execute_script("return arguments[0].scrollIntoView(true);", twitter_button)
    twitter_button.click()
    twitter_window = browser.window_handles[1]
    browser.switch_to.window(twitter_window)
    time.sleep(10)
    try:
        assert "twitter" in browser.title.lower() 
        print("Test case N1 passed")
    except AssertionError:
        print("Test case N1 failed")
    #Test case N2: Test if there is working Facebook link on the footer 
    browser.switch_to.window(first_window)
    facebook_button = browser.find_element_by_link_text("Facebook")
    facebook_button.click()
    facebook_window = browser.window_handles[2]
    browser.switch_to.window(facebook_window)
    time.sleep(10)
    try:
        assert "facebook" in browser.title.lower() 
        print("Test case N2 passed")
    except AssertionError:
        print("Test case N2 failed")
    #Test case N3: Test if there is working LinkedIn link on the footer 
    browser.switch_to.window(first_window)
    linkedin_button = facebook_button = browser.find_element_by_link_text("LinkedIn")
    linkedin_button.click()
    linkedin_window = browser.window_handles[3]
    browser.switch_to.window(linkedin_window)
    time.sleep(10)
    try:
        assert "linkedin" in browser.title.lower() 
        print("Test case N3 passed")
    except AssertionError:
        print("Test case N3 failed")

finally:
    time.sleep(2)
    browser.quit()
