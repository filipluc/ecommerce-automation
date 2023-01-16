from pages.home.home_page import HomePage
from pages.women.women import WomenPage
import unittest
import pytest
import utilities.custom_logger as cl
import logging

@pytest.mark.usefixtures("oneTimeSetUp", "setUp")
class WomenLeftMenuTests(unittest.TestCase):
    log = cl.customLogger(logging.DEBUG)

    @pytest.fixture(autouse=True)
    def objectSetup(self, oneTimeSetUp):
        self.hp = HomePage(self.driver)
        self.wp = WomenPage(self.driver)

    @pytest.mark.women_page
    def test_WomenLeftMenuCategory(self):
        self.hp.navigateToLinkWomen()
        result1 = self.wp.verifyWomenCategoryTopsPresent()
        assert result1 == True
        result2 = self.wp.verifyWomenCategoryBottomsPresent()
        assert result2 == True

    @pytest.mark.women_page
    def test_WomenLeftMenuTops(self):
        self.hp.navigateToLinkWomen()
        result1 = self.wp.verifyWomenTopsHoodiesPresent()
        assert result1 == True
        result2 = self.wp.verifyWomenTopsJacketsPresent()
        assert result2 == True
