from selenium import webdriver

from selenium.webdriver.common.by import By
from selenium.webdriver import ActionChains
import time


driver=webdriver.Chrome("chromedriver")
#find how text input box in webpage

#enable for mouse hover
#driver.get("https://www.orangehrm.com/")
#driver.maximize_window()

#mouse hover
#double click
#right click
#drag and drop

#mouse hover
'''parent=driver.find_element(By.XPATH,"//*[@id='navbarSupportedContent']/ul/li[2]/a")
child=driver.find_element(By.XPATH,"//*[@id='navbarSupportedContent']/ul/li[2]/div/div/div/div/ul/li[1]")
final=driver.find_element(By.XPATH,"//*[@id='navbarSupportedContent']/ul/li[2]/div/div/div/div/ul/li[1]/div/div/h6[1]/a")
actions=ActionChains(driver)
actions.move_to_element(parent).move_to_element(child).move_to_element(final).click().perform()
'''

#double click
'''driver.get("file:///C:/Users/R%20Chandu/selenium_with_Nuera/test.html")
button=driver.find_element("name","dbc")
actions=ActionChains(driver)
actions.double_click(button).perform()'''

#right click

'''driver.get("https://demo.guru99.com/test/simple_context_menu.html")
button=driver.find_element(By.XPATH,"//*[@id='authentication']/span")
actions=ActionChains(driver)
actions.context_click(button).perform()'''

#drag and drop
#currently not working
'''
driver.get("http://www.dhtmlgoodies.com/scripts/drag-drop-custom/demo-drag-drop-3.html")

source=driver.find_element(By.XPATH,"//*[@id='DHTMLgoodies_dragableElement5']")
dest=driver.find_element(By.XPATH,"//*[@id='box106']")
actions=ActionChains(driver)
actions.drag_and_drop(source,dest).perform()'''
time.sleep(10)