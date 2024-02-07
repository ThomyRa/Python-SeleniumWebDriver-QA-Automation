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

# my_heading = driver.find_element('xpath', '/html/body/h1').text
print("Before switching focus: " + driver.title)


