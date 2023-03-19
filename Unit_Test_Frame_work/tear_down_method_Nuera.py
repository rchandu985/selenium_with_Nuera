import unittest

class Test(unittest.TestCase):
    #setup method used to after completes the task data..it will excute the after excuting the every function
    @classmethod
    def tearDown(self):#function name shoud be same
        print("im setup")
    def test_get_report(self):
        print("im report")
    def test_profile(self):
        print('im profile')
if __name__=="__main__":
    unittest.main()