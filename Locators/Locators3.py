from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webelement import WebElement

serv_obj = Service("C:\Drivers\chromedriver_win32\chromedriver.exe")
driver = webdriver.Chrome(service=serv_obj)
driver.get("https://www.facebook.com/")
driver.maximize_window()

#Css Tag and ID = tagname#valueofID
# driver.find_element(By.CSS_SELECTOR,"input#email").send_keys('fahime.shafiee@gmail.com')
# driver.find_element(By.CSS_SELECTOR,"#email").send_keys('fahime.shafiee@gmail.com')

#tag and Class combination = tagname#valueofClass
# driver.find_element(By.CSS_SELECTOR,"input.inputtext").send_keys('fahimeh.shafiee@gmail.com')
# driver.find_element(By.CSS_SELECTOR,".inputtext").send_keys('fahimeh.shafiee@gmail.com')

#tag attribute = tagname[attribute=value]
# driver.find_element(By.CSS_SELECTOR,"input[data-testid=royal_email]").send_keys("fahime.shafiee@gmail.com")
# driver.find_element(By.CSS_SELECTOR,"[data-testid=royal_email]").send_keys("fahime.shafiee@gmail.com")

#tag class attribute tagname.valueofclass[attribute=value]
driver.find_element(By.CSS_SELECTOR,"input.inputtext[data-testid=royal_email]").send_keys('fahimeh.shafiee@gmail.com')
driver.find_element(By.CSS_SELECTOR,"input.inputtext[data-testid=royal_pass]").send_keys('password')