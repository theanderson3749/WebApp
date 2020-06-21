import requests               # requests library for get/post
import lxml.html              # lxml library mainly for prettify()
from requests import Session  # Session objects for log-ins
from bs4 import BeautifulSoup # Formatting tool for debug

from config import userName   # used another file to store login
from config import passWord   

def redirectChecker(requestObject): #function to detect redirects
    if requestObject.history:
        print("Request was redirected:")
        for resp in requestObject.history:
             print("Here is the redirected link")
             print(resp.status_code, resp.url)
             print("")
             print("Here are the cookies present at said link")
             print(resp.cookies)
             print("========")
        print("Final destination:")
        print(requestObject.status_code, requestObject.url)
        print(response.cookies)
    else:
      print("Request was not redirected")

def divider():  #function to divide segments for debug
    print("============================")

URL_SITE = "https://my.fullerton.edu/Portal/Dashboard/" #section of sites saved as variables
DEST_SITE = "https://csufullerton.instructure.com/"

payload = {
    'j_username' : userName,
    'j_password' : passWord
}           #will be used as data variable for .post functions
            #needs tweaking; as it doesn't seem to work
            #(COULD BE MISSING POTENTIAL HIDDEN FIELDS)

generated_LOGIN = "initially empty" #individual jSESSION website generated by URL_SITE

divider() 
################################################
s = requests.Session()          # creating the Session object

response = s.get(URL_SITE)      
redirectChecker(response)

generated_LOGIN = response.url  # final redirect gives us session's unique jSESSION website

divider()
##################################################
login_post = s.post(generated_LOGIN, data=payload)  # POSTing payload for logging in; doesn't seem to work though
redirectChecker(login_post)

divider()
###################################################
canvas_get = s.get(DEST_SITE)                 # Authentication fails...
redirectChecker(canvas_get)              # This means that the log-in fails above

divider()
####################################################
soup = BeautifulSoup(canvas_get.content, 'lxml')
print(soup.prettify())

divider()
#####################################################




    

   



    


