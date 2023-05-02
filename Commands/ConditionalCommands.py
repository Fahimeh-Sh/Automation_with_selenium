from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webelement import WebElement

serv_obj = Service("C:\Drivers\chromedriver_win32\chromedriver.exe")
driver = webdriver.Chrome(service=serv_obj)
driver.get("http://demo.nopcommerce.com/register")
driver.maximize_window()

searchbox = driver.find_element(By.XPATH, "//input[@id='small-searchterms']")
print("Display Status : ", searchbox.is_displayed())
print("Diaplay Status:", searchbox.is_enabled())
print("siaplay Status:", searchbox.is_selected())

rd_male = driver.find_element(By.XPATH, "//input[@id='gender-male']")
rd_female = driver.find_element(By.XPATH, "//input[@id='gender-female']")

print("Default radio button status")
print(rd_male.is_selected())
print(rd_female.is_selected())

#after male radio button selected
rd_male.click()
print(rd_male.is_selected())
print(rd_female.is_selected())

#after female radio button selected
rd_female.click()
print(rd_male.is_selected())
print(rd_female.is_selected())
driver.quit()

#conditional commands
#is_displayed()
#is_enabaled()
#is_selected()
