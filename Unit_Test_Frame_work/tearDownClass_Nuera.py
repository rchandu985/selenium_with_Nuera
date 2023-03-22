import unittest

class Test(unittest.TestCase):
    #setUpClass excutes the only one time after excuting the all methods 
    @classmethod
    def tearDownClass(cls):#function name shoud be same and takes cls as parameeter
        print("im tearDownClass")
    def test_get_report(self):
        print("im report")
    def test_profile(self):
        print('im profile')
if __name__=="__main__":
    unittest.main()