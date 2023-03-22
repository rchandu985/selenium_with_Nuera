import unittest

class SignupTest(unittest.TestCase):
    def test_SignUp_By_Email(self):
        print("this is from SignUp By Email")
        self.assertTrue(True)
    def test_SignUp_By_Facebook(self):
        print("this is from SignUp By Facebook")
        self.assertTrue(True)
    def test_SignUp_By_Twitter(self):
        print("this is from SignUp By Twitter")
        self.assertTrue(True)

if __name__=="__main__":
    unittest.main()
    