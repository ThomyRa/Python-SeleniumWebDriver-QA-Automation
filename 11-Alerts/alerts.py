import time
from selenium import webdriver
from selenium.webdriver.common.by import By
import pdb

options = webdriver.ChromeOptions()
options.add_experimental_option("detach", True)
options.add_argument("--start-maximized")
driver = webdriver.Chrome(options)

url = "file:///home/thomy/GitHub/MyRepos/Python-SeleniumWebDriver-QA-Automation/11-Alerts/alerts_example.html"

driver.get(url)

#########################################################
#  Example 1: Javascript Alert
alert_1_btn = driver.find_element(By.CSS_SELECTOR, "div#jsAlertExample button")
alert_1_btn.click()
# pdb.set_trace()
my_alert = driver.switch_to.alert
assert my_alert.text == "I am a JavaScript Alert", "Unexpected text on alert."
time.sleep(2)
my_alert.accept()
# my_alert.dismiss()

# alert_1_btn = driver.find_element('css selector', 'div#jsAlertExample button')

#########################################################
# Example 2:
my_js_confirm_btn = driver.find_element(By.CSS_SELECTOR, 'div#jsConfirmExample button')
time.sleep(2)
my_js_confirm_btn.click()
my_confirm_alert = driver.switch_to.alert
# my_confirm_alert.accept()
# rs_message = driver.find_element(By.ID, 'userResponse1').text
# assert rs_message == 'Great! You will love it!', "Wrong message after accepting"

my_confirm_alert.dismiss()
rs_message = driver.find_element('id', 'userResponse1').text
assert rs_message == "Too bad!!! You would've loved it!", "Wrong message after accepting"
