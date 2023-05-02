from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
import requests
from selenium.webdriver.remote.webelement import WebElement

serv_obj = Service("C:\Drivers\chromedriver_win32\chromedriver.exe")
driver = webdriver.Chrome(service=serv_obj)
driver.get("http://www.deadlinkcity.com/")
driver.maximize_window()
alllinks = driver.find_elements(By.TAG_NAME, 'a')
count = 0
for links in alllinks:
    url = links.get_attribute('href')
    try:
        res = requests.head(url)
    except:
        None
    if res.status_code >= 400:
        print(url," is broken link")
        count += 1
    else:
        print(url, " Is valid link")


driver.quit()