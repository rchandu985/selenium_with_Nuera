from selenium import webdriver

from selenium.webdriver.common.by import By

import time


driver=webdriver.Chrome("chromedriver")

#find how text input box in webpage
driver.get("file:///C:/Users/R%20Chandu/Desktop/selenium/test.html")
inp=driver.find_elements(By.CLASS_NAME,"text_field")
print(len(inp))

driver.find_element("id",'f_name').send_keys("R")
driver.find_element("id",'l_name').send_keys("cahndu")
driver.find_element("id",'cell').send_keys("123")
driver.find_element("id",'email').send_keys("chadu")

#selected radio and checkboxes

status=driver.find_element(By.CSS_SELECTOR,"input[value=Male]").is_selected()
print('radio button before unselected ',status)
driver.find_element(By.CSS_SELECTOR,"input[value=Male]").click()
status=driver.find_element(By.CSS_SELECTOR,"input[value=Male]").is_selected()
print('radio button after selected ',status)

c_status=driver.find_element('id',"india").is_selected()
print('radio checkbox before unselected ',c_status)
driver.find_element('id',"india").click()
c_status=driver.find_element('id',"india").is_selected()
print('check box after selected ',c_status)
time.sleep(60)



