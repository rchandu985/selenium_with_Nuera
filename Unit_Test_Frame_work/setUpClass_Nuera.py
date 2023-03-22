import unittest

class Test(unittest.TestCase):
    #setUpClass excutes the onnly one time before excuting the all methods 
    @classmethod
    def setUpClass(cls):#function name shoud be same and takes cls as parameeter
        print("im setUpClass")
    def test_get_report(self):
        print("im report")
    def test_profile(self):
        print('im profile')
if __name__=="__main__":
    unittest.main()