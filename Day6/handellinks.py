from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webelement import WebElement

serv_obj = Service("C:\Drivers\chromedriver_win32\chromedriver.exe")
driver = webdriver.Chrome(service=serv_obj)
driver.get("http://demo.nopcommerce.com/register")
driver.maximize_window()
#click on the links
# driver.find_element(By.LINK_TEXT,"Digital downloads").click()
# driver.find_element(By.PARTIAL_LINK_TEXT,"Digital").click()

Links = driver.find_elements(By.XPATH, "//a")
# print("Count of all links", len(Links))
#print all links
for links in Links:
    print(links.text)

