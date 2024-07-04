import random
import time

import allure

from selenium.webdriver.common.by import By
from src.decorators.property import prop, method, allure_step
from src.pages.base_element import BaseElement
from src.pages.base_page import BasePage


class HomePageDfpAds(BasePage):

#----------------------- Common locators for Desktop and Mobile -------------------------
    
    @prop
    def main_header(self):
        locator = (By.CLASS_NAME, "main-header")
        return BaseElement(self.driver, locator)
    
    @prop
    def search_filters_on_hp(self):
        locator = (By.CLASS_NAME, "index-search-width-canary")
        return BaseElement(self.driver, locator)
    
    @prop
    def gs_category_container_on_comm(self):
        locator = (By.CLASS_NAME, "category-section")
        return BaseElement(self.driver, locator)
    
    @prop
    def show_all_button_gs_icons_on_comm(self):
        locator = (By.CLASS_NAME, "show-all-button")
        return BaseElement(self.driver, locator)
    
    @prop
    def most_popular_boats_by_state_header(self):
        locator = (By.XPATH, "//h2[.='Most popular boats by state']")
        return BaseElement(self.driver, locator)
    
    @prop
    def buy_online_carousel(self):
        locator = (By.XPATH, 
                   "//div[contains(@class,'buy-online')]/following-sibling::div[@class='featured-wrapper']")
        return BaseElement(self.driver, locator)
    
    @prop
    def featured_listing_carousel(self):
        locator = (By.CLASS_NAME, "featuredHomePage")
        return BaseElement(self.driver, locator)
    
    @prop
    def sell_your_vehicle_banner(self):
        locator = (By.CLASS_NAME, "needToSellCont-wrapper")
        return BaseElement(self.driver, locator)
    
    @prop
    def rent_equipment_today_banner(self):
        locator = (By.ID, "rent-equipment-today")
        return BaseElement(self.driver, locator)
    
    @prop
    def footer(self):
        locator = (By.CLASS_NAME, "footerBg")
        return BaseElement(self.driver, locator)
    
#--------------------------Mobile Ad locators--------------------------------

    @method
    def mob_home_ad(self, ad_pos):
        locator = (By.XPATH, 
                   f"//div[@data-targeting-pos='{ad_pos}' and contains(@data-fuse,'mob_home')]")
        return BaseElement(self.driver, locator)
    
    @method
    def mob_home_ad_iframe(self, ad_pos):
        locator = (By.XPATH, 
                   f"//div[@data-targeting-pos='{ad_pos}' and contains(@data-fuse,'mob_home')]//iframe[@data-load-complete='true']")
        return BaseElement(self.driver, locator)
    
#--------------------------------- Desktop Ad Locators----------------------

    @method
    def desk_home_ad(self, ad_pos):
        locator = (By.XPATH, 
                   f"//div[@data-targeting-pos='{ad_pos}' and not(contains(@data-fuse,'mob_home'))]")
        return BaseElement(self.driver, locator)
    
    @method
    def desk_home_ad_iframe(self, ad_pos):
        locator = (By.XPATH, 
                   f"//div[@data-targeting-pos='{ad_pos}' and not(contains(@data-fuse,'mob_home'))]//iframe[@data-load-complete='true']")
        return BaseElement(self.driver, locator)
    
