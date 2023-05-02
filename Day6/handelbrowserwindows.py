from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
import requests
from selenium.webdriver.remote.webelement import WebElement

serv_obj = Service("C:\Drivers\chromedriver_win32\chromedriver.exe")
driver = webdriver.Chrome(service=serv_obj)
driver.get("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")
driver.maximize_window()
driver.find_element(By.LINK_TEXT, "OrangeHRM, Inc").click()
windowsIDs = driver.window_handles

parentwindowid = windowsIDs[0]
childwindowId = windowsIDs[1]
driver.switch_to.window(childwindowId)
print(driver.title)
driver.switch_to(parentwindowid)
print(driver.title)

for winid in windowsIDs:
    driver.switch_to.window(winid)
    print(driver.title)