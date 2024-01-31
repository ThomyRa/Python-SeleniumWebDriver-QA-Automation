from selenium import webdriver
from selenium.webdriver.common.by import By
import pdb

options = webdriver.ChromeOptions()
options.add_experimental_option("detach", True)
options.add_argument("--start-maximized")
driver = webdriver.Chrome(options)
driver.get('http://demostore.supersqa.com')

###########################################
# Getting Attribute "placeholder"
# search_field = driver.find_element(By.ID, "woocommerce-product-search-field-0")
# place_holder = search_field.get_attribute("placeholder")
# if place_holder != "Search products…":
#     raise Exception(f"Place holder for search field is not as expected. Actual: {place_holder}")
# else:
#     print("PASS")

###########################################
# Check which tab is selected
# first click on my account
# my_account = driver.find_element(By.CSS_SELECTOR, "li.page-item-9")
# my_account.click()
#
# nav_items = driver.find_elements(By.CSS_SELECTOR, "ul.nav-menu li")
# for item in nav_items:
#     # pdb.set_trace()
#     item_class = item.get_attribute("class")
#     if "current_page_item" in item_class:
#         print(f"The selected tab is: {item.text}")

###########################################
# Getting link url
product_link = driver.find_element(By.CSS_SELECTOR, "li.product a")
product_url = product_link.get_attribute("href")
print(f"The url for product is: {product_url}")
