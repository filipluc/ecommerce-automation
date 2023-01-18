import logging
from base.basepage import BasePage
import utilities.custom_logger as cl

class ItemPage(BasePage):

    log = cl.customLogger(logging.DEBUG)

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    # Locators
    _item_price = "//div[contains(@class, 'product-info-main')]//span[@class='price']"
    _item_first_size = "//div[contains(@class, 'swatch-option text')][1]"
    _item_first_color = "//div[contains(@class, 'swatch-option color')][1]"
    _item_quantity = "//input[@id='qty']"
    _add_to_cart_button = "//button[@id='product-addtocart-button']"
    _checkout_cart_link = "//span[contains(text(),'My Cart')]//parent::a[contains(@href,'/cart')]"
    _view_and_edit_cart_link = "//span[contains(text(), 'View and Edit Cart')]//parent::a[contains(@href, '/cart')]"
    _shopping_cart_link = "//a[contains(@href, '/cart') and contains(text(), 'shopping cart')]"
    _checkout_cart_url = "https://magento.softwaretestingboard.com/checkout/cart/"


    def getValueForAttributeClassForItem(self):
        result = self.getValueForAttribute("href", locator=self._first_item_in_list, locatorType="xpath")
        return result

    def getTextForItemPrice(self):
        result = self.getElementText(locator=self._item_price, locatorType="xpath")
        return result

    def getValueForAttributeOptionLabelForItemFirstSize(self):
        result = self.getValueForAttribute("option-label", locator=self._item_first_size, locatorType="xpath")
        return result

    def getValueForAttributeOptionLabelForItemFirstColor(self):
        result = self.getValueForAttribute("option-label", locator=self._item_first_color, locatorType="xpath")
        return result

    def getValueForAttributeValueForItemQty(self):
        result = self.getValueForAttribute("value", locator=self._item_quantity, locatorType="xpath")
        return result

    def clickItemFirstSize(self):
        self.elementClick(locator=self._item_first_size, locatorType="xpath")

    def clickItemFirstColor(self):
        self.elementClick(locator=self._item_first_color, locatorType="xpath")

    def clickAddToCartButton(self):
        self.elementClick(locator=self._add_to_cart_button, locatorType="xpath")

    def clickCheckoutCartLink(self):
        self.waitForElement(locator=self._checkout_cart_link, locatorType="xpath")
        self.elementClick(locator=self._checkout_cart_link, locatorType="xpath")

    def clickViewAndEditCartLink(self):
        self.waitForElement(locator=self._view_and_edit_cart_link, locatorType="xpath")
        self.elementClick(locator=self._view_and_edit_cart_link, locatorType="xpath")

    def clickShoppingCartLink(self):
        self.waitForElement(locator=self._shopping_cart_link, locatorType="xpath")
        self.elementClick(locator=self._shopping_cart_link, locatorType="xpath")

    def verifyCheckoutCartURL(self):
        result = self.compareURL(self._checkout_cart_url)
        return result
