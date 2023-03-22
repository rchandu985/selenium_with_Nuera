from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
import time

# initialize the Chrome driver
driver = webdriver.Chrome("chromedriver")
# head to github login page
driver.get("file:///C:/Users/R%20Chandu/selenium_with_Nuera/test.html")
driver.find_element("id",'click').click()
#switching to the alert and accepting
time.sleep(10)
driver.switch_to.alert.accept()
#cancel the alert
#driver.switch_to.alert.dismiss()
time.sleep(10)
