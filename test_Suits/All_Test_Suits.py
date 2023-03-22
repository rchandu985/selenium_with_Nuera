import unittest
from UserActionModules.Login_Test import LoginTest
from UserActionModules.SignUp import SignupTest
from FunctionalTestModules.payments import Payments
from FunctionalTestModules.payments_Reception import Payments_Recieved_Bank

#loading all tests
t1=unittest.TestLoader().loadTestsFromTestCase(LoginTest)
t2=unittest.TestLoader().loadTestsFromTestCase(SignupTest)
t3=unittest.TestLoader().loadTestsFromTestCase(Payments_Recieved_Bank)
t4=unittest.TestLoader().loadTestsFromTestCase(Payments)

#excute Test

sanity_Test=unittest.TestSuite([t1,t2])#this test suit contains all test cases

#run test case
#unittest.TextTestRunner().run(sanity_Test)
functional_test_suite=unittest.TestSuite([t3,t4])
#unittest.TextTestRunner().run(functional_test_suite)

master_test=unittest.TestSuite([t1,t2,t3,t4])#it contains all test methods
unittest.TextTestRunner(verbosity=2).run(master_test)