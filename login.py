import requests
from bs4 import BeautifulSoup

session = requests.Session()
cookie_jar = requests.cookies.RequestsCookieJar()
cookie_jar.set('ASP.NET_SessionId','uclxftwssmcr1mjelnrhzmwe')
cookie_jar.set('_shibsession_64656661756c7468747470733a2f2f6d792e66756c6c6572746f6e2e6564752f73686962626f6c657468','_16969ed83da9622bf60068092be6cd74')
cookie_jar.set('.ASPXAUTH','5B9F9B8645ACD687461621224B4003D61DE7E92BAEDA102AC7F674F5162A2EA9953BBC83AC744210085DD31C0DE72587D74F8DE2EDB36EB3927BEF38E1DD39B48F3282ED0FD6DEFDC876F9204A44CA3BD862D02FF5E946A7B4218F3CB47E174DE37726B861CDB7827216897BC021FA7CC6ED31F2FBA4FCD1D581A7CD3B358F5C543401C1D9470E87B60350084CEB1AB2')
session.cookies = cookie_jar
r = session.get('https://my.fullerton.edu/Portal/Dashboard/')
soup = BeautifulSoup(r.text, 'lxml')
print(soup.title.text)
print(soup.prettify())
'''
import requests
from config import data 
from bs4 import BeautifulSoup
import http.cookiejar
import urllib

cookie_jar = http.cookiejar.CookieJar()
url_login = 'http://my.fullerton.edu'
url_site = "https://my.fullerton.edu/Portal/TITANium/StudentLink.aspx"
if __name__ == "__main__":
    session = requests.Session()
    #r = session.post(url_login, data=data)
    url_opener = urllib.request.build_opener(urllib.request.HTTPCookieProcessor(cookie_jar))
    url_opener.open(url_login)
    for cookie in cookie_jar:
        print("[Cookie Name = %s] -- [Cookie Value = %s]" %(cookie.name, cookie.value))
    r = session.get("https://my.fullerton.edu/Portal/TITANium/StudentLink.aspx")
    if r.status_code == 200:
        print("Success!")
    elif r.status_code == 404:
        print("Failure!")
    soup = BeautifulSoup(r.text, 'lxml')
    print(soup.title.text)
    #soup = BeautifulSoup(r.content, 'lxml')
    #print(soup.prettify()) '''