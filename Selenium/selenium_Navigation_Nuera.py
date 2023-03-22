from selenium import webdriver
import time

driver=webdriver.Chrome("chromedriver")
#1 st url
driver.get("https://dash.thinxview.com/auth/login")
time.sleep(5)
print(driver.title)


#opening 2nd url in same tabe

driver.get("https://www.facebook.com/")
time.sleep(5)
print(driver.title)


#coming to backward to 1st url

driver.back()
time.sleep(5)
print(driver.title)

#going to 2nd url..forward

driver.forward()
time.sleep(5)
print(driver.title)

