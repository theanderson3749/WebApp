from selenium import webdriver
import requests
from bs4 import BeautifulSoup

if __name__ == "__main__":
    userName_ = str(input("Enter your username: "))
    password_ = str(input("Enter your password: "))
    driver = webdriver.Chrome()
    driver.get("https://my.fullerton.edu/Portal/TITANium/StudentLink.aspx")

    driver.find_element_by_xpath('//*[@id="username"]').send_keys(userName_)  
    driver.find_element_by_xpath('//*[@id="password"]').send_keys(password_)
    driver.find_element_by_xpath('//*[@id="Form1"]/div[6]/button').click()