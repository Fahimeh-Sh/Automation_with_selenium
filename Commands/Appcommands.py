from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webelement import WebElement

serv_obj = Service("C:\Drivers\chromedriver_win32\chromedriver.exe")
driver = webdriver.Chrome(service=serv_obj)
driver.get("http://automationpractice.com/index.php")
print(driver.title)
print(driver.current_url)
#to capture surce code of the page
print(driver.page_source)
driver.quit()

