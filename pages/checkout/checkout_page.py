import logging
from base.basepage import BasePage
import utilities.custom_logger as cl

class CheckoutPage(BasePage):

    log = cl.customLogger(logging.DEBUG)

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    # Locators
    _input_email = "//form//div//input[contains(@type, 'email') and contains(@id, 'customer-email')]"
    _input_first_name = "//input[contains(@name, 'firstname')]"
    _input_last_name = "//input[contains(@name, 'lastname')]"
    _input_street_address = "//input[contains(@name, 'street[0]')]"
    _input_city = "//input[contains(@name, 'city')]"
    _select_state = "//select[contains(@name, 'region_id')]"
    _input_postcode = "//input[contains(@name, 'postcode')]"
    _input_telephone = "//input[contains(@name, 'telephone')]"
    _input_ship_method = "//input[contains(@type, 'radio')][1]"
    _button_next = "//span[contains(text(),'Next')]//parent::button[contains(@type, 'submit')]"
    _checkout_payment_url = "https://magento.softwaretestingboard.com/checkout/#payment"
    _payment_page_text_title = "//div[contains(text(), 'Payment Method')]"
    _button_place_order = "//span[contains(text(),'Place Order')]//parent::button[@type='submit']"
    _order_success_page_title = "//span[contains(text(),'Thank you for your purchase!')]//parent::h1"


    def enterEmail(self, email):
        self.waitForElement(locator=self._input_email, locatorType="xpath")
        self.clearField(locator=self._input_email, locatorType="xpath")
        result = self.sendKeys(email, locator=self._input_email, locatorType="xpath")
        return result

    def enterFirstName(self, firstname):
        self.waitForElement(locator=self._input_first_name, locatorType="xpath")
        self.clearField(locator=self._input_first_name, locatorType="xpath")
        result = self.sendKeys(firstname, locator=self._input_first_name, locatorType="xpath")
        return result

    def enterLastName(self, lastname):
        self.waitForElement(locator=self._input_last_name, locatorType="xpath")
        self.clearField(locator=self._input_last_name, locatorType="xpath")
        result = self.sendKeys(lastname, locator=self._input_last_name, locatorType="xpath")
        return result

    def enterTextAddress(self, data):
        self.waitForElement(locator=self._input_street_address, locatorType="xpath")
        self.clearField(locator=self._input_street_address, locatorType="xpath")
        result = self.sendKeys(data, locator=self._input_street_address, locatorType="xpath")
        return result

    def enterTextCity(self, data):
        self.waitForElement(locator=self._input_city, locatorType="xpath")
        self.clearField(locator=self._input_city, locatorType="xpath")
        result = self.sendKeys(data, locator=self._input_city, locatorType="xpath")
        return result

    def selectState(self, data):
        self.waitForElement(locator=self._select_state, locatorType="xpath")
        self.elementClick(locator=self._select_state, locatorType="xpath")
        self.sendKeys(data, locator=self._select_state, locatorType="xpath")
        result = self.sendKeys("key_Enter", locator=self._select_state, locatorType="xpath")
        return result

    def enterTextPostcode(self, data):
        self.waitForElement(locator=self._input_postcode, locatorType="xpath")
        self.clearField(locator=self._input_postcode, locatorType="xpath")
        result = self.sendKeys(data, locator=self._input_postcode, locatorType="xpath")
        return result

    def enterTextTelephone(self, data):
        self.waitForElement(locator=self._input_telephone, locatorType="xpath")
        self.clearField(locator=self._input_telephone, locatorType="xpath")
        result = self.sendKeys(data, locator=self._input_telephone, locatorType="xpath")
        return result

    def clickShippingMethod(self):
        self.elementClick(self._input_ship_method, locatorType="xpath")

    def clickNextButton(self):
        self.elementClick(self._button_next, locatorType="xpath")

    def verifyPaymentTitleDisplayed(self):
        self.waitForElement(self._payment_page_text_title, locatorType="xpath")
        result = self.isElementDisplayed(locator=self._payment_page_text_title, locatorType="xpath")
        return result

    def clickPlaceOrderButton(self):
        self.waitForElement(self._button_place_order, locatorType="xpath")
        self.elementClick(self._button_place_order, locatorType="xpath")

    def verifyOrderSuccessPageTitleDisplayed(self):
        self.waitForElement(self._order_success_page_title, locatorType="xpath")
        result = self.isElementDisplayed(locator=self._order_success_page_title, locatorType="xpath")
        return result