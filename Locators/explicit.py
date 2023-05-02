# Explicit Wait
# An explicit wait is applied to instruct the webdriver to wait for a specific condition before
# moving to the other steps in the automation script
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait

serv_obj = Service("C:\Drivers\chromedriver_win32\chromedriver.exe")
driver = webdriver.Chrome(service=serv_obj)
driver.get("https://www.tutorialspoint.com/about/about_careers.htm")
driver.find_element(By.LINK_TEXT, "Team").click()
w = WebDriverWait(driver, 5)
w.until(EC.presence_of_element_located(By.TAG_NAME, 'h1'))
s = driver.find_element(By.TAG_NAME, 'h1')
print("text is " + s.text)
driver.quit()

# Explicit Wait
# An explicit wait is applied to instruct the webdriver to wait for a specific condition before
# moving to the other steps in the automation script
driver.implicitly_wait(5)
# Selenium Webdriver provides two types of waits - implicit & explicit.
# An explicit wait makes WebDriver wait for a certain condition to occur before
# proceeding further with execution. An implicit wait makes WebDriver poll
# the DOM for a certain amount of time when trying to locate an element.