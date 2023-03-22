import unittest

#tearDownModule excutes the after excutes all class or all module...first tearDownModule will excute

class Test(unittest.TestCase):
    #setUpClass excutes the onnly one time before excuting the all methods 
    
    
    def test_get_report(self):
        print("im report")
    
    def test_profile(self):
        print('im profile')
    
    @unittest.SkipTest # it did not excute this function
    def test_info(self):
        print("im info")
    
    @unittest.skip("not implemented fully")#reason based skipping
    def test_login(self):
        print("login")
    
    @unittest.skipIf(2==2,'conditional')#conditional based skipping
    def test_reg(self):
        print('reg')

if __name__=="__main__":
    unittest.main()