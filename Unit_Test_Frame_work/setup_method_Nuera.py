import unittest

class Test(unittest.TestCase):
    #setup method used to preload data..it will excute the before excuting the every function
    @classmethod
    def setUp(self):#function name shoud be same
        print("im setup")
    def test_get_report(self):
        print("im report")
    def test_profile(self):
        print('im profile')
if __name__=="__main__":
    unittest.main()