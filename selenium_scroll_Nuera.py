from selenium import webdriver

from selenium.webdriver.common.by import By

import time


driver=webdriver.Chrome("chromedriver")
#find how text input box in webpage
driver.get("https://www.worldometers.info/geography/flags-of-the-world/")
driver.maximize_window()

#3 ways

# 1 . scroll down page by pixel
# 2 . scroll down page by till element found
# 3 . scroll end of the page

# 1 . scroll down page by pixel

#driver.execute_script("window.scrollBy(0,1000)","")

# 2 . scroll down page by till element found
#flag=driver.find_element(By.XPATH,"/html/body/div[3]/div[2]/div[1]/div/div/div/div[79]/div/a/img")
#driver.execute_script("arguments[0].scrollIntoView(true);",flag)

# 3 . scroll end of the page
driver.execute_script('window.scrollBy(0,document.body.scrollHeight)')
time.sleep(10)