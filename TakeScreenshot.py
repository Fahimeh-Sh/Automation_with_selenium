from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from time import sleep
import os
from pathlib import Path

serv_obj = Service("C:\Drivers\chromedriver_win32\chromedriver.exe")
driver = webdriver.Chrome(service=serv_obj)
driver.get("http://amazoon.com")
sleep(5)
driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
current_path = Path(__file__).parent
file_name = os.path.join(str(current_path), 'Amazoon.png')
driver.save_screenshot(file_name)