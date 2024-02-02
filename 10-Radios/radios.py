from selenium import webdriver
from selenium.webdriver.common.by import By
import pdb


options = webdriver.ChromeOptions()
options.add_experimental_option("detach", True)
options.add_argument("--start-maximized")
driver = webdriver.Chrome(options)

url = "file:///home/thomy/GitHub/MyRepos/Python-SeleniumWebDriver-QA-Automation/10-Radios/radios_example.html"

driver.get(url)

expected_default_value = '21-40'
locator_by_value = f'input[name="age-group-radio"][value="{expected_default_value}"]'

# # Example 1. verify default is selected
# default_element = driver.find_element(By.CSS_SELECTOR, locator_by_value)
# assert default_element.is_selected(), f"The default value of {expected_default_value} is not selected."

# Ex 2
expected_values = ['21-40', '41-60', '61-80', '81+']
all_radios = driver.find_elements(By.NAME, 'age-group-radio')
assert len(all_radios) == len(expected_values), \
    f"the number of radios does not match the expected. Expected: {len(expected_values)}, Actual: {len(all_radios)}"

