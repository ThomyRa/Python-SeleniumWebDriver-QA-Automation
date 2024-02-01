from selenium import webdriver
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.by import By
import pdb

options = webdriver.ChromeOptions()
options.add_experimental_option("detach", True)
options.add_argument("--start-maximized")
driver = webdriver.Chrome(options)

url = "file:///home/thomy/GitHub/MyRepos/Python-SeleniumWebDriver-QA-Automation/08-Dropdowns/drop_down_example.html"

driver.get(url)

##################################################
# Option 1 is using the Select class

my_dropdown = driver.find_element(By.ID, "age-range-select")
dropdown_object = Select(my_dropdown)
dropdown_object.select_by_index(3)
dropdown_object.select_by_value("21-40")
all_options = dropdown_object.options
for option in all_options:
    print(option.text)

##################################################
# Option 2: When web page use Frontend Framewok
dropdown_btn = driver.find_element(By.ID, "dropdownMenuButton")
dropdown_btn.click()
my_option = driver.find_element(By.XPATH, '//*[@id="dropdowns"]/div[2]/div/ul/li[1]/a')
my_option.click()

# pdb.set_trace()
