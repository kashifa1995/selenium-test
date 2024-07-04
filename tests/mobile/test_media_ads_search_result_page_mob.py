import allure
import pytest
import unittest

from src.utils.config_manager import conf
from parameterized import parameterized
from src.pages.market_place.srp.search_page_dfp_ads import SearchPageDfpAds
from src.utils.browser_manager import BrowserManager
from src.utils.ads_verification_util import AdsVerificationUtil
from src.utils.urls import CTT_SEARCH_PAGE, RV_SEARCH_PAGE, CYCLE_SEARCH_PAGE, EQUIPMENT_SEARCH_PAGE,\
    ATV_SEARCH_PAGE, PWC_SEARCH_PAGE, SNOWMOBILE_SEARCH_PAGE, AERO_SEARCH_PAGE, BOAT_SEARCH_PAGE

ALL_REALMS_SRP = [AERO_SEARCH_PAGE, ATV_SEARCH_PAGE, CTT_SEARCH_PAGE, CYCLE_SEARCH_PAGE,
                  EQUIPMENT_SEARCH_PAGE, PWC_SEARCH_PAGE, RV_SEARCH_PAGE, SNOWMOBILE_SEARCH_PAGE, BOAT_SEARCH_PAGE]

#--------------------Available ads on SRP of all realms--------------------
common_ads_srp_mob = ("top", "footer", "spons", "liner1", "liner2", "liner3", "liner4", "liner5", 
                      "liner6", "bottom")

#------------------Description for ads on SRP of all realms----------------------
common_descriptn_srp_mob = '''
    1 Top - Below Page Title header
    2 Footer (sticky footer) - At Scroll height (bottom of viewport)
    3 Spons - Below 3rd listing card
    4 Liner1 - Below 9th listing card
    6 Liner2 - Below 15th listing card
    6 Liner3 - Below 22nd listing card
    7 Liner4 - Below 28th listing card
    8 Liner5 - Below 34th listing card
    9 Liner6 - Below 36th listing card
    10 Bottom - Below Pagination (After all listing cards)
    '''


# --------------- Test Class--------------------------------------
@allure.epic("Mobile")
@allure.story("Search Result Page")
class TestMediaAdsSearchResultPageMob(unittest.TestCase):
    
    @classmethod
    def setUpClass(cls):
        cls.driver = BrowserManager.get_chrome()
        cls.srp_dfp = SearchPageDfpAds(cls.driver)
        cls.ads_util = AdsVerificationUtil(cls.driver)

    def setUp(self):
        self.driver.delete_all_cookies()

    @parameterized.expand(ALL_REALMS_SRP)
    def test_verify_media_ads_on_mobile_srp(self, name, url):
        ads_list = common_ads_srp_mob
        descriptn = common_descriptn_srp_mob
        allure.dynamic.feature((name.split(" "))[0])
        allure.dynamic.description(descriptn)
        ads_loc = self.srp_dfp.mob_srp_ad
        ads_iframe_loc = self.srp_dfp.mob_srp_ad_iframe
        ads_pos_verifictn_meth = self.srp_dfp.verify_ad_position_srp_mob
        norfolk_coords = conf.geoloc_coord.norfolk_virginia
        self.srp_dfp.set_geolocation(lat=norfolk_coords.lat, long=norfolk_coords.long)
        self.srp_dfp.set_mobile()
        self.srp_dfp.open(name, url)
        issues = self.ads_util.verification_of_ads_by_criteria(
            ads_list=ads_list, ads_loc=ads_loc, ads_iframe_loc=ads_iframe_loc, 
            ads_pos_verifictn_meth=ads_pos_verifictn_meth
        )
        if issues:
                pytest.fail("Issue found:\n" + "\n".join(map(str, issues)))

    def tearDown(self):
        self.srp_dfp.add_page_source_and_screenshot_when_test_ends(
            self._outcome.errors, self.id()
        )

    @classmethod
    def tearDownClass(cls):
        cls.driver.quit()
