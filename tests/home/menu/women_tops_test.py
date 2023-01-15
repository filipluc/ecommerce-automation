from pages.home.home_page import HomePage
import unittest
import pytest
import utilities.custom_logger as cl
import logging

@pytest.mark.usefixtures("oneTimeSetUp", "setUp")
class WomenTopsTests(unittest.TestCase):
    log = cl.customLogger(logging.DEBUG)

    @pytest.fixture(autouse=True)
    def objectSetup(self, oneTimeSetUp):
        self.hp = HomePage(self.driver)

    @pytest.mark.menu
    def test_womenTops(self):
        self.hp.navigateToLinkWomenTops()
        result = self.hp.verifyWomenTopsURL()
        assert result == True
