from pages.home.home_page import HomePage
from pages.women.tops_women import WomenTopsPage
import unittest
import pytest
import utilities.custom_logger as cl
import logging

@pytest.mark.usefixtures("oneTimeSetUp", "setUp")
class TopsWomenLeftMenuTests(unittest.TestCase):
    log = cl.customLogger(logging.DEBUG)

    @pytest.fixture(autouse=True)
    def objectSetup(self, oneTimeSetUp):
        self.hp = HomePage(self.driver)
        self.wt = WomenTopsPage(self.driver)

    @pytest.mark.order(1)
    @pytest.mark.tops_women_page
    def test_WomenLeftMenuCategory_ListHidden(self):
        self.hp.navigateToLinkWomenTops()
        result1 = self.wt.verifyTopsWomenCategoryJacketDisplay()
        result_final = False
        if result1:
            self.log.info("Tops Women page - Category list should not be visible!")
            result_final = False
        else:
            self.log.info("Tops Women page - Category list is hidden")
            result_final = True
        assert result_final == True

    @pytest.mark.order(2)
    @pytest.mark.tops_women_page
    def test_WomenLeftMenuCategory_ListDisplayed(self):
        self.hp.navigateToLinkWomenTops()
        self.wt.navigateToTopsWomenCategoryLink()
        result1 = self.wt.verifyTopsWomenCategoryJacketDisplay()
        if result1:
            self.log.info("Tops Women page - Category list is displayed")
            result_final = True
        else:
            self.log.info("Tops Women page - Category list is not displayed!")
            result_final = False
        assert result_final == True

    @pytest.mark.order(3)
    @pytest.mark.tops_women_page
    def test_WomenLeftMenuCategoryJacketsFilter_Displayed(self):
        # test elements are displayed
        self.hp.navigateToLinkWomenTops()
        self.wt.navigateToTopsWomenCategoryLink()
        self.wt.navigateToTopsWomenCategoryJackets()
        result1 = self.wt.verifyTopsWomenCategoryFilterLabelDisplay()
        assert result1 == True
        result2 = self.wt.verifyTopsWomenCategoryFilterValueJacketsDisplay()
        assert result2 == True
        result3 = self.wt.verifyTopsWomenFilterClearAllDisplay()
        assert result3 == True
        # test that when pressing Clear all link, filter is cleared and page is top-women
        self.wt.clickTopsWomenFilterClearAll()
        result4 = self.hp.verifyWomenTopsURL()
        assert result4 == True
