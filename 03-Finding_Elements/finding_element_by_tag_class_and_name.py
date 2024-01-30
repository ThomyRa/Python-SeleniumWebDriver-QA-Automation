from selenium import webdriver
from selenium.webdriver.common.by import By

options = webdriver.ChromeOptions()
options.add_experimental_option("detach", True)
options.add_argument("--start-maximized")

driver = webdriver.Chrome(options)
driver.get('http://demostore.supersqa.com')

# Finding by 'class name'
product = driver.find_element(By.CLASS_NAME, 'product')
products = driver.find_elements(By.CLASS_NAME, 'product')


# Finding by 'name'
order_by = driver.find_element(By.NAME, 'orderby')
print(order_by.text)

# Finding by 'tag'
all_links = driver.find_elements(By.TAG_NAME, 'a')
print(f"Found number of 'a' tag: {len(all_links)}")
all_li = driver.find_elements(By.TAG_NAME, 'li')
print(f"Found number of 'li' tag: {len(all_li)}")
