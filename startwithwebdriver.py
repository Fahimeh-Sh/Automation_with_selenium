from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from time import sleep

serv_obj = Service("C:\Drivers\chromedriver_win32\chromedriver.exe")
driver = webdriver.Chrome(service=serv_obj)

# browser action 1 open google
driver.get("http://google.com")
# browser action 2 maximize_window
driver.maximize_window()
sleep(3)
# browser action 3 minimize_window
driver.minimize_window()
sleep(3)
# browser action 4 fullscreen
driver.fullscreen_window()
sleep(3)
# tear down
driver.find_element(By.NAME, 'q').send_keys("hi selenium")
sleep(3)
# print current browser title
print(driver.title)

# browser action back
driver.get("http://wikipedia.com")
sleep(1)
driver.back()

# browser action forward
driver.forward()
sleep(1)

driver.quit()