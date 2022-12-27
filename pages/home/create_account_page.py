from pages.home.home_page import HomePage
import logging
from base.basepage import BasePage
import utilities.custom_logger as cl

class CreateAccountPage(BasePage):

    log = cl.customLogger(logging.DEBUG)

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver
        self.home = HomePage(driver)

    # Locators
    _firstname_field = "firstname"
    _lastname_field = "lastname"
    _email_field = "email_address"
    _password_field = "password"
    _confirm_password_field = "password-confirmation"
    _create_account_button = "//div//button//span[text()='Create an Account']"
    _account_creation_successful = "//div[contains(text(), 'Thank you for registering')]"

    def enterFirstName(self, firstname):
        self.sendKeys(firstname, self._firstname_field)

    def enterLastName(self, lastname):
        self.sendKeys(lastname, self._lastname_field)

    def enterEmail(self, email):
        self.sendKeys(email, self._email_field)

    def enterPassword(self, password):
        self.sendKeys(password, self._password_field)

    def enterPasswordConfirmation(self, password_confirmation):
        self.sendKeys(password_confirmation, self._confirm_password_field)

    def clickCreateAccount(self):
        self.elementClick(self._create_account_button, locatorType="xpath")

    def createAccount(self, firstname="", lastname="", email="", password="", password_confirmation=""):
        self.home.navigateToCreateAccount()
        self.enterFirstName(firstname)
        self.enterLastName(lastname)
        self.enterEmail(email)
        self.enterPassword(password)
        self.enterPasswordConfirmation(password_confirmation)
        self.clickCreateAccount()

    def verifyAccountCreationSuccessful(self):
        self.waitForElement(self._account_creation_successful,
                                locatorType="xpath")
        result = self.isElementDisplayed(locator=self._account_creation_successful,
                                             locatorType="xpath")
        return result