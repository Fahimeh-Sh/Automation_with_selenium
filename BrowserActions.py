from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from time import sleep

serv_obj = Service("C:\Drivers\chromedriver_win32\chromedriver.exe")
driver = webdriver.Chrome(service=serv_obj)

# Browser Action 1 > Open Web google.com
driver.get("http://google.com")
sleep(1)

# Browser Action 2 > Refresh
driver.refresh()
sleep(1)

# Browser Action 3 > Open new window and switch to new tab
driver.switch_to.new_window('tab')
sleep(1)

# Browser Action 3 > Open new window and switch to new window
driver.switch_to.new_window('window')
driver.get("http://yahoo.com")
sleep(1)

# Browser Action 4 > current window
current_window = driver.current_window_handle
print('current handle :', str(current_window))

# Browser Action 5 > All window
all_handles = driver.window_handles
print('all_handles :', str(all_handles))

# Browser Action 6 > Switch
driver.switch_to.window(all_handles[0])
sleep(1)

# Browser Action 7 > get window size
window_size = driver.get_window_size()
print('window size is :', window_size)

# Browser Action 8 > set window size
driver.set_window_size(800, 600)
sleep(2)

# Browser Action 9 > get window position
window_position = driver.get_window_position()
print('window position', window_position)
sleep(1)

# Browser Action 10 > Close tab
driver.close()
sleep(1)

# Browser Action 11 > Quit session
driver.quit()