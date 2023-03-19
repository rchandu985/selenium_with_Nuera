from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
import time

# initialize the Chrome driver
driver = webdriver.Chrome("chromedriver")
# head to github login page
driver.get("https://www.amazon.in/")
c=driver.get_cookies()
print(len(c))
#add cookie to the browser

insert={"name":"chandu",'value':"dopamine"}#its is a single cookie..if need add more cookie..do same {name:"dcbdj",'value:'dcddd'}
driver.add_cookie(insert)
print(len(driver.get_cookies()))
print(driver.get_cookies())

#deleting single cookie
driver.delete_cookie("chandu")
print(len(driver.get_cookies()))

#deleting all cookies

driver.delete_all_cookies()
print(driver.get_cookies())


time.sleep(10)
driver.quit()