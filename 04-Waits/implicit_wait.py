from selenium import webdriver
from selenium.webdriver.common.by import By

options = webdriver.ChromeOptions()
options.add_experimental_option("detach", True)
options.add_argument("--start-maximized")
driver = webdriver.Chrome(options)
driver.implicitly_wait(10)

driver.get("file:///home/thomy/GitHub/MyRepos/Python-SeleniumWebDriver-QA-Automation/04-Waits/page_with_slow_image.html")

img = driver.find_element(By.ID, "the_slow_image")
img.click()
print("Image found!")

driver.quit()
