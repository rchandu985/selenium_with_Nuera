import unittest

#setUpModule excutes the before excutes any class or any module...first setUpModule will excute

def setUpModule():
    print("setup module")

class Test(unittest.TestCase):
    #setUpClass excutes the onnly one time before excuting the all methods 
    
    def test_get_report(self):
        print("im report")
    def test_profile(self):
        print('im profile')
if __name__=="__main__":
    unittest.main()