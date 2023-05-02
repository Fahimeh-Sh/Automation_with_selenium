# Methods
# The methods to handle new pop-ups are listed below:
#  driver.current_window_handle: To obtain the handle id of the window in
# focus.
#  driver.window_handles:To obtain the list of all the opened window handle ids.
#  driver.swtich_to.window(<window handle id>):To switch the webdriver
# control to an opened window whose handle id is passed as a parameter to the
# method.

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

serv_obj = Service("C:\Drivers\chromedriver_win32\chromedriver.exe")
driver = webdriver.Chrome(service=serv_obj)
driver.get("https://demo.guru99.com/test/delete_customer.php")
driver.maximize_window()
driver.find_element(By.XPATH, "//input[@name='cusid']").send_keys("Cutomer155")
driver.find_element(By.XPATH, "//input[@name='submit']").click()
driver.implicitly_wait(25)
#current main window handle
m = driver.current_window_handle
# alert = driver.window_handles

alert = driver.switch_to.alert
alertMessage = driver.switch_to.alert.text
print("first alert message " + alertMessage)
driver.implicitly_wait(25)
alert.accept()
# alert.dismiss()
alert = driver.switch_to.alert
alertMessage_accept = driver.switch_to.alert.text
print("second alert message " + alertMessage_accept)
driver.implicitly_wait(25)
alert.accept()

# for h in driver.window_handles:
#     if h != m:
#         driver.switch_to.window(h)
#     print(driver.title)
#

#iterate over all window handles
#check for main window handle
# for h in driver.window_handles:
#     if h != m:
#         n = h
#     driver.switch_to.window(n)
# # driver.close()
# driver.quit()
