from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
import time

# initialize the Chrome driver
driver = webdriver.Chrome("chromedriver")
# head to github login page
driver.get("https://www.epfindia.gov.in/site_en/index.php")
driver.find_element(By.XPATH,"//*[@id='nav']/li[8]/a").click()
print(driver.current_window_handle)#prints parent window
handles=driver.window_handles

#get all windows info
for h in handles:
    driver.switch_to.window(h)
    print(driver.title,driver.current_url)
time.sleep(10)
driver.close()  
