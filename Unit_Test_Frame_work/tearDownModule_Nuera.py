import unittest

#tearDownModule excutes the after excutes all class or all module...first tearDownModule will excute

def tearDownModule():
    print("tearDown module")

class Test(unittest.TestCase):
    #setUpClass excutes the onnly one time before excuting the all methods 
    
    def test_get_report(self):
        print("im report")
    def test_profile(self):
        print('im profile')
if __name__=="__main__":
    unittest.main()