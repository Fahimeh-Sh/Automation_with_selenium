from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webelement import WebElement

serv_obj = Service("C:\Drivers\chromedriver_win32\chromedriver.exe")
driver = webdriver.Chrome(service=serv_obj)
driver.get("http://demo.nopcommerce.com/register")
driver.maximize_window()
#find_elemet() -returns single one element
# 1 locator matching with single one webelement
# element = driver.find_element(By.XPATH,"//input[@id='small-searchterms']")
# element.send_keys("Apple Mac book pro")
# 2 locator matching with multiple web elements
# element1 = driver.find_element(By.XPATH, "//div[@class='footer']//a")
#prints first link from the footer "Sitemap"
# print(element1.text)

# 3 Element not avalible through no such element exception
# element3 = driver.find_element((By.LINK_TEXT, "Log in"))
# element3.click()

#4 find_elemets() - Return multiple web element
#1)Locator matching with single webelement
# elements = driver.find_element(By.XPATH, "//input[@id='small-searchterms']")

# element5 = driver.find_elements(By.XPATH, "//div[@class='footer']//a")
# print(element5[0])
# print(element5[len(element5)-1])
# for ele in element5:
#     print(ele.text)

# 5 element not avalible Zero
elements = driver.find_elements(By.LINK_TEXT, "log")
print("elements  returned :", len(elements))
