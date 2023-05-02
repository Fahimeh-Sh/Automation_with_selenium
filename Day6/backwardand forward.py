from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

serv_obj = Service("C:\Drivers\chromedriver_win32\chromedriver.exe")
driver = webdriver.Chrome(service=serv_obj)
driver.get("https://www.tutorialspoint.com/about/about_careers.htm")
driver.maximize_window()
driver.get("https://www.tutorialspoint.com/online_dev_tools.htm")
driver.maximize_window()
driver.back()
print("page navigate after back " + driver.title)
driver.forward()
print("page forward" + driver.title)
driver.quit()
