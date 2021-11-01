#The test case was Written by Ani Voskanyan
#!/usr/bin/env python3
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

browser = webdriver.Chrome()
browser.implicitly_wait(3)


def login():
    link = "https://www.saucedemo.com/"
    browser.get(link)
    username_input_field = browser.find_element_by_css_selector('input[placeholder = "Username"]')
    username_input_field.send_keys('standard_user') 
    password_input_field = browser.find_element_by_css_selector('input[placeholder = "Password"]')
    password_input_field.send_keys('secret_sauce')
    browser.find_element_by_class_name('submit-button').click()
    first_window = browser.window_handles[0]
    return first_window
    

def logout():
    browser.switch_to.window(login())
    browser.execute_script("window.scrollTo(0, -document.body.scrollHeight);")
    sidebar_button = browser.find_element(By.ID, "react-burger-menu-btn")
    sidebar_button.click()
    browser.find_element_by_id("logout_sidebar_link").click()

#Test case N1: Test if there is working Twitter link on the footer 
def test_twitter_link():
    login()
    twitter_button = browser.find_element_by_link_text("Twitter")
    browser.execute_script("return arguments[0].scrollIntoView(true);", twitter_button)
    twitter_button.click()
    twitter_window = browser.window_handles[1]
    browser.switch_to.window(twitter_window)
    WebDriverWait(browser, 10).until(EC.title_contains("Twitter"))
    assert "twitter" in browser.title.lower() 
    logout()
    
    #Test case N2: Test if there is working Facebook link on the footer 
def test_facebook_link():
    login()
    facebook_button = browser.find_element_by_link_text("Facebook")
    browser.execute_script("return arguments[0].scrollIntoView(true);", facebook_button)
    facebook_button.click()
    facebook_window = browser.window_handles[2]
    browser.switch_to.window(facebook_window)
    WebDriverWait(browser, 10).until(EC.title_contains("Facebook"))
    assert "facebook" in browser.title.lower()
    logout()
        
    #Test case N3: Test if there is working LinkedIn link on the footer 
def test_linkedin_link():
    login()
    linkedin_button = browser.find_element_by_link_text("LinkedIn")
    browser.execute_script("return arguments[0].scrollIntoView(true);", linkedin_button)
    linkedin_button.click()
    linkedin_window = browser.window_handles[3]
    browser.switch_to.window(linkedin_window)
    WebDriverWait(browser, 10).until(EC.title_contains("LinkedIn"))
    assert "linkedin" in browser.title.lower() 
    logout()
    