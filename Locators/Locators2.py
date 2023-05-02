from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webelement import WebElement

serv_obj = Service("C:\Drivers\chromedriver_win32\chromedriver.exe")
driver = webdriver.Chrome(service=serv_obj)
driver.get("http://automationpractice.com/index.php")
driver.maximize_window()
#find_element return not webelement object so len() function didn't work for that
#find_elements retrun webelement object so len() function work for that
silder = driver.find_elements(By.CLASS_NAME,'homeslider-container')
# for i in range(len(silder)):
#     print(silder[i])
print(len(silder))

links = driver.find_elements(By.TAG_NAME, 'a')
print(len(links))