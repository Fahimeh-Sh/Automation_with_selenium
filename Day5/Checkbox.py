from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webelement import WebElement

serv_obj = Service("C:\Drivers\chromedriver_win32\chromedriver.exe")
driver = webdriver.Chrome(service=serv_obj)
driver.get("https://itera-qa.azurewebsites.net/home/automation")
driver.maximize_window()
# 1 select check boxes
check_boxes = driver.find_elements(By.XPATH, "//input[@type='checkbox' and contains(@id,'day')]")
print(len(check_boxes))
# how check boxes exist
# first approach to select check boxes
# for i in range(len(check_boxes)):
#     check_boxes[i].click()
# driver.quit()
# secons approch to click check boxes
# for checkbox in check_boxes:
    # checkbox.click()

# selct multiple check boxes with choice
for checkbox in check_boxes:
    weekname = checkbox.get_attribute('id')
    if weekname == 'saturday' or weekname == 'friday':
        checkbox.click()