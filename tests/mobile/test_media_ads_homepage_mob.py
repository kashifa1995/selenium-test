import allure
import pytest
import unittest

from src.utils.config_manager import conf
from parameterized import parameterized
from src.pages.market_place.homepage.homepage_dfp_ads import HomePageDfpAds
from src.utils.browser_manager import BrowserManager
from src.utils.ads_verification_util import AdsVerificationUtil

from src.utils.urls import AERO_HOME_PAGE, ATV_HOME_PAGE, CTT_HOME_PAGE, CYCLE_HOME_PAGE, EQUIPMENT_HOME_PAGE, \
    PWC_HOME_PAGE, RV_HOME_PAGE, SNOWMOBILE_HOME_PAGE, BOAT_HOME_PAGE

#--------------------Available ads on HP of all realms--------------------
common_ads_hp_mob = ("hero","spons", "bottom")
boat_ads_hp_mob = ("hero", "spons", "bottom")
ctt_ads_hp_mob = ("hero","spons", "tile2", "bottom")

aero_ads_hp_mob = common_ads_hp_mob
atv_ads_hp_mob = common_ads_hp_mob
cycle_ads_hp_mob = common_ads_hp_mob
eqp_ads_hp_mob = common_ads_hp_mob
pwc_ads_hp_mob = common_ads_hp_mob
rv_ads_hp_mob = common_ads_hp_mob
snow_ads_hp_mob = common_ads_hp_mob

#------------------Description for ads on HP of all realms----------------------
common_descriptn_hp_mob = '''
    1 Hero Ad - Below main header
    2 Spons - Below search filters
    3 Bottom - Below footer
    '''

ctt_descriptn_hp_mob = '''
    1 Hero Ad - Below main header
    2 Spons - Below search filters
    3 tile2 - Below Guided search category (on CTT only)
    4 Bottom - Below footer
    '''

aero_descriptn_hp_mob = common_descriptn_hp_mob
atv_descriptn_hp_mob = common_descriptn_hp_mob
boat_descriptn_hp_mob = common_descriptn_hp_mob
cycle_descriptn_hp_mob = common_descriptn_hp_mob
eqp_descriptn_hp_mob = common_descriptn_hp_mob
pwc_descriptn_hp_mob = common_descriptn_hp_mob
rv_descriptn_hp_mob = common_descriptn_hp_mob
snow_descriptn_hp_mob = common_descriptn_hp_mob

# --------------- Test Class--------------------------------------
@allure.epic("Mobile")
@allure.story("Homepage")
class TestMediaAdsHomepageMob(unittest.TestCase):
    
    @classmethod
    def setUpClass(cls):
        cls.driver = BrowserManager.get_chrome()
        cls.hp_dfp = HomePageDfpAds(cls.driver)
        cls.ads_util = AdsVerificationUtil(cls.driver)

    def setUp(self):
        self.driver.delete_all_cookies()

    @parameterized.expand([
        (*AERO_HOME_PAGE, aero_ads_hp_mob, aero_descriptn_hp_mob), 
        (*ATV_HOME_PAGE, atv_ads_hp_mob, atv_descriptn_hp_mob),
        (*BOAT_HOME_PAGE, boat_ads_hp_mob, boat_descriptn_hp_mob), 
        (*CTT_HOME_PAGE, ctt_ads_hp_mob, ctt_descriptn_hp_mob), 
        (*CYCLE_HOME_PAGE, cycle_ads_hp_mob, cycle_descriptn_hp_mob), 
        (*EQUIPMENT_HOME_PAGE, eqp_ads_hp_mob, eqp_descriptn_hp_mob),
        (*PWC_HOME_PAGE, pwc_ads_hp_mob, pwc_descriptn_hp_mob), 
        (*RV_HOME_PAGE, rv_ads_hp_mob, rv_descriptn_hp_mob),
        (*SNOWMOBILE_HOME_PAGE, snow_ads_hp_mob, snow_descriptn_hp_mob)
        ])
    def test_verify_media_ads_on_mobile_hp(self, name, url, ads_list: list[str], descriptn):
        allure.dynamic.feature((name.split(" "))[0])
        allure.dynamic.description(descriptn)
        ads_loc = self.hp_dfp.mob_home_ad
        ads_iframe_loc = self.hp_dfp.mob_home_ad_iframe
        ads_pos_verifictn_meth = self.hp_dfp.verify_ad_position_hp_mob
        norfolk_coords = conf.geoloc_coord.norfolk_virginia
        self.hp_dfp.set_geolocation(lat=norfolk_coords.lat, long=norfolk_coords.long)
        self.hp_dfp.set_mobile()
        self.hp_dfp.open(name, url)
        issues = self.ads_util.verification_of_ads_by_criteria(
             ads_list=ads_list, ads_loc=ads_loc, ads_iframe_loc=ads_iframe_loc, 
             ads_pos_verifictn_meth=ads_pos_verifictn_meth
        )
        if issues:
                pytest.fail("Issue found:\n" + "\n".join(map(str, issues)))

    def tearDown(self):
        self.hp_dfp.add_page_source_and_screenshot_when_test_ends(
            self._outcome.errors, self.id()
        )

    @classmethod
    def tearDownClass(cls):
        cls.driver.quit()
