from selenium import webdriver
from selenium.webdriver.common.by import By
import time

# Options for the browser when launching it
options = webdriver.ChromeOptions()
options.add_experimental_option("detach", True)
options.add_argument("--start-maximized")

# Getting the driver
driver = webdriver.Chrome(options)
driver.implicitly_wait(5)

# Go to url
driver.get("http://demostore.supersqa.com/")
time.sleep(3)

# Click on 'My Account' tab
my_acct_tab = driver.find_element(By.LINK_TEXT, "My account")
my_acct_tab.click()
time.sleep(3)

# Scroll the page up
driver.execute_script("window.scrollBy(0,300)")

# Find username field and input username
u_name_field = driver.find_element(By.ID, "username")
u_name_field.send_keys("fakename")

# Find password field and input username
p_field = driver.find_element(By.ID, "password")
p_field.send_keys("aaaaaaa")

# Click login button
login_btn = driver.find_element(By.NAME, 'login')
login_btn.click()
time.sleep(3)

# Get displayed error
errors_list_elm = driver.find_elements(By.CSS_SELECTOR, 'ul.woocommerce-error li')
first_error_elm = errors_list_elm[0]
displayed_error_text = first_error_elm.text

# Verify the displayed error is as expected
expected_error = "Error: The password you entered for the username fakename is incorrect. Lost your password?"
assert expected_error == displayed_error_text, "Displayed error is not as expected."
print("Success.")

# Close the browser
driver.quit()
