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
PREVclass_names_list = list()
PREVclass_term_list = list()
PREVclass_grades_list = list()
PREVclass_enrollment_list = list()

CURRclass_names_list = list()
CURRclass_term_list = list()
CURRclass_grades_list = list()
CURRclass_enrollment_list = list()

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

#PREVIOUS SEMESTER CLASSES
PREVclass_table = soup.find('table', id ="past_enrollments_table") #finding the table with id and printing out how many we find--> OUTPUT SHOULD BE 1
for classes in PREVclass_table.find_all('tr', class_= "course-list-table-row"):
    class_name = classes.find('span', class_="name")
    name = class_name.text
    nameAdd = remove(name)
    slicedClass = nameAdd[10:]
    PREVclass_names_list.append(slicedClass)

for term in PREVclass_table.find_all('tr', class_= "course-list-table-row"):
    class_term = term.find('td', class_="course-list-no-left-border course-list-term-column")
    termName = class_term.text
    termAdd = remove(termName)
    PREVclass_term_list.append(termAdd)

for enrollment in PREVclass_table.find_all('tr', class_= "course-list-table-row"):
    class_enrollment = enrollment.find('td', class_="course-list-no-left-border course-list-enrolled-as-column")
    enrollName = class_enrollment.text
    enrollAdd = remove(enrollName)
    PREVclass_enrollment_list.append(enrollAdd)

#FUTURE SEMESTER CLASSES
CURRclass_table = soup.find('table', id ="future_enrollments_table") #finding the table with id and printing out how many we find--> OUTPUT SHOULD BE 1
for classes in CURRclass_table.find_all('tr', class_= "course-list-table-row"):
    class_name = classes.find('span', class_="name")
    name = class_name.text
    nameAdd = remove(name)
    slicedClass = nameAdd[8:]
    CURRclass_names_list.append(slicedClass)

for term in CURRclass_table.find_all('tr', class_= "course-list-table-row"):
    class_term = term.find('td', class_="course-list-no-left-border course-list-term-column")
    termName = class_term.text
    termAdd = remove(termName)
    CURRclass_term_list.append(termAdd)

for enrollment in CURRclass_table.find_all('tr', class_= "course-list-table-row"):
    class_enrollment = enrollment.find('td', class_="course-list-no-left-border course-list-enrolled-as-column")
    enrollName = class_enrollment.text
    enrollAdd = remove(enrollName)
    CURRclass_enrollment_list.append(enrollAdd)

#OUTPUT FOR PREVIOUS SEMESTER CLASSES
print("-----------------PREVIOUS SEMESTER INFO---------------------")
print("CLASSES",end='     ')
print("\t\t",end='')
print('TERM',end='     ')
print("\t",end='')
print("ENROLLMENT")
for index in range(0, len(PREVclass_names_list)):
    print(PREVclass_names_list[index],end='     ')
    print("\t",end='')
    print(PREVclass_term_list[index],end='     ')
    print("\t",end='')
    print(PREVclass_enrollment_list[index])

#OUTPUT FOR UPCOMING SEMESTER CLASSES
print("-----------------FUTURE SEMESTER INFO---------------------")
print("CLASSES",end='     ')
print("\t\t",end='')
print('TERM',end='     ')
print("\t",end='')
print("ENROLLMENT")
for index in range(0, len(CURRclass_names_list)):
    print(CURRclass_names_list[index],end='     ')
    print("\t",end='')
    print(CURRclass_term_list[index],end='     ')
    print("\t",end='')
    print(CURRclass_enrollment_list[index])
'''print(class_names_list)
print(class_term_list)
print(class_enrollment_list)'''