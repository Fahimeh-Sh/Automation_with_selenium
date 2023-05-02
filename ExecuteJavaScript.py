from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from time import sleep

serv_obj = Service("C:\Drivers\chromedriver_win32\chromedriver.exe")
driver = webdriver.Chrome(service=serv_obj)
driver.get("http://yahoo.com")
sleep(5)
driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
sleep(2)