from selenium import webdriver
from selenium.webdriver.common.by import By
import pdb

options = webdriver.ChromeOptions()
options.add_experimental_option("detach", True)
options.add_argument("--start-maximized")
driver = webdriver.Chrome(options)

url = "file:///home/thomy/GitHub/MyRepos/Python-SeleniumWebDriver-QA-Automation/13-Multiple_Windows_and_Tabs/windows-and_tabs_example.html"
driver.get(url)

driver.find_element(By.XPATH, '//*[@id="windows"]/a[1]').click()

# This statement fail because element not in focus
# my_heading = driver.find_element('xpath', '/html/body/h1').text
print("Before switching focus: " + driver.title)

# Getting current window/tab handle
original_window_handle = driver.current_window_handle

# Getting all windows/tabs handles as a list
all_window_handles = driver.window_handles

# Getting the actual window/tab after opened
new_window = all_window_handles[1]

# Switching to new window
driver.switch_to.window(new_window)
print("After switching focus: " + driver.title)

# We can close the new tab with
print("Closing tab...")
driver.close()

# After closing the window/tab, we can switch back to original
print("Switching to original window")
driver.switch_to.window(all_window_handles[0])
print("After switching focus: " + driver.title)

