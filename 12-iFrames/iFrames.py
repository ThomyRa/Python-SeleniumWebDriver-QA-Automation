"""
NOTES:
    to switch to the frame use
        WebElement
        ID
        NAME
        INDEX
"""

from selenium import webdriver
from selenium.webdriver.common.by import By

options = webdriver.ChromeOptions()
options.add_experimental_option("detach", True)
options.add_argument("--start-maximized")
driver = webdriver.Chrome(options)

url = "file:///home/thomy/GitHub/MyRepos/Python-SeleniumWebDriver-QA-Automation/12-iFrames/iFrames_example.html"

driver.get(url)

#####################################################
# Example without iFrame
# driver.find_element(By.ID, 'btnOutFrame').click()
# my_alert = driver.switch_to.alert
# my_alert_text = my_alert.text
# assert my_alert_text == 'Just Clicked Outside iFrame', "Should've gotten outside message"
# my_alert.dismiss()

#####################################################
# Example of iFrame: Using 'WebElement'
my_frame = driver.find_element(By.ID, 'myFrame1')
driver.switch_to.frame(my_frame)
driver.find_element(By.ID, 'btnInFrame').click()
print(driver.switch_to.alert.text)
driver.switch_to.alert.dismiss()

driver.switch_to.default_content()
driver.find_element(By.ID, 'btnOutFrame').click()
driver.switch_to.alert.dismiss()
