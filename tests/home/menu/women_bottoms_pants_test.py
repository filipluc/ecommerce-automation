from pages.home.home_page import HomePage
import unittest
import pytest
import utilities.custom_logger as cl
import logging

@pytest.mark.usefixtures("oneTimeSetUp", "setUp")
class WomenBottomsPantsTests(unittest.TestCase):
    log = cl.customLogger(logging.DEBUG)

    @pytest.fixture(autouse=True)
    def objectSetup(self, oneTimeSetUp):
        self.hp = HomePage(self.driver)

    def test_womenBottomsPants(self):
        self.hp.navigateToLinkWomenBottomsPants()
        result = self.hp.verifyWomenBottomsPantsURL()
        assert result == True
