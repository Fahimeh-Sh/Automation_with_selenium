#close() -- close single browser window (where driver focused)
#quite() -- close multiple browser windows
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webelement import WebElement

serv_obj = Service("C:\Drivers\chromedriver_win32\chromedriver.exe")
driver = webdriver.Chrome(service=serv_obj)
driver.get("https://www.digikala.com/")
driver.get("https://hooyo.ir/")

driver.back()
driver.forward()
driver.refresh()
driver.quit()