import allure
import uuid
import pytest
import unittest
from os import path

from src.utils.config_manager import conf
from parameterized import parameterized
from src.pages.market_place.homepage.homepage_dfp_ads import HomePageDfpAds
from src.utils.browser_manager import BrowserManager
from src.utils.ads_verification_util import AdsVerificationUtil

from src.utils.urls import AERO_HOME_PAGE, ATV_HOME_PAGE, CTT_HOME_PAGE, CYCLE_HOME_PAGE, EQUIPMENT_HOME_PAGE, \
    PWC_HOME_PAGE, RV_HOME_PAGE, SNOWMOBILE_HOME_PAGE, BOAT_HOME_PAGE

#--------------------Available ads on HP of all realms--------------------
common_ads_hp_desk = ("hero", "leader", "right1", "bottom", "right2")
ctt_ads_hp_desk = ("hero",  "leader", "tile2", "right1", "bottom", "right2")

aero_ads_hp_desk = common_ads_hp_desk
atv_ads_hp_desk = common_ads_hp_desk
boat_ads_hp_desk = common_ads_hp_desk
cycle_ads_hp_desk = common_ads_hp_desk
eqp_ads_hp_desk = common_ads_hp_desk
pwc_ads_hp_desk = common_ads_hp_desk
rv_ads_hp_desk = common_ads_hp_desk
snow_ads_hp_desk = common_ads_hp_desk

#------------------Description for ads on HP of all realms----------------------
common_descriptn_hp_desk = '''
    1 Hero Ad - Below main header
    2 Leader Ad - Above Featured listing carousel
    3 Right1 Ad - Positioned in right of Feature listing carousel
    4 Bottom Ad - Below Sell Your Vehicle Banner
    5 Right2 Ad - below Footer'''

boat_descriptn_hp_desk='''
    1 Hero Ad - Below main header
    2 Leader Ad - Above Most Popular boats by State header
    3 Right1 Ad - Positioned in right of Feature listing carousel
    4 Bottom Ad - Below Sell Your Vehicle Banner
    5 Right2 Ad - Below Footer'''

ctt_descriptn_hp_desk = '''
    1 Hero Ad - Below main header
    2 Tile2 - Positioned in right of Guided Search category container
    3 Leader Ad - Above Most Popular boats by State header
    4 Right1 Ad - Positioned in right of Feature listing carousel
    5 Bottom Ad - Below Sell Your Vehicle Banner
    6 Right2 Ad - Below Footer'''

cycle_descriptn_hp_desk = '''
    1 Hero Ad - Below main header
    2 Leader Ad - Above Buy Online carousel
    3 Right1 Ad - Positioned in right of Feature listing carousel
    4 Bottom Ad - Below Sell Your Vehicle Banner
    5 Right2 Ad - Below Footer'''

eqp_descriptn_hp_desk = '''
    1 Hero Ad - Below main header
    2 Leader Ad - Above Buy Online carousel
    3 Right1 Ad - Positioned in right of Feature listing carousel
    4 Bottom Ad - Below Rent Equipment Today Banner
    5 Right2 Ad - Below Footer'''

aero_descriptn_hp_desk = common_descriptn_hp_desk
atv_descriptn_hp_desk = cycle_descriptn_hp_desk
pwc_descriptn_hp_desk = common_descriptn_hp_desk
rv_descriptn_hp_desk = common_descriptn_hp_desk
snow_descriptn_hp_desk = common_descriptn_hp_desk

# --------------- Test Class--------------------------------------
@allure.epic("Desktop")
@allure.story("Homepage")
class TestMediaAdsHomepageMob1(unittest.TestCase):
    
    @classmethod
    def setUpClass(cls):
        cls.random_id = str(uuid.uuid4())[:8]
        cls.driver = BrowserManager.get_chrome()
        cls.hp_dfp = HomePageDfpAds(cls.driver)
        cls.ads_util = AdsVerificationUtil(cls.driver)

    def setUp(self):
        self.driver.delete_all_cookies()

    @parameterized.expand([
        # (*AERO_HOME_PAGE, aero_ads_hp_desk, aero_descriptn_hp_desk), 
        # (*ATV_HOME_PAGE, atv_ads_hp_desk, atv_descriptn_hp_desk),
        # (*BOAT_HOME_PAGE, boat_ads_hp_desk, boat_descriptn_hp_desk), 
        # (*CTT_HOME_PAGE, ctt_ads_hp_desk, ctt_descriptn_hp_desk), 
        # (*CYCLE_HOME_PAGE, cycle_ads_hp_desk, cycle_descriptn_hp_desk), 
        # (*EQUIPMENT_HOME_PAGE, eqp_ads_hp_desk, eqp_descriptn_hp_desk),
        # (*PWC_HOME_PAGE, pwc_ads_hp_desk, pwc_descriptn_hp_desk), 
        # (*RV_HOME_PAGE, rv_ads_hp_desk, rv_descriptn_hp_desk),
        (*SNOWMOBILE_HOME_PAGE, snow_ads_hp_desk, snow_descriptn_hp_desk)
        ])
    def test_verify_media_ads_on_desktop_hp(self, name, url, ads_list: list[str], descriptn):
        with allure.step(self.random_id):
             print(self.random_id)
        allure.dynamic.feature((name.split(" "))[0])
        allure.dynamic.description(descriptn)
        ads_loc = self.hp_dfp.desk_home_ad
        ads_iframe_loc = self.hp_dfp.desk_home_ad_iframe
        ads_pos_verifictn_meth = self.hp_dfp.verify_ad_position_hp_desk
        # norfolk_coords = conf.geoloc_coord.norfolk_virginia
        # self.hp_dfp.set_geolocation(lat=norfolk_coords.lat, long=norfolk_coords.long)
        self.hp_dfp.open(name, url)
        issues = self.ads_util.verification_of_ads_by_criteria(
             ads_list=ads_list, ads_loc=ads_loc, ads_iframe_loc=ads_iframe_loc, 
             ads_pos_verifictn_meth=ads_pos_verifictn_meth, url=url
        )
        if issues:
                pytest.fail("Issue found:\n" + "\n".join(map(str, issues)))

    def tearDown(self):
        self.hp_dfp.add_page_source_and_screenshot_when_test_ends(
            self._outcome.errors, self.id()
        )
        # root_dir = path.abspath(f'{__file__}/../../../../')
        # body = f'{root_dir}\chrome_logs\{self.random_id}.log'
        # with open(body, "r") as log_file:
        #     allure.attach(log_file.read(), name="driver_logs", attachment_type=allure.attachment_type.TEXT)

    @classmethod
    def tearDownClass(cls):
        cls.driver.quit()
