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
    _wait_for_icon_to_hover = "//a[contains(@href, 'https://magento.softwaretestingboard.com/women.html')]//span[contains(@class, 'ui-menu-icon')]"
    _link_what_is_new = "//a[contains(@href, 'https://magento.softwaretestingboard.com/what-is-new.html')]"
    _link_women = "//a[contains(@href, 'https://magento.softwaretestingboard.com/women.html')]"
    _link_women_tops = "//a[contains(@href, 'https://magento.softwaretestingboard.com/women/tops-women.html')]"
    _link_women_tops_jackets = "//a[contains(@href, 'https://magento.softwaretestingboard.com/women/tops-women/jackets-women.html')]"
    _link_women_tops_tees = "//a[contains(@href, 'https://magento.softwaretestingboard.com/women/tops-women/tees-women.html')]"
    _link_women_bottoms = "//a[contains(@href, 'https://magento.softwaretestingboard.com/women/bottoms-women.html')]"
    _link_women_bottoms_pants = "//a[contains(@href, 'https://magento.softwaretestingboard.com/women/bottoms-women/pants-women.html')]"

    _link_women_tops_url = "https://magento.softwaretestingboard.com/women/tops-women.html"
    _link_women_tops_jackets_url = "https://magento.softwaretestingboard.com/women/tops-women/jackets-women.html"
    _link_women_bottoms_url = "https://magento.softwaretestingboard.com/women/bottoms-women.html"
    _link_women_bottoms_pants_url = "https://magento.softwaretestingboard.com/women/bottoms-women/pants-women.html"


    def navigateToCreateAccount(self):
        self.elementClick(locator=self._create_an_account, locatorType="xpath")

    def navigateToSignIn(self):
        self.elementClick(locator=self._sign_in, locatorType="xpath")

    def isDisplayedSignIn(self):
        self.isElementDisplayed(locator=self._sign_in, locatorType="xpath")

    def navigateToLinkWhatIsNew(self):
        self.elementClick(locator=self._link_what_is_new, locatorType="xpath")

    def navigateToLinkWomen(self):
        self.elementClick(locator=self._link_women, locatorType="xpath")

    def navigateToLinkWomenTops(self):
        self.hoverOverLinkWomen()
        self.elementClick(locator=self._link_women_tops, locatorType="xpath")

    def navigateToLinkWomenTopsJackets(self):
        self.hoverOverLinkWomenTops()
        self.elementClick(locator=self._link_women_tops_jackets, locatorType="xpath")

    def navigateToLinkWomenTopsTees(self):
        self.hoverOverLinkWomenTops()
        self.elementClick(locator=self._link_women_tops_tees, locatorType="xpath")

    def navigateToLinkWomenBottoms(self):
        self.hoverOverLinkWomen()
        self.elementClick(locator=self._link_women_bottoms, locatorType="xpath")

    def navigateToLinkWomenBottomsPants(self):
        self.hoverOverLinkWomenBottoms()
        self.elementClick(locator=self._link_women_bottoms_pants, locatorType="xpath")

    def hoverOverLinkWomen(self):
        self.waitForElement(self._wait_for_icon_to_hover, locatorType="xpath")
        self.elementHover(locator=self._link_women, locatorType="xpath")

    def hoverOverLinkWomenTops(self):
        self.hoverOverLinkWomen()
        self.elementHover(locator=self._link_women_tops, locatorType="xpath")

    def hoverOverLinkWomenBottoms(self):
        self.hoverOverLinkWomen()
        self.elementHover(locator=self._link_women_bottoms, locatorType="xpath")

    def verifyWelcomeMsg(self):
        self.waitForElement(self._default_welcome_msg, locatorType="xpath")
        result = self.isElementDisplayed(locator=self._default_welcome_msg, locatorType="xpath")
        return result

    def verifySignInDisplayed(self):
        self.waitForElement(self._sign_in, locatorType="xpath")
        result = self.isElementDisplayed(locator=self._sign_in, locatorType="xpath")
        return result

    def verifyWomenTopsURL(self):
        result = self.compareURL(self._link_women_tops_url)
        return result

    def verifyWomenTopsJacketsURL(self):
        result = self.compareURL(self._link_women_tops_jackets_url)
        return result

    def verifyWomenBottomsURL(self):
        result = self.compareURL(self._link_women_bottoms_url)
        return result

    def verifyWomenBottomsPantsURL(self):
        result = self.compareURL(self._link_women_bottoms_pants_url)
        return result