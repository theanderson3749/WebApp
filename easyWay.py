from selenium import webdriver
import requests
from requests import Session
from requests.cookies import cookiejar_from_dict
from bs4 import BeautifulSoup
import time

URL_SITE = 'https://my.fullerton.edu/Portal/Dashboard/'

if __name__ == "__main__":
    userName_ = str(input("Enter your username: "))
    password_ = str(input("Enter your password: "))
    driver = webdriver.Chrome()
    driver.get(URL_SITE)

    driver.find_element_by_xpath('//*[@id="username"]').send_keys(userName_)  
    driver.find_element_by_xpath('//*[@id="password"]').send_keys(password_)
    driver.find_element_by_xpath('//*[@id="Form1"]/div[6]/button').click()
    cookie_jar = driver.get_cookies()
    
    cookies_dict = {}
    for cookie in cookie_jar:
        cookies_dict[cookie['name']] = cookie['value']

    driver.close()

    session = requests.Session()
    cookie_jarSess = requests.cookies.RequestsCookieJar()
    for cookie in cookies_dict:
        cookie_jarSess.set(cookie, cookies_dict[cookie])
    session.cookies = cookie_jarSess
    r = session.get(URL_SITE)
    soup = BeautifulSoup(r.text, 'lxml')
    print(soup.title.text)
    print(soup.prettify())