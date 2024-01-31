from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.common.by import By

options = webdriver.ChromeOptions()
options.add_experimental_option("detach", True)
options.add_argument("--start-maximized")
driver = webdriver.Chrome(options)
wait = WebDriverWait(driver, 5)

url = "file:///home/thomy/GitHub/MyRepos/Python-SeleniumWebDriver-QA-Automation/05-Present_vs_Displayed/Example2/present_vs_visible_example_with_cars.html"
driver.get(url)

# Element is not interactable
# series_6 = driver.find_element(By.CSS_SELECTOR, "#bmw-models > label:nth-child(2)")
# series_6.click()

# Element is located but not clickable
# series_6 = wait.until(ec.presence_of_element_located((By.CSS_SELECTOR, '#bmw-models > input[type=checkbox]:nth-child(7)')))

# In order to click element, first navigate to that element
driver.find_element(By.CSS_SELECTOR, '#bmw').click()
series_6 = wait.until(ec.element_to_be_clickable((By.CSS_SELECTOR, '#bmw-models > input[type=checkbox]:nth-child(7)')))
series_6.click()
