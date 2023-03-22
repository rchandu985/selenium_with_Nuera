from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import time

driver=webdriver.Chrome("chromedriver")
driver.get("https://dash.thinxview.com/auth/login")
get_title=driver.title
current_url=driver.current_url
page_source=driver.page_source

#click sign in button using xpath location
driver.find_element(By.XPATH,"//*[@id='__next']/section/div/div[2]/div[2]/form/button").click()

time.sleep(10)

driver.close()#it closes only current tab
#driver.quit() # it closed whole browser