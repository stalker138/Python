'''
Created on 05 авг. 2016 г.

@author: Alex
'''

from urllib.request import *
from urllib.error import *
from urllib.parse import *

def request(page, data=None, headers={}):
    content = None
    try:
        req = Request(page, data, headers)
        u = urlopen(req)
    except HTTPError as u:
        status = str(u.code)
        print("Error! " + " code: " + status)
    except URLError as uerr:
        status = str(uerr)
        print("Error! " + " code: " + str(uerr))
    except OSError as oerr:
        status = str(oerr)
        print("Error! " + " code: " + str(oerr))
    except Exception as e:
        hdr = e.info()
        status = "Unknown"
        print("Error?????")
    else:
        data = u.read()
        decoding = True
        try:
            content = data.decode("utf-8")
        except:
            try:
                content = data.decode("cp1251")
            except:
                decoding = False
        finally:
#            f = data.find("b-group-phrase__price-value")
            print("url: " + u.geturl())
            hdr = u.info()
            if decoding:
                print("Decoding: " + page)
            else:
                print("No codecs: " + page)
    return content

class MyRedirectHandler(HTTPRedirectHandler):
    def redirect_request(self, req, fp, code, msg, hdrs, url):
        newurl = super().redirect_request(req, fp, code, msg, hdrs, url)
        return newurl

class MyErrorHandler(HTTPDefaultErrorHandler):
    def http_error_default(self, req, fp, code, msg, hdrs):
        pass
        return super().http_error_default(req, fp, code, msg, hdrs)

class MyUnknownHandler(UnknownHandler):
    def unknown_open(self, req):
        ret = super().unknown_open(req)
        return ret
'''
herror = MyErrorHandler()
hredirect = MyRedirectHandler()
hunknown = MyUnknownHandler()
opener = build_opener(herror, hredirect, hunknown)
# ...and install it globally so it can be used with urlopen.
install_opener(opener)

headers = {"Content-Type":"application/x-www-form-urlencoded;charset=utf-8",
           "User-Agent": "Firefox/12.3"}
url = "https://www.google.ru/search?num=50&newwindow=1&hl=ru&biw=1280&bih=855&q=site%3Apolmsk.ru"
url = "https://direct.yandex.ru/registered/main.pl?cmd=showCamp&cid=11868880&ulogin=&csrf_token=yc-wUGcWqrWTfxIQ"
url = "https://satoshihero.com/ru/login"
url = "https://bitplay.io/api/v1/login"
#url = "https://www.yandex.ru/search/?user=Stalker321&key=03.7063636:d97aaf081731ef6f085923ea7d41056b&lr=1&win=209&text=%D0%BF%D0%BE%D0%BB%D0%B8%D0%BC%D0%B5%D1%80%D0%BD%D1%8B%D0%B5%20%D0%BF%D0%BE%D0%BB%D1%8B"
#url = 'https://api.exmo.com/v1/pair_settings/'
#url = 'https://www.teohim-yr.ru'
url = "https://www.huobi.com/vision/?prefix=data/trades/spot/daily/ADAUSDT/ADAUSDT-trades-2021-10-14.zip"

data = None
data = urlencode({'login': 'st17', 'pass': 'st17'}).encode('utf-8')
data = urlencode({'email': 'wander321@yandex.ru', 'password': 'tu138pik'}).encode('utf-8')
data = request(url, None, headers)
'''

from selenium import webdriver 
from selenium.webdriver.common.by import By
 
# Get the path of chromedriver which you have install
 
def startBot(username, password, url):
    path = "d:/chrome/chromedriver.exe"
     
    # giving the path of chromedriver to selenium webdriver
    driver = webdriver.Chrome()
     
    # opening the website  in chrome.
    driver.get(url)
     
    # find the id or name or class of
    # username by inspecting on username input
    user = driver.find_element(By.NAME, "auth_cookie_login")
    user.send_keys(username)
     
    # find the password by inspecting on password input
    psw = driver.find_element(By.NAME, "auth_cookie_password")
    psw.send_keys(password)
     
    # click on submit
    entry = driver.find_element(By.CSS_SELECTOR, ".formh input[type=\"submit\"]")
    entry.click()

    price = driver.find_elements(By.CSS_SELECTOR, ".gs1")
    pass
  
# Driver Code
# Enter below your login credentials
username = "as321"
password = "as321pik"
 
# URL of the login page of site
# which you want to automate login.
url = "https://www.vashdom.ru/login.htm"
 
# Call the function
startBot(username, password, url)
