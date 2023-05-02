from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

serv_obj = Service("C:\Drivers\chromedriver_win32\chromedriver.exe")
driver = webdriver.Chrome(service=serv_obj)
driver.get("https://demo.nopcommerce.com")
# maximize the browser window
driver.maximize_window()
print("page Title " + driver.title)
# driver.quit()
#id and name locators
driver.find_element(By.ID,"small-searchterms").send_keys("Lenovo")
# driver.find_element(By.NAME,"q").send_keys("Lenovo")
value = driver.find_element(By.NAME,"q").get_attribute('value')
print('value entered', value)
# #link text and partial link text
# driver.find_element(By.LINK_TEXT,"Register").click()
# driver.find_element(By.PARTIAL_LINK_TEXT,"Reg").click()
driver.quit()


