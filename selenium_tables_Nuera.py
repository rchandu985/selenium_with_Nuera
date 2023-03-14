from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
import time

driver=webdriver.Chrome('chrome')
driver.get("C:/Users/R%20Chandu/selenium_with_Nuera/test.html")
n_row=driver.find_elements(By.XPATH,"/html/body/table/tbody/tr")
n_col=driver.find_elements(By.XPATH,"/html/body/table/tbody/tr[1]/th")    
for x in n_row:
    print(x.text)
for k in n_col:
    print(k.text)
time.sleep(20)