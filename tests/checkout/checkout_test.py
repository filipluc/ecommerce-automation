from pages.home.login_page import LoginPage
from pages.home.home_page import HomePage
from pages.women.tops_women import WomenTopsPage
from pages.items.item_page import ItemPage
from pages.items.shopping_cart_page import ShoppingCartPage
import unittest
import pytest
import utilities.custom_logger as cl
import logging
from utilities.read_config import ReadConfig

@pytest.mark.usefixtures("oneTimeSetUp", "setUp")
class CheckoutTests(unittest.TestCase):
    log = cl.customLogger(logging.DEBUG)
    login_username = ReadConfig.getLoginUsername()
    login_password = ReadConfig.getLoginPassword()

    @pytest.fixture(autouse=True)
    def objectSetup(self, oneTimeSetUp):
        self.lp = LoginPage(self.driver)
        self.hp = HomePage(self.driver)
        self.wt = WomenTopsPage(self.driver)
        self.item = ItemPage(self.driver)
        self.shopping_cart = ShoppingCartPage(self.driver)

    @pytest.mark.smoke
    def test_validSignIn(self):
        self.lp.SignIn(self.login_username, self.login_password)
        self.hp.navigateToLinkWomenTopsJackets()
        self.wt.clickFirstItemInList()
        self.item.clickItemFirstSize()
        self.item.clickItemFirstColor()
        self.item.clickAddToCartButton()
        self.shopping_cart.clickProceedToCheckout()
