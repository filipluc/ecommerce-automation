from pages.home.login_page import LoginPage
from pages.home.home_page import HomePage
from pages.women.tops_women import WomenTopsPage
from pages.items.item_page import ItemPage
from pages.items.shopping_cart_page import ShoppingCartPage
from pages.checkout.checkout_page import CheckoutPage
import unittest
import pytest
import utilities.custom_logger as cl
import logging
from utilities.util import Util
from utilities.read_config import ReadConfig
import time

@pytest.mark.usefixtures("oneTimeSetUp", "setUp")
class CheckoutTests(unittest.TestCase):
    log = cl.customLogger(logging.DEBUG)
    util = Util()
    random_email = util.getUniqueName() + "@yahoo.com"
    first_name = ReadConfig.getFirstName()
    last_name = ReadConfig.getLastName()
    checkout_address = ReadConfig.getAddress()
    checkout_city = ReadConfig.getCity()
    checkout_state = ReadConfig.getState()
    checkout_postcode = ReadConfig.getPostcode()
    checkout_telephone = ReadConfig.getTelephone()

    @pytest.fixture(autouse=True)
    def objectSetup(self, oneTimeSetUp):
        self.lp = LoginPage(self.driver)
        self.hp = HomePage(self.driver)
        self.wt = WomenTopsPage(self.driver)
        self.item = ItemPage(self.driver)
        self.shopping_cart = ShoppingCartPage(self.driver)
        self.checkout = CheckoutPage(self.driver)

    @pytest.mark.smoke
    def test_checkout(self):
        # self.lp.SignIn(self.login_username, self.login_password)
        self.hp.navigateToLinkWomenTopsJackets()
        self.wt.clickFirstItemInList()
        self.item.clickItemFirstSize()
        self.item.clickItemFirstColor()
        self.item.clickAddToCartButton()
        self.item.clickShoppingCartLink()
        self.shopping_cart.clickProceedToCheckout()

        self.checkout.enterEmail(self.random_email)
        self.checkout.enterFirstName(self.first_name)
        self.checkout.enterLastName(self.last_name)
        self.checkout.enterTextAddress(self.checkout_address)
        self.checkout.enterTextCity(self.checkout_city)
        self.checkout.selectState(self.checkout_state)
        self.checkout.enterTextPostcode(self.checkout_postcode)
        self.checkout.enterTextTelephone(self.checkout_telephone)
        self.checkout.clickShippingMethod()
        self.checkout.clickNextButton()
        result1 = self.checkout.verifyPaymentTitleDisplayed()
        assert result1 == True
        # check how can I replace sleep
        time.sleep(3)
        self.checkout.clickPlaceOrderButton()
        result2 = self.checkout.verifyOrderSuccessPageTitleDisplayed()
        assert result2 == True

