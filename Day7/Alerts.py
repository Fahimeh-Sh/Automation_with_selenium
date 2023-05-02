import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By


from selenium.webdriver.remote.webelement import WebElement

serv_obj = Service("C:\Drivers\chromedriver_win32\chromedriver.exe")
driver = webdriver.Chrome(service=serv_obj)
driver.get("https://the-internet.herokuapp.com/javascript_alerts")
driver.maximize_window()
driver.find_element(By.XPATH, "//button[@onclick='jsPrompt()']").click()
time.sleep(5)
alertwindow = driver.switch_to.alert
print(alertwindow.text)
alertwindow.send_keys("Welcome fahime")
alertwindow.accept() #close alert window by using ok button
alertwindow.dismiss()#close alert window by using cancel button

