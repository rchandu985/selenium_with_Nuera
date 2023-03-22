import unittest

class Payments(unittest.TestCase):
    def test_payment_in_dollar(self):
        print("this is from Payments in Dollar")
        self.assertTrue(True)
    def test_payements_in_rupees(self):
        print("this is from payement in Rupees")
        self.assertTrue(True)
    

if __name__=="__main__":
    unittest.main()
    