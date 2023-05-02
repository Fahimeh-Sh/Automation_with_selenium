from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from time import sleep
from selenium.webdriver.common.by import By

serv_obj = Service("C:\Drivers\chromedriver_win32\chromedriver.exe")
driver = webdriver.Chrome(service=serv_obj)
driver.get("https://www.wikipedia.org/")

# find elemet by ID
driver.find_element(By.ID, 'searchInput').send_keys('Python')

# find element by Xpath
driver.find_element(By.XPATH, "//input[@id='searchInput']").send_keys(('Python'))

# find element by Name
driver.find_element(By.NAME, 'search').send_keys('Python')

# find element by css selector
driver.find_element(By.CSS_SELECTOR, '#searchInput').send_keys('Pyhton')

# find element by partial link text
driver.find_element(By.PARTIAL_LINK_TEXT, 'Download').send_keys()

# find element by link text
# driver.find_element((By.LINK_TEXT, 'Download Wikipedia for Android or iOS'))