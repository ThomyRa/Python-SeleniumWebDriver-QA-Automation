from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

options = webdriver.ChromeOptions()
options.add_experimental_option("detach", True)
options.add_argument("--start-maximized")
driver = webdriver.Chrome(options)


##################################
# Example 1: Sending regular keys
# driver.get('http://demostore.supersqa.com/my-account/')
# u_name = driver.find_element(By.ID, "username")
# u_name.send_keys("SendingKeys")
#
# p_field = driver.find_element(By.ID, "password")
# p_field.send_keys("mypassword")
#
# submit_btn = driver.find_element(By.CSS_SELECTOR, "#customer_login > div.u-column1.col-1 > form > p:nth-child(3) > button")
# submit_btn.click()


##################################
# Example 2 Sending special keys: ENTER
# driver.get("http://demostore.supersqa.com")
#
# search_field = driver.find_element(By.ID, "woocommerce-product-search-field-0")
# search_field.send_keys("hoodie")
# time.sleep(3)
# search_field.send_keys(Keys.ENTER)

##################################
# Example 2 Sending special Keys: TAB
driver.get("http://demostore.supersqa.com/my-account/")
u_name = driver.find_element(By.ID, "username")
u_name.send_keys("abcd")
time.sleep(3)
u_name.send_keys(Keys.TAB)
