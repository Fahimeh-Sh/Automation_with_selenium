from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By

serv_obj = Service("C:\Drivers\chromedriver_win32\chromedriver.exe")
driver = webdriver.Chrome(service=serv_obj)
driver.get("https://jqueryui.com/droppable/")
driver.maximize_window()
driver.switch_to.frame(0)
src = driver.find_element(By.CSS_SELECTOR, "#draggable")
tar = driver.find_element(By.CSS_SELECTOR, "#droppable")
a = ActionChains(driver)
a.drag_and_drop(src,tar).perform()
driver.implicitly_wait(150)
driver.quit()
