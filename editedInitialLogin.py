from selenium import webdriver

import requests
from requests import Session
import json

from config import userName
from config import passWord

import time

# ~13 seconds benchmark test
# need to find a better method bc that takes too long >.<

CANVASACCOUNTLINK = 'https://csufullerton.instructure.com/profile/settings'

def gettingToken():
    # setting up Chrome webdriver 
    op = webdriver.ChromeOptions()
    op.add_argument('headless')
    driver = webdriver.Chrome(options = op)

    # Selenium initiates web traversal to csufullerton.instructure
    driver.get(CANVASACCOUNTLINK)

    # goes through redirected CSUF login page
    # uses login information from a file called config.py
    driver.find_element_by_xpath('//*[@id="username"]').send_keys(userName)  
    driver.find_element_by_xpath('//*[@id="password"]').send_keys(passWord)
    driver.find_element_by_xpath('//*[@id="Form1"]/div[6]/button').click()

    # checks if part 1 of website tutorial appears
    # closes tutorial pop-up; skips if not present
    STAR_TUTORIAL = len(driver.find_elements_by_xpath('//*[@id="___reactour"]/div[4]/div/div/div/span[1]/span/button'))

    if(STAR_TUTORIAL > 0):
        driver.find_element_by_xpath('//*[@id="___reactour"]/div[4]/div/div/div/span[1]/span/button').click()
    else:
        pass

    # wait for 1 second to buffer click time 
    time.sleep(1)

    # checks if part 2 of website tutorial appears
    # closes tutorial pop-up; skips if not present
    # TODO: optimize by integrating STAR_TUTORIAL w/ PANDA_TUTORIAL 
    PANDA_TUTORIAL = len(driver.find_elements_by_xpath('//*[@id="___reactour"]/div[4]/div/div/div/span[2]/span[2]/button'))

    if(PANDA_TUTORIAL > 0):
        driver.find_element_by_xpath('//*[@id="___reactour"]/div[4]/div/div/div/span[2]/span[2]/button').click()
    else:
        pass

    # detects data table of existing tokens and saves to variable
    TABLE_OF_TOKENS = driver.find_element_by_xpath('//*[@id="access_tokens"]')

    # if a token exists with the purpose, "ADEALPHA", then token exists
    if(TABLE_OF_TOKENS.text.find("ADEALPHA") != -1):
        #An access token already exists
        return "ERROR"
    else:
        # go through processes to generate an access token
        ADD_ACCESS_TOKEN1 = len(driver.find_elements_by_xpath('//*[@id="content"]/div[3]/div[2]/a'))
        # if more than 0 non-'ADEALPHA' token exists, then perform this operation
        if(ADD_ACCESS_TOKEN1 > 0):
            driver.find_element_by_xpath('//*[@id="content"]/div[3]/div[2]/a').click()
            driver.find_element_by_xpath('//*[@id="access_token_purpose"]').send_keys('ADEALPHA')
            driver.find_element_by_xpath('/html/body/div[6]/div[11]/div/button[2]/span').click()
            time.sleep(1)
            token = driver.find_element_by_xpath('//*[@id="token_details_dialog"]/div[3]/table/tbody/tr[1]/td/div[1]').text
            return token
        # if there are no existing tokens at all, then perform this operation
        else:
            driver.find_element_by_xpath('//*[@id="content"]/div[3]/div[3]/a').click()
            driver.find_element_by_xpath('//*[@id="access_token_purpose"]').send_keys('ADEALPHA')
            driver.find_element_by_xpath('/html/body/div[6]/div[11]/div/button[2]/span').click()
            time.sleep(1)
            token = driver.find_element_by_xpath('//*[@id="token_details_dialog"]/div[3]/table/tbody/tr[1]/td/div[1]').text
            return token
    
    # exiting Selenium
    driver.close()

# will print out access token if you wish to see; just uncomment
# print(gettingToken())






