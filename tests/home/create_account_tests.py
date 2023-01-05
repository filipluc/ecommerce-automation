from pages.home.create_account_page import CreateAccountPage
import unittest
import pytest
import utilities.custom_logger as cl
import logging
from utilities.util import Util
from utilities.read_config import ReadConfig

@pytest.mark.usefixtures("oneTimeSetUp", "setUp")
class CreateAccountTests(unittest.TestCase):
    log = cl.customLogger(logging.DEBUG)
    util = Util()
    random_user_name = util.getUniqueName() + "@yahoo.com"
    first_name = ReadConfig.getFirstName()
    last_name = ReadConfig.getLastName()
    password = ReadConfig.getLoginPassword()

    @pytest.fixture(autouse=True)
    def objectSetup(self, oneTimeSetUp):
        self.cap = CreateAccountPage(self.driver)

    @pytest.mark.smoke
    def test_validCreateAccount(self):
        self.cap.createAccount(self.first_name, self.last_name, self.random_user_name, self.password, self.password)
        result = self.cap.verifyAccountCreationSuccessful()
        assert result == True