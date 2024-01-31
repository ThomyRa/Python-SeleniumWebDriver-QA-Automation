from selenium import webdriver
from selenium.webdriver.common.by import By
import pdb


options = webdriver.ChromeOptions()
options.add_experimental_option("detach", True)
options.add_argument("--start-maximized")
driver = webdriver.Chrome(options)
driver.implicitly_wait(5)

url = "file:///home/thomy/GitHub/MyRepos/Python-SeleniumWebDriver-QA-Automation/05-Present_vs_Displayed/present_vs_displayed.html"
driver.get(url)

my_btn1 = driver.find_element(By.ID, 'btn1')
my_btn1_txt = my_btn1.text
print(f"First button text: {my_btn1_txt}")

my_btn2 = driver.find_element(By.ID, 'btn2')
print(f"Second button text: {my_btn2.text}")

my_btn3 = driver.find_element(By.ID, 'btn3')
print(f"Third button text: {my_btn3.text}")

my_btn4 = driver.find_element(By.ID, 'btn4')
print(f"Fourth button text: {my_btn4.text}")

if my_btn4.is_displayed():
    my_btn4.click()
else:
    pdb.set_trace()
    raise Exception("Button 4 is not displayed")
