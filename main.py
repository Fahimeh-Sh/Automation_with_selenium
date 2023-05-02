import time

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from solverecaptcha import solveRecaptcha
serv_obj = Service("C:\Drivers\chromedriver_win32\chromedriver.exe")
driver = webdriver.Chrome(service=serv_obj)
driver.get("https://phptravels.com/demo/")
driver.find_element(By.NAME,"first_name").send_keys("fahimeh")
driver.find_element(By.NAME,"last_name").send_keys("shafiei")
driver.find_element(By.NAME,"business_name").send_keys("Art painting")
driver.find_element(By.NAME,"email").send_keys("fahime.shafiei@gmail.com")

driver.find_element(By.ID,"demo").send_keys()

time.sleep(15)
#checkBox = driver.find_element_by_id("recaptcha-checkbox-spinner")
#checkBox.click()
time.sleep(15)
#result = solveRecaptcha("6LdX3JoUAAAAAFCG5tm0MFJaCF3LKxUN4pVusJIF","https://phptravels.com/demo/" )
#code = result['code']
#print (result)


#driver.get('https://phptravels.com/demo/')
#WebDriverWait(driver, 20).until(EC.frame_to_be_available_and_switch_to_it((By.CSS_SELECTOR,"iframe[title='reCAPTCHA']")))
#WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "div.recaptcha-checkbox-border"))).click()
time.sleep(100)
