from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
ops = webdriver.ChromeOptions()
ops.add_argument("--disable-notification")
serv_obj = Service("C:\Drivers\chromedriver_win32\chromedriver.exe")
driver = webdriver.Chrome(service=serv_obj, options=ops)
driver.get("https://whatmylocation.com/")
driver.maximize_window()