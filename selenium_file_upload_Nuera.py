from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
import time

# initialize the Chrome driver
driver = webdriver.Chrome("chromedriver")
# head to github login page
driver.get("https://www.tutorialspoint.com/selenium/selenium_automation_practice.htm")
driver.find_element(By.XPATH,"//input[@type='file']").send_keys('C:/Users/R Chandu/selenium_with_Nuera/upload_test.txt')


time.sleep(10)
driver.quit()