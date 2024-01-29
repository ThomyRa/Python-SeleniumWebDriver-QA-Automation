from selenium import webdriver
from selenium.webdriver.common.by import By

options = webdriver.ChromeOptions()
options.add_experimental_option("detach", True)
options.add_argument("--start-maximized")

driver = webdriver.Chrome(options)
driver.implicitly_wait(5)

driver.get('http://demostore.supersqa.com')

cart = driver.find_element(By.ID, 'site-header-cart')
cart.click()

driver.get('http://demostore.supersqa.com/my-account/')
u_name = driver.find_element(By.ID, 'username')
u_name.send_keys('myusername')
