from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from time import sleep
from selenium.webdriver.chrome.options import Options

chrome_options = Options()
chrome_options.add_argument("--incognito")
chrome_options.add_argument("--headless")


serv_obj = Service("C:\Drivers\chromedriver_win32\chromedriver.exe")
# driver with chrome options
driver = webdriver.Chrome(service=serv_obj, options=chrome_options)

# Browser Action 1 > Open Web google.com
driver.get("http://google.com")
sleep(3)
