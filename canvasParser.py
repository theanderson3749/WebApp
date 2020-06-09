from selenium import webdriver
from bs4 import BeautifulSoup
import requests
from config import userName  #this and password come from another py file i made to hold my info
from config import passWord


URL = 'https://csufullerton.instructure.com/courses'
#basically opens a browser-->logs in and gets the cookies used
driver = webdriver.Chrome()
driver.get(URL)
driver.find_element_by_xpath('//*[@id="username"]').send_keys(userName)  
driver.find_element_by_xpath('//*[@id="password"]').send_keys(passWord)
driver.find_element_by_xpath('//*[@id="Form1"]/div[6]/button').click()
cookie_jar = driver.get_cookies()
    
cookies_dict = {} #adds cookies into the cookie jar for the requests use
for cookie in cookie_jar:
    cookies_dict[cookie['name']] = cookie['value']

driver.close()

#creates the session we are going to be working in
session = requests.Session()
cookie_jarSess = requests.cookies.RequestsCookieJar()
for cookie in cookies_dict:  #setting cookies into the jar for the session
    cookie_jarSess.set(cookie, cookies_dict[cookie])
session.cookies = cookie_jarSess
r = session.get(URL)
soup = BeautifulSoup(r.content, 'lxml') #Beautifulsoup object to parse through
class_table = soup.find_all('table', id ="past_enrollments_table") #finding the table with id and printing out how many we find--> OUTPUT SHOULD BE 1
print(len(class_table))



'''def itemsAvailableAndLink():
    supremeSite = requests.get('https://www.supremenewyork.com/shop/all')
    soup = BeautifulSoup(supremeSite.content, 'html.parser')
    for cat in soup.find_all('ul' , {'id': 'nav-categories'}):
        count = 0
        count2 = 0
        for litag in cat.find_all('li'):
            print(str(count) + ": " + litag.text)
            count += 1
        catNum = input("Enter the catergory number: ")
        for desired in cat.find_all('li'):
            if(catNum == str(count2)):
                extension = (desired.find('a').get('href'))
                fullLink = ("https://www.supremenewyork.com" + extension)
                return fullLink
            count2 += 1
'''
