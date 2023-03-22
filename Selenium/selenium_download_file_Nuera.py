from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By

import time


# initialize the Chrome driver
driver = webdriver.Chrome("chromedriver")
driver.maximize_window()
# head to github login page
driver.get("https://demo.automationtesting.in/FileDownload.html")
driver.find_element(By.XPATH,"//textarea[@id='textbox']").send_keys("hi..im new")
time.sleep(3)
driver.find_element("id","createTxt").click()
time.sleep(2)
driver.find_element("id","link-to-download").click()
time.sleep(10)
driver.quit()
