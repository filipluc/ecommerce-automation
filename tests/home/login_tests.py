from pages.home.login_page import LoginPage
import unittest
import pytest
import utilities.custom_logger as cl
import logging

@pytest.mark.usefixtures("oneTimeSetUp", "setUp")
class LoginTests(unittest.TestCase):
    log = cl.customLogger(logging.DEBUG)

    @pytest.fixture(autouse=True)
    def objectSetup(self, oneTimeSetUp):
        self.lp = LoginPage(self.driver)

    @pytest.mark.smoke
    def test_validSignIn(self):
        self.lp.SignIn("fl_magento@yahoo.com", "Magento_999")
        result = self.lp.verifySignInSuccessful()
        assert result == True