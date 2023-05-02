# Methods
# The methods to handle cookies are listed below:
#  add_cookie: Used to add a cookie to the present session.
#  get_cookie: Used to get a cookie with a particular name. It yields none, if there
# is no cookie available with the given name.
#  get_cookies: Used to get all the cookies for the present URL.
#  delete_cookie: Used to delete a cookie with a particular name.
#  delete_all_cookies: Used to delete all the cookies for the present URL

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

serv_obj = Service("C:\Drivers\chromedriver_win32\chromedriver.exe")
driver = webdriver.Chrome(service=serv_obj)
driver.get("https://www.tutorialspoint.com/index.htm")
c = {'name': 'Name1', 'value': 'Value1'}
driver.add_cookie(c)
cn = driver.get_cookie('Name1')
print(cn)
print("print cookie ")
print(driver.get_cookies())
driver.delete_cookie('Name1')
print("cookie after delete ")
print(driver.get_cookies())
driver.quit()
