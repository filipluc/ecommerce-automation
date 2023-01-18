from pages.home.home_page import HomePage
from pages.women.tops_women import WomenTopsPage
from pages.items.item_page import ItemPage
from pages.items.shopping_cart_page import ShoppingCartPage
import unittest
import pytest
import utilities.custom_logger as cl
import logging
import time


@pytest.mark.usefixtures("oneTimeSetUp", "setUp")
class TopsWomenLeftMenuTests(unittest.TestCase):
    log = cl.customLogger(logging.DEBUG)

    @pytest.fixture(autouse=True)
    def objectSetup(self, oneTimeSetUp):
        self.hp = HomePage(self.driver)
        self.wt = WomenTopsPage(self.driver)
        self.item = ItemPage(self.driver)
        self.shopping_cart = ShoppingCartPage(self.driver)

    @pytest.mark.items_page
    def test_AddItemToCart(self):
        self.hp.navigateToLinkWomenTopsJackets()
        item_link_1 = self.wt.getValueForAttributeClassForItem()
        self.wt.clickFirstItemInList()
        item_link_2 = self.hp.getURL()

        # assert if the item link is correct
        assert item_link_1 == item_link_2

        # get the item price from the item page
        item_price_1 = self.item.getTextForItemPrice()

        # get the item first size from the list and select it
        item_size_1 = self.item.getValueForAttributeOptionLabelForItemFirstSize()
        self.item.clickItemFirstSize()

        # get the item first color from the list and select it
        item_color_1 = self.item.getValueForAttributeOptionLabelForItemFirstColor()
        self.item.clickItemFirstColor()

        # get the item quantity
        item_qty_1 = self.item.getValueForAttributeValueForItemQty()

        # click Add to Cart
        self.item.clickAddToCartButton()

        # click Shopping Cart link and verify URL
        self.item.clickShoppingCartLink()
        self.item.verifyCheckoutCartURL()

        # get the item price and compare
        item_price_2 = self.shopping_cart.getTextForItemPrice()
        assert item_price_1 == item_price_2

        # get the item size and compare
        item_size_2 = self.shopping_cart.getTextForItemSize()
        assert item_size_1 == item_size_2

        # get the item color and compare
        item_color_2 = self.shopping_cart.getTextForItemColor()
        assert item_color_1 == item_color_2

        # get the item quantity and compare
        item_qty_2 = self.shopping_cart.getValueForAttributeValueForItemQty()
        assert item_qty_1 == item_qty_2