#=================================== Functions =======================================================

    #-------------------------- Mobile Functions---------------------------------------

    @allure_step
    def assert_hero_ad_position_mob_is_below_main_header(self):
        hero_ad_rect = self.mob_home_ad("hero").get_rect()
        main_header_rect = self.main_header.get_rect()
        assert 0 <= (hero_ad_rect['y'] - (main_header_rect['y'] + main_header_rect['height'])) < 2,\
        "Hero ad is not below main header"

    @allure_step
    def assert_spons_ad_position_mob_is_below_search_filters(self):
        spons_ad_rect = self.mob_home_ad("spons").get_rect()
        search_filters_rect = self.search_filters_on_hp.get_rect()
        assert 0 <= (spons_ad_rect['y'] - (search_filters_rect['y'] + search_filters_rect['height'])) < 50,\
        "Spons ad is not below Search filters"

    @allure_step
    def assert_tile2_ad_position_mob_is_below_gs_category_container(self):
        tile2_ad_rect = self.mob_home_ad("tile2").get_rect()
        gs_cat_cont_rect = self.gs_category_container_on_comm.get_rect()
        assert 0 <= (tile2_ad_rect['y'] - (gs_cat_cont_rect['y'] + gs_cat_cont_rect['height'])) < 100,\
        "Tile2 ad is not below Show all button of guided search icons"

    @allure_step
    def assert_bottom_ad_position_mob_is_below_footer(self):
        bottom_ad_rect = self.mob_home_ad("bottom").get_rect()
        footer_rect = self.footer.get_rect()
        assert 0 <= (bottom_ad_rect['y'] - (footer_rect['y'] + footer_rect['height'])) < 50,\
        "Bottom ad is not below footer"

    def verify_ad_position_hp_mob(self, ad_name):
        if ad_name == "hero":
            return self.assert_hero_ad_position_mob_is_below_main_header()
        elif ad_name == "spons":
            return self.assert_spons_ad_position_mob_is_below_search_filters()
        elif ad_name == "bottom":
            return self.assert_bottom_ad_position_mob_is_below_footer()
        elif ad_name == "tile2":
            return self.assert_tile2_ad_position_mob_is_below_gs_category_container()
        
    #------------------ Desktop Functions -----------------------------
        
    @allure_step
    def assert_hero_ad_position_desk_is_below_main_header(self):
        hero_ad_rect = self.desk_home_ad("hero").get_rect()
        main_header_rect = self.main_header.get_rect()
        assert -1 <= (hero_ad_rect['y'] - (main_header_rect['y'] + main_header_rect['height'])) < 2,\
        "Hero ad is not below main header"

    def assert_leader_ad_position_desk(self, url):
        leader_ad_rect = self.desk_home_ad("leader").get_rect()
        if "boatmart" in url:
            with allure.step("Assert leader ad position is above Most popular boats by state header"):
                most_pop_boat_hdr_rect = self.most_popular_boats_by_state_header.get_rect()
                assert 0 <= (most_pop_boat_hdr_rect['y'] - (leader_ad_rect['y'] + leader_ad_rect['height'])) < 200,\
                "Leader ad is not above Most popular boats by state header"
        elif any([i in url for i in ["cycle", "atv"]]):
            with allure.step("Assert Leader ad is above Buy Online Carousel"):
                buy_online_carousel_rect = self.buy_online_carousel.get_rect()
                assert 0 <= (buy_online_carousel_rect['y'] - (leader_ad_rect['y'] + leader_ad_rect['height'])) < 200,\
                "Leader ad is not above Buy Online Carousel"
        else:
            with allure.step("Assert Leader ad is above Featured listing carousel"):
                feature_list_carsl_rect = self.featured_listing_carousel.get_rect()
                assert 0 <= (feature_list_carsl_rect['y'] - (leader_ad_rect['y'] + leader_ad_rect['height'])) < 200,\
                "Leader ad is not above Featured listing carousel"

    @allure_step
    def assert_tile2_ad_postion_desk_is_in_right_of_gs_category_container(self):
        tile2_ad_rect = self.desk_home_ad("tile2").get_rect()
        gs_cat_cont_rect = self.gs_category_container_on_comm.get_rect()
        assert -1 <= (tile2_ad_rect['x'] - (gs_cat_cont_rect['x'] + gs_cat_cont_rect['width'])) < 2,\
        "tile2 ad is not in right of Guided search category container"

    @allure_step
    def assert_right1_ad_position_desk_is_in_right_of_featured_listing_carousel(self):
        right1_ad_rect = self.desk_home_ad("right1").get_rect()
        feature_list_carsl_rect = self.featured_listing_carousel.get_rect()
        assert -1 <= (
            right1_ad_rect['x'] - (feature_list_carsl_rect['x'] + feature_list_carsl_rect['width'])
            ) < 2, \
        "right1 ad is not in right of feature listing carousel"

    def assert_bottom_ad_position_desk(self, url):
        bottom_ad_rect = self.desk_home_ad("bottom").get_rect()
        if "equipment" in url:
            with allure.step("Assert Bottom ad is below Rent Equipment Today Banner"):
                rent_eqp_banner_rect = self.rent_equipment_today_banner.get_rect()
                assert 0 <= (bottom_ad_rect['y'] - (rent_eqp_banner_rect['y'] + rent_eqp_banner_rect['height'])) < 50,\
                "Bottom ad is not below Rent Equipment Today Banner"
        else:
            with allure.step("Assert Bottom ad is below Sell Your Vehicle Banner"):
                sell_veh_banner_rect = self.sell_your_vehicle_banner.get_rect()
                assert 0 <= (bottom_ad_rect['y'] - (sell_veh_banner_rect['y'] + sell_veh_banner_rect['height'])) < 150,\
                "Bottom ad is not below Sell Your Vehicle Banner"

    @allure_step
    def assert_right2_ad_position_desk_is_below_footer(self):
        right2_ad_rect = self.desk_home_ad("right2").get_rect()
        footer_rect = self.footer.get_rect()
        assert 0 <= (right2_ad_rect['y'] - (footer_rect['y'] + footer_rect['height'])) < 50,\
        "Right2 ad is not below footer"

    def verify_ad_position_hp_desk(self, url, ad_name):
        if ad_name == "hero":
            return self.assert_hero_ad_position_desk_is_below_main_header()
        elif ad_name == "leader":
            return self.assert_leader_ad_position_desk(url)
        elif ad_name == "tile2":
            return self.assert_tile2_ad_postion_desk_is_in_right_of_gs_category_container()
        elif ad_name == "right1":
            return self.assert_right1_ad_position_desk_is_in_right_of_featured_listing_carousel()
        elif ad_name == "bottom":
            return self.assert_bottom_ad_position_desk(url)
        elif ad_name == "right2":
            return self.assert_right2_ad_position_desk_is_below_footer()
        