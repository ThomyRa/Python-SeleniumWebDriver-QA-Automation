from selenium import webdriver
from selenium.webdriver.common.by import By

# Options for the browser when launching it
options = webdriver.ChromeOptions()
options.add_experimental_option("detach", True)
options.add_argument("--start-maximized")

# Getting the driver
driver = webdriver.Chrome(options)

# Open the browser and go to the url
driver.get("https://www.selenium.dev/selenium/web/web-form.html")

# Verifying the title of the page via assertion
title = driver.title
assert title == "Web form"

driver.implicitly_wait(0.5)

# Locating and getting the text box
text_box = driver.find_element(by=By.NAME, value="my-text")
# Locating and getting the submit button
submit_button = driver.find_element(by=By.CSS_SELECTOR, value="button")

# Inserting the "Selenium" text in the text box
text_box.send_keys("Selenium")
# Pressing the submit button
submit_button.click()

# Locating and getting the resulting message
message = driver.find_element(by=By.ID, value="message")
value = message.text
# Verifying that the value of the resulting message is "Received!"
assert value == "Received!"

# Closing the broser and end the webdriver sesion
# driver.quit()
