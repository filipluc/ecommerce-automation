from pages.home.create_account_page import CreateAccountPage
import unittest
import pytest
import utilities.custom_logger as cl
import logging
from utilities.util import Util

@pytest.mark.usefixtures("oneTimeSetUp", "setUp")
class CreateAccountTests(unittest.TestCase):
    log = cl.customLogger(logging.DEBUG)
    util = Util()
    random_user_name = util.getUniqueName() + "@yahoo.com"

    @pytest.fixture(autouse=True)
    def objectSetup(self, oneTimeSetUp):
        self.cap = CreateAccountPage(self.driver)

    @pytest.mark.smoke
    def test_validCreateAccount(self):
        self.cap.createAccount("f1", "l1", self.random_user_name, "Magento_999", "Magento_999")
        result = self.cap.verifyAccountCreationSuccessful()
        assert result == True