import requests
import http.cookiejar
import urllib

URL_AUTH = 'https://my.fullerton.edu/Portal/Authenticate.aspx?ReturnUrl=%2fPortal%2f'
URL_SITE = 'https://my.fullerton.edu/Portal/Dashboard/'

cookie_jar = http.cookiejar.CookieJar()

def extract_cookies():
    url_opener = urllib.request.build_opener(urllib.request.HTTPCookieProcessor(cookie_jar))
    url_opener.open(URL_AUTH)
    for cookie in cookie_jar:
        print("[Cookie Name = %s] -- [Cookie Value = %s]" %(cookie.name, cookie.value))

loginfo = {

}
if __name__ == "__main__":
    extract_cookies()
    with requests.Session() as session:
        post = session.post(URL_AUTH, cookies=cookie_jar)
        r = session.get(URL_SITE)
        print(r.text)