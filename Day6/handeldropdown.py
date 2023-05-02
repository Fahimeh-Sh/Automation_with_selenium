from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select

from selenium.webdriver.remote.webelement import WebElement

serv_obj = Service("C:\Drivers\chromedriver_win32\chromedriver.exe")
driver = webdriver.Chrome(service=serv_obj)
driver.get("https://demo.guru99.com/test/delete_customer.php")
driver.maximize_window()
allcountry = Select(driver.find_element(By.XPATH, "//select[@id='input-country']"))
#select option country
# allcountry.select_by_visible_text(["India"])
# allcountry.select_by_value("10")
# allcountry.select_by_index(15)
#print all drop down menue
# allcountryopt = allcountry.options
# for opt in allcountryopt:
#     print(opt.text)
#
# for opt in allcountryopt:
#     if opt.text == "India":
#         opt.click()
#     break

alloptions_country = driver.find_elements(By.XPATH, "//select[@id='input-country']/option")
print(len(alloptions_country))
