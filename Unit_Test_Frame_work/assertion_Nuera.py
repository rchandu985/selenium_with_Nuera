import unittest
from selenium import webdriver

class Test(unittest.TestCase):
    
    def test_title_match(self):
        driver=webdriver.Chrome("chrome")
        driver.get("https://www.google.com/")
        self.title=driver.title
        self.assertEqual("Google",self.title,"title name not matched")
    
    def test_title_mismatch(self):
        driver=webdriver.Chrome("chrome")
        driver.get("https://www.google.com/")
        self.title=driver.title
        self.assertEqual("Googl",self.title,"title name not matched")
    def test_ass_ne(self):
        driver=webdriver.Chrome("chrome")
        driver.get("https://www.google.com/")
        self.title=driver.title
        self.assertNotEqual("Googl",self.title,"title name not matched")
        #self.assertTrue(self.title=="Google")
        #self.assertFalse(self.title=="Google")
    def test_ass_none(self):
        driver=webdriver.Chrome("chrome")
        driver.get("https://www.google.com/")
        #self.assertIsNone(driver)
        self.assertIsNotNone(driver)
    def test_in(self):
        x=[1,2,3,4]
        #self.assertIsNone(driver)
        self.assertIn(1,x)
        self.assertNotIn(10,x)
    def test_relation(self):
        self.a=100
        self.b=10
        '''self.assertGreaterEqual(self.a,self.b)#100>=10
        self.assertGreater(self.a,self.b)#100>10
        self.assertLessEqual(self.b,self.a)#10<=100
        self.assertLess(self.b,self.a)#10<100'''
        
if __name__=="__main__":
    unittest.main()