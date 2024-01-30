from selenium import webdriver
from selenium.webdriver.common.by import By

options = webdriver.ChromeOptions()
options.add_experimental_option("detach", True)
options.add_argument("--start-maximized")
driver = webdriver.Chrome(options)

driver.get('http://demostore.supersqa.com')

cart_elm = driver.find_element(By.LINK_TEXT, 'Cart')
print(cart_elm.text)

acct_elm = driver.find_element(By.LINK_TEXT, 'My account')
print(acct_elm.text)

acct_elm_p = driver.find_element(By.PARTIAL_LINK_TEXT, 'account')
print(acct_elm_p.text)

footer_link = driver.find_element(By.PARTIAL_LINK_TEXT, 'Built with Storefront')
print(footer_link.text)

# Must be <a> tag or it will fail
# driver.find_element(By.LINK_TEXT, '0 items')
