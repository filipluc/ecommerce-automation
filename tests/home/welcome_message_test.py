from pages.home.home_page import HomePage
import unittest
import pytest
import utilities.custom_logger as cl
import logging

@pytest.mark.usefixtures("oneTimeSetUp", "setUp")
class WelcomeMessageTests(unittest.TestCase):
    log = cl.customLogger(logging.DEBUG)

    @pytest.fixture(autouse=True)
    def objectSetup(self, oneTimeSetUp):
        self.hp = HomePage(self.driver)

    def test_welcomeMsg(self):
        # verify first if Sign in is displayed (welcome message is displayed only when you are NOT signed in)
        result_signIn = self.hp.verifySignInDisplayed()
        assert result_signIn == True
        result_welcomeMsg = self.hp.verifyWelcomeMsg()
        assert result_welcomeMsg == True
