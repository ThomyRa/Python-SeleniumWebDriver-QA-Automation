from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec


options = webdriver.ChromeOptions()
options.add_experimental_option("detach", True)
options.add_argument("--start-maximized")
driver = webdriver.Chrome(options)

driver.get("file:///home/thomy/GitHub/MyRepos/Python-SeleniumWebDriver-QA-Automation/04-Waits/page_with_slow_image.html")

# img = WebDriverWait(driver, 10).until(ec.visibility_of_element_located((By.ID, "the_slow_image")))
# if img.is_displayed():
#     print("Pass")

# Is possible to assign the WebDriverWait to a variable in order to be more concise
wait = WebDriverWait(driver, 10)
img = wait.until(ec.visibility_of_element_located((By.ID, "the_slow_image")))
if img.is_displayed():
    print("Pass")
