from pages.home.home_page import HomePage
import logging
from base.basepage import BasePage
import utilities.custom_logger as cl

class WomenTopsPage(BasePage):

    log = cl.customLogger(logging.DEBUG)

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver
        self.home = HomePage(driver)

    # Locators
    _tops_women_category_link = "//div[text()='Category' and contains(@aria-expanded, 'false')]"
    _tops_women_category_jackets = "//div//li//a[contains(text(), 'Jackets') and contains(@href, 'https://magento.softwaretestingboard.com/women/tops-women.html')]"
    _tops_women_category_filter_label = "//li//span[@class='filter-label' and contains(text(), 'Category')]"
    _tops_women_category_filter_value_jackets = "//li//span[@class='filter-value' and contains(text(), 'Jackets')]"
    _tops_women_filter_clear_all = "//span[contains(text(), 'Clear All')]//parent::a[contains(@href, 'https://magento.softwaretestingboard.com/women/tops-women.html')]"
    _first_item_in_list = "//div//ol//li[@class='item product product-item'][1]//a[contains(@class, 'product-item-link')]"


    def navigateToTopsWomenCategoryLink(self):
        self.elementClick(locator=self._tops_women_category_link, locatorType="xpath")

    def navigateToTopsWomenCategoryJackets(self):
        self.elementClick(locator=self._tops_women_category_jackets, locatorType="xpath")

    def verifyTopsWomenCategoryJacketDisplay(self):
        result = self.isElementDisplayed(locator=self._tops_women_category_jackets, locatorType="xpath")
        return result

    def verifyTopsWomenCategoryFilterLabelDisplay(self):
        result = self.isElementDisplayed(locator=self._tops_women_category_filter_label, locatorType="xpath")
        return result

    def verifyTopsWomenCategoryFilterValueJacketsDisplay(self):
        result = self.isElementDisplayed(locator=self._tops_women_category_filter_value_jackets, locatorType="xpath")
        return result

    def verifyTopsWomenFilterClearAllDisplay(self):
        result = self.isElementDisplayed(locator=self._tops_women_filter_clear_all, locatorType="xpath")
        return result

    def clickTopsWomenFilterClearAll(self):
        self.elementClick(locator=self._tops_women_filter_clear_all, locatorType="xpath")

    def clickFirstItemInList(self):
        self.elementClick(locator=self._first_item_in_list, locatorType="xpath")

    def getValueForAttributeClassForItem(self):
        result = self.getValueForAttribute("href", locator=self._first_item_in_list, locatorType="xpath")
        return result