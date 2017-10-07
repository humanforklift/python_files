#! /usr/bin/env python3
# gmailer.py - takes text and logs into email address,
# sending text to the email address provided

import sys
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

if len(sys.argv) >= 3:
    # Get email address and text from command line
    email = sys.argv[1]
    text = ' '.join(sys.argv[2:])

    # Open browser and navigate to gmail
    browser = webdriver.Chrome('/Path/to/Chrome/Driver')
    browser.get('https://www.gmail.com')

    try:
        # store password in string
        passwordStr = 'YOUR_PASSWORD'

        # navigate to login screen
        browser.find_element_by_name('identifier').click()
    
        # enter email address into username field
        browser.find_element_by_id('identifierId').send_keys('YOUR_EMAIL@gmail.com')

        # navigate to next screen to enter password
        browser.find_element_by_tag_name('content').click()
        
        # tell browser to wait until password element is displayed before trying to find
        password = WebDriverWait(browser, 60).until(
            EC.presence_of_element_located((By.NAME, 'password')))

        # enter password in input field
        password.send_keys(passwordStr)

        # complete login
        browser.find_element_by_id('passwordNext').click()

        # wait until email login completed before trying to send new mail
        compose = WebDriverWait(browser, 30).until(
            EC.presence_of_element_located((By.XPATH, "//div[@role='button'][@class='T-I J-J5-Ji T-I-KE L3']")))
        compose.click()

        # wait until new message is able to be sent before trying to enter recipient email
        to = WebDriverWait(browser, 30).until(
            EC.presence_of_element_located((By.ID, ':8y')))
        to.send_keys(email)
        
        # enter text in textbox area
        browser.find_element_by_xpath("//div[@role='textbox']").click().send_keys(text)
        
        # send message
        browser.find_element_by_xpath("//div[@role='button'][@class='T-I J-J5-Ji aoO T-I-atl L3']").click()

        # close browser
        browser.quit()
        
    except:
        print('There was a problem')
else:
    print('Please enter valid email address and text to send.')




