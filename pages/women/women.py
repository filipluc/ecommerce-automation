from pages.home.home_page import HomePage
import logging
from base.basepage import BasePage
import utilities.custom_logger as cl

class WomenPage(BasePage):

    log = cl.customLogger(logging.DEBUG)

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver
        self.home = HomePage(driver)

    # Locators
    _women_shop_by = "//div/strong[text() = 'Shop By']"
    _women_category_tops = "//dt[text() = 'Category']//parent::dl//dd//li/a[(text()='Tops') and contains(@href, 'https://magento.softwaretestingboard.com/women/tops-women.html')]"
    _women_category_bottoms = "//dt[text() = 'Category']//parent::dl//dd//li/a[(text()='Bottoms') and contains(@href, 'https://magento.softwaretestingboard.com/women/bottoms-women.html')]"
    _women_tops_hoodies = "//span[text()='Tops']//parent::strong//following-sibling::ul//li//a[(text()='Hoodies & Sweatshirts') and contains(@href, 'https://magento.softwaretestingboard.com/women/tops-women/hoodies-and-sweatshirts-women.html')]"
    _women_tops_jackets = "//span[text()='Tops']//parent::strong//following-sibling::ul//li//a[(text()='Jackets') and contains(@href, 'https://magento.softwaretestingboard.com/women/tops-women/jackets-women.html')]"

    def verifyWomenCategoryTopsPresent(self):
        self.waitForElement(self._women_category_tops, locatorType="xpath")
        result = self.isElementPresent(locator=self._women_category_tops, locatorType="xpath")
        return result

    def verifyWomenCategoryBottomsPresent(self):
        self.waitForElement(self._women_category_bottoms, locatorType="xpath")
        result = self.isElementPresent(locator=self._women_category_bottoms, locatorType="xpath")
        return result

    def verifyWomenTopsHoodiesPresent(self):
        self.waitForElement(self._women_tops_hoodies, locatorType="xpath")
        result = self.isElementPresent(locator=self._women_tops_hoodies, locatorType="xpath")
        return result

    def verifyWomenTopsJacketsPresent(self):
        self.waitForElement(self._women_tops_jackets, locatorType="xpath")
        result = self.isElementPresent(locator=self._women_tops_jackets, locatorType="xpath")
        return result