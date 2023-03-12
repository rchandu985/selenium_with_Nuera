from selenium import webdriver
from selenium.webdriver.common.by import By
import time

driver=webdriver.Chrome("chromedriver")
#1 st url
driver.get("https://dash.thinxview.com/auth/login")

#conditional statements
#is_displayed
#is_enabled
#is_selected

username=driver.find_element("id",'username')
password=driver.find_element("id",'password')

#checking username and password field is displayed or not in login page
u_displayed=username.is_displayed()#return True or False
p_displayed=password.is_displayed()#return True or False
print(u_displayed,p_displayed)

#checking username and password field is enabled or not in login page
u_enabled=username.is_enabled()#return True or False
p_enabled=password.is_enabled()#return True or False
print(u_enabled,u_displayed)

#testing local html for raiobutton and slection box testing

driver.get("file:///C:/Users/R%20Chandu/Desktop/selenium/test.html")
radio_male=driver.find_element(By.CSS_SELECTOR,"input[value=Male]")
m_status=radio_male.is_selected()#check radio button is selected or not ,,,it also have enabled,displayed functions
radio_female=driver.find_element(By.CSS_SELECTOR,"input[value=Female]")
f_status=radio_female.is_selected()#check radio button is selected or not ,,,it also have enabled,displayed functions
print(m_status,f_status)
time.sleep(20)

driver.close()