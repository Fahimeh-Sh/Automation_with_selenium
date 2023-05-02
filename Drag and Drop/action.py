# Methods
# The methods of ActionChains class are listed below:
#  click: It is used to click a webelement.
#  click_and_hold: It is used to hold down the left mouse button on a webelement.
#  double_click: It is used to double click a webelement.
#  context_click: It is used to right click a webelement.
#  drag_and_drop_by_offset: It is used to first perform pressing the left mouse
# on the source element, navigating to the target offset and finally releasing the
# mouse.
#  drag_and_drop: It is used to first perform pressing the left mouse on the
# source element, navigating to the target element and finally releasing the mouse.
#  key_up: It is used to release a modifier key.
#  key_down: It is used for a keypress without releasing it.
# 11. Selenium Webdriver — Action ClassSelenium Webdriver
# 55
#  move_to_element: It is used to move the mouse to the middle of a
# webelement.
#  move_by_offset: It is used to move the mouse to an offset from the present
# mouse position.
#  Perform: It is used to execute the queued actions.
#  move_to_element_by_offset: It is used to move the mouse by an offset of a
# particular webelement. The offsets are measured from the left-upper corner of
# the webelement.
#  Release: It is used to release a held mouse button on a webelement.
#  Pause: It is used to stop every input for a particular duration in seconds.
#  send_keys: It is used to send keys to the present active element.
#  reset_actions: It is used to delete all actions that are held locally and in remote

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By

serv_obj = Service("C:\Drivers\chromedriver_win32\chromedriver.exe")
driver = webdriver.Chrome(service=serv_obj)

driver.get("https://www.tutorialspoint.com/about/about_careers.htm")
driver.maximize_window()
a = ActionChains(driver)
pp = driver.find_element(By.XPATH, "//a[contains(text(),'Privacy Policy')]")
a.move_to_element(pp)
a.click().perform()
print("page Title " + driver.title)
# driver.close()