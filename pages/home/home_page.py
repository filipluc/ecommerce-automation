import utilities.custom_logger as cl
import logging
from base.basepage import BasePage


class HomePage(BasePage):

    log = cl.customLogger(logging.DEBUG)

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    # Locators
    _create_an_account = "(//div//li//a[text()='Create an Account'])[1]"
    _sign_in = "(//div//li//a[contains(text(), 'Sign In')])[1]"
    _default_welcome_msg = "//div//li//span[contains(text(), 'Default welcome msg!')]"
    _link_what_is_new = "https://magento.softwaretestingboard.com/what-is-new.html"
    _link_women = "https://magento.softwaretestingboard.com/women.html"
    _link_women_tops = "https://magento.softwaretestingboard.com/tops-women.html"


    def navigateToCreateAccount(self):
        self.elementClick(locator=self._create_an_account, locatorType="xpath")

    def navigateToSignIn(self):
        self.elementClick(locator=self._sign_in, locatorType="xpath")

    def isDisplayedSignIn(self):
        self.isElementDisplayed(locator=self._sign_in, locatorType="xpath")

    def navigateToLinkWhatIsNew(self):
        self.elementClick(locator=self._link_what_is_new, locatorType="link")

    def navigateToLinkWomen(self):
        self.elementClick(locator=self._link_women, locatorType="link")

    def navigateToLinkWomenTops(self):
        self.elementClick(locator=self._link_women_tops, locatorType="link")

    def verifyWelcomeMsg(self):
        self.waitForElement(self._default_welcome_msg,
                                locatorType="xpath")
        result = self.isElementDisplayed(locator=self._default_welcome_msg,
                                             locatorType="xpath")
        return result

    def verifySignInDisplayed(self):
        self.waitForElement(self._sign_in,
                                locatorType="xpath")
        result = self.isElementDisplayed(locator=self._sign_in,
                                             locatorType="xpath")
        return result