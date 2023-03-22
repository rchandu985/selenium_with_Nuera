from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
import time

# initialize the Chrome driver
driver = webdriver.Chrome("chromedriver")
# head to github login page
driver.get("https://dash.thinxview.com/auth/login")

#extracting the how many link present in webpage
a=driver.find_elements(By.TAG_NAME,'a')
print(len(a))
for link in a:
    print("Link Name : ",link.text)

#selecting the link

# 1 Link_TEXT ..we specify the full link text 
driver.find_element(By.LINK_TEXT,"Signup").click()
driver.get("https://dash.thinxview.com/register")
driver.find_element(By.LINK_TEXT,'Login').click()

# 2 PARTIAL_LINK_TEXT...pass the small text in link..ex : Signup..now pass Sig
time.sleep(10)
driver.find_element(By.PARTIAL_LINK_TEXT,'Sig').click()
time.sleep(120)