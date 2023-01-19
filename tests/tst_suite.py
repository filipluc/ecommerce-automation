import unittest
from tests.home.create_account_test import CreateAccountTests
from tests.home.login_test import LoginTests


# Get all tests from the test classes
tc1 = unittest.TestLoader().loadTestsFromTestCase(CreateAccountTests)
tc2 = unittest.TestLoader().loadTestsFromTestCase(LoginTests)


# Create a test suite combining all test classes
smokeTest = unittest.TestSuite([tc2])

unittest.TextTestRunner(verbosity=2).run(smokeTest)