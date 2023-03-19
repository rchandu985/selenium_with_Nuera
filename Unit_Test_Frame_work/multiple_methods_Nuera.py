import unittest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
import asyncio

class Test(unittest.TestCase):
    def test_amazon(self):
        
            self.driver=webdriver.Chrome(service=Service(ChromeDriverManager().install()))
            self.driver.get("https://www.amazon.in/")
            print(self.driver.title,'\n')
            self.driver.close()
        
    def test_google(self):
        self.driver=webdriver.Chrome(service=Service(ChromeDriverManager().install()))
        self.driver.get("https://onedrive.live.com/?id=C634A76FCF010194%212801&cid=C634A76FCF010194")
        print(self.driver.title,'\n')
        self.driver.close()
if __name__=="__main__":
    try:
        unittest.main()
    except ResourceWarning:
        pass