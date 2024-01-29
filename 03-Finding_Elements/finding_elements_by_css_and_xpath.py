from selenium import webdriver
from selenium.webdriver.common.by import By
import time


options = webdriver.ChromeOptions()
options.add_experimental_option("detach", True)
options.add_argument("--start-maximized")

driver = webdriver.Chrome(options)

driver.get('http://demostore.supersqa.com')

# Finding elements by CSS_SELECTOR: ID
# cart = driver.find_element(By.CSS_SELECTOR, '#site-header-cart')
# time.sleep(3)
# cart.click()

# Finding Elements by CSS_SELECTOR
# my_acct = driver.find_element(By.CSS_SELECTOR, '#site-navigation > div:nth-child(2) > ul > li.page_item.page-item-9 > a')
# time.sleep(3)
# my_acct.click()

# Finding Elements by XPATH
my_acct = driver.find_element(By.XPATH, '//*[@id="site-navigation"]/div[1]/ul/li[4]/a')
time.sleep(3)
my_acct.click()

# time.sleep(3)
# driver.quit()