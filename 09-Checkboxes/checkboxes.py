from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import pdb

options = webdriver.ChromeOptions()
options.add_experimental_option("detach", True)
options.add_argument("--start-maximized")
driver = webdriver.Chrome(options)

time.sleep(2)
url = "file:///home/thomy/GitHub/MyRepos/Python-SeleniumWebDriver-QA-Automation/09-Checkboxes/checkbox_example.html"
driver.get(url)
time.sleep(2)

# Example 1
# to_select_value = '61-80'
# locator_by_value = f'input[name="age-group-checkbox"][value="{to_select_value}"]'
#
# my_choice = driver.find_element(By.CSS_SELECTOR, locator_by_value)
# my_choice.click()
# pdb.set_trace()
# assert my_choice.is_selected(), f"After clicking value {to_select_value} it is not selected."

# Example 2
# verify number of checkboxes and if they are selectable
expected_number_of_options = 4
all_checkboxes = driver.find_elements(By.NAME, 'age-group-checkbox')
assert len(all_checkboxes) == expected_number_of_options, "Number of checkboxes is not the expected"

for checkbox in all_checkboxes:
    checkbox.click()
    time.sleep(2)
    value = checkbox.get_attribute('value')
    if checkbox.is_selected():
        print(f"Checkbox with value '{value}' is selectable")
    else:
        raise Exception(f"Value '{value}' is not selectable")
