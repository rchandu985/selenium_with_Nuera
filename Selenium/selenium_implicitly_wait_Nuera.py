from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import time

driver=webdriver.Chrome("chromedriver")
driver.get("https://dash.thinxview.com/auth/login")


#when the page is taking time to load..the implicity_wait a specified time in seconds..it is applicatble for all elements in html 
driver.implicitly_wait(10)
get_title=driver.title
assert "Thinxview Dashboard" in get_title

username = "coffeeday@gndsolutions.in"
password = "coffeeday@123"

driver.find_element('id','username').send_keys(username)
driver.find_element('id','password').send_keys(password)
driver.find_element(By.XPATH,"//*[@id='__next']/section/div/div[2]/div[2]/form/button").click()
time.sleep(20)