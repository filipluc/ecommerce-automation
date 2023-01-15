from pages.home.login_page import LoginPage
import unittest
import pytest
import utilities.custom_logger as cl
import logging
from utilities.read_config import ReadConfig

@pytest.mark.usefixtures("oneTimeSetUp", "setUp")
class LoginTests(unittest.TestCase):
    log = cl.customLogger(logging.DEBUG)
    login_username = ReadConfig.getLoginUsername()
    login_password = ReadConfig.getLoginPassword()

    @pytest.fixture(autouse=True)
    def objectSetup(self, oneTimeSetUp):
        self.lp = LoginPage(self.driver)

    @pytest.mark.smoke
    def test_validSignIn(self):
        self.lp.SignIn(self.login_username, self.login_password)
        result = self.lp.verifySignInSuccessful()
        assert result == True