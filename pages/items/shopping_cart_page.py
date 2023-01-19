import logging
from base.basepage import BasePage
import utilities.custom_logger as cl

class ShoppingCartPage(BasePage):

    log = cl.customLogger(logging.DEBUG)

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    # Locators
    _item_price = "//td[@data-th='Price']//span[@class='price']"
    _item_quantity = "//input[contains(@id, 'qty') and contains(@title, 'Qty')]"
    _item_size = "//dl[@class='item-options']//dd[1]"
    _item_color = "//dl[@class='item-options']//dd[2]"
    _item_subtotal = "//td[@data-th='Subtotal']//span[@class='price']"

    def getTextForItemPrice(self):
        result = self.getElementText(locator=self._item_price, locatorType="xpath")
        return result

    def getValueForAttributeValueForItemQty(self):
        result = self.getValueForAttribute("value", locator=self._item_quantity, locatorType="xpath")
        return result

    def getTextForItemSize(self):
        result = self.getElementText(locator=self._item_size, locatorType="xpath")
        return result

    def getTextForItemColor(self):
        result = self.getElementText(locator=self._item_color, locatorType="xpath")
        return result

    def getTextForItemSubtotal(self):
        result = self.getElementText(locator=self._item_subtotal, locatorType="xpath")
        return result

