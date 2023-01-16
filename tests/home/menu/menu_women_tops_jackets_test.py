from pages.home.home_page import HomePage
import unittest
import pytest
import utilities.custom_logger as cl
import logging

@pytest.mark.usefixtures("oneTimeSetUp", "setUp")
class WomenTopsJacketsTests(unittest.TestCase):
    log = cl.customLogger(logging.DEBUG)

    @pytest.fixture(autouse=True)
    def objectSetup(self, oneTimeSetUp):
        self.hp = HomePage(self.driver)

    @pytest.mark.menu
    def test_womenTopsJackets(self):
        self.hp.navigateToLinkWomenTopsJackets()
        result = self.hp.verifyWomenTopsJacketsURL()
        assert result == True
