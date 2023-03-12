from selenium import webdriver

from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
import time


driver=webdriver.Chrome("chromedriver")

#find how text input box in webpage
driver.get("file:///C:/Users/R%20Chandu/selenium_with_Nuera/test.html")

#find the how many options present in dropdown
drp=Select(driver.find_element("id",'drop'))
print(len(drp.options))

#extracting the dropdown values
for op in drp.options:
    print(op.text)
#selec the value in dropdown
drp.select_by_visible_text('india')
time.sleep(10)