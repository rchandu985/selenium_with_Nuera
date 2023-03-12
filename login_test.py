from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
import time
# Github credentials
username = "coffeeday@gndsolutions.in"
password = "coffeeday@123"

# initialize the Chrome driver
driver = webdriver.Chrome("chromedriver")
# head to github login page
driver.get("https://dash.thinxview.com/auth/login")

# find username/email field and send the username itself to the input field
driver.find_element("id", "username").send_keys(username)
# find password input field and insert password as well
driver.find_element("id", "password").send_keys(password)
# click login button

driver.find_element(By.XPATH,'//button[text()="SIGN IN"]').click()
# wait the ready state to be complete
time.sleep(60)
WebDriverWait(driver=driver, timeout=60).until(
    lambda x: x.execute_script("return document.readyState === 'complete'")
)
error_message = "Incorrect username or password."
# get the errors (if there are)
errors = driver.find_elements("css selector", ".flash-error")
# print the errors optionally
# for e in errors:
#     print(e.text)
# if we find that error message within errors, then login is failed
if any(error_message in e.text for e in errors):
    print("[!] Login failed")
else:
    print("[+] Login successful")
    
