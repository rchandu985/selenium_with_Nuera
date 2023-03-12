from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver import Keys, ActionChains
import time


driver=webdriver.Chrome("chromedriver")
driver.implicitly_wait(10)
driver.maximize_window()

driver.get("https://www.expedia.com/")


#explicity_wait performs particular element ..it wait for some time to get specified element

driver.find_element(By.XPATH,"//span[normalize-space()='Flights']").click()


driver.find_element(By.XPATH,"//button[@aria-label='Leaving from']").send_keys("Hyderabad (HYD - Rajiv Gandhi Intl.)")
driver.find_element(By.XPATH,"//button[@aria-label='Going to']").send_keys("Going to Goa (GOI - Dabolim)")

driver.find_element(By.XPATH,"//button[@type='submit']").click()
time.sleep(60)
