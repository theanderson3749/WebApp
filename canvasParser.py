from selenium import webdriver
from bs4 import BeautifulSoup
import requests
from config import userName  #this and password come from another py file i made to hold my info
from config import passWord

#FUNCTION TO REMOVE SPACES FROM STRING
def remove(string):
    return "".join(string.split()) 

#THE URL WE WANT TO REACH
URL = 'https://csufullerton.instructure.com/courses'

#DATA STRUCTURES
class_names_list = list()
class_term_list = list()
class_grades_list = list()

#basically opens a browser-->logs in and gets the cookies used
op = webdriver.ChromeOptions()
op.add_argument('headless')
driver = webdriver.Chrome(options=op)
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
class_table = soup.find('table', id ="past_enrollments_table") #finding the table with id and printing out how many we find--> OUTPUT SHOULD BE 1
for classes in class_table.find_all('tr', class_= "course-list-table-row"):
    class_name = classes.find('span', class_="name")
    name = class_name.text
    nameAdd = remove(name)
    class_names_list.append(nameAdd)

print(class_names_list)

