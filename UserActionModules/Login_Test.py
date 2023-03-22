import unittest

class LoginTest(unittest.TestCase):
    def test_Login_By_Email(self):
        print("this is from Login By Email")
        self.assertTrue(True)
    def test_Login_By_Facebook(self):
        print("this is from Login By Facebook")
        self.assertTrue(True)
    def test_Login_By_Twitter(self):
        print("this is from Login By Twitter")
        self.assertTrue(True)

if __name__=="__main__":
    unittest.main()
    