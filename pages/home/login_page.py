from pages.home.home_page import HomePage
import logging
from base.basepage import BasePage
import utilities.custom_logger as cl

class LoginPage(BasePage):

    log = cl.customLogger(logging.DEBUG)

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver
        self.home = HomePage(driver)

    # Locators
    _email_field = "email"
    _password_field = "pass"
    _sign_in_button = "send2"
    _welcome_msg_sign_in = "//div//li//span[contains(text(), 'Welcome, John Doe!')][1]"

    def enterEmail(self, email):
        self.sendKeys(email, self._email_field)

    def enterPassword(self, password):
        self.sendKeys(password, self._password_field)

    def clickSignIn(self):
        self.elementClick(self._sign_in_button)

    def SignIn(self, email="", password=""):
        self.home.navigateToSignIn()
        self.enterEmail(email)
        self.enterPassword(password)
        self.clickSignIn()

    def verifySignInSuccessful(self):
        self.waitForElement(self._welcome_msg_sign_in,
                                locatorType="xpath")
        result = self.isElementDisplayed(locator=self._welcome_msg_sign_in,
                                             locatorType="xpath")
        return result