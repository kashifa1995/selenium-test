import allure

from selenium.webdriver.common.by import By
from src.decorators.property import prop, method, allure_step
from src.pages.base_element import BaseElement
from src.pages.base_page import BasePage


class SearchPageDfpAds(BasePage):

#--------------------------------- Common locators for Destop and Mobile ----------------------------------
    
    @prop
    def page_title_header(self):
        locator = (By.CLASS_NAME, "pageTitle")
        return BaseElement(self.driver, locator)
    
    @method
    def listing_card(self, list_num):
        locator = (By.XPATH,
                    f"(//article//div[contains(@class,'title-wrapper') and @currentpage]/ancestor::a)[{list_num}]")
        return BaseElement(self.driver, locator)
    
    @prop
    def pagination(self):
        locator = (By.XPATH, 
                   "//div[@class='results per-row-1']/following-sibling::div[@class='ti-pagination']")
        return BaseElement(self.driver, locator)

#----------------------------------- Mobile Ad locators ------------------------------------------

    @method
    def mob_srp_ad(self, ad_pos):
        if ad_pos == "footer":
            locator = (By.XPATH, 
                       "//div[@data-fuse='mob_sale_sticky_footer'] |"
                       f"//div[@data-targeting-pos='{ad_pos}' and contains(@data-fuse,'mob_sale')]")
        else:
            locator = (By.XPATH, 
                   f"//div[@data-targeting-pos='{ad_pos}' and contains(@data-fuse,'mob_sale')]")
        return BaseElement(self.driver, locator)
    
    @method
    def mob_srp_ad_iframe(self, ad_pos):
        if ad_pos == "footer":
            locator = (By.XPATH, "//div[@data-fuse='mob_sale_sticky_footer']//iframe[@data-load-complete='true'] |"
                       f"//div[@data-targeting-pos='{ad_pos}' and contains(@data-fuse,'mob_sale')]//iframe[@data-load-complete='true']")
        else:
            locator = (By.XPATH, 
                    f"//div[@data-targeting-pos='{ad_pos}' and contains(@data-fuse,'mob_sale')]//iframe[@data-load-complete='true']")
        return BaseElement(self.driver, locator)
    
#--------------------------------- Desktop Ad Locators

    
#=================================== Functions =======================================================

    #-------------------------- Mobile Functions---------------------------------------

    @allure_step
    def assert_top_ad_position_mob_is_below_page_title_header(self):
        top_ad_rect = self.mob_srp_ad('top').get_rect()
        page_title_hdr_rect = self.page_title_header.get_rect()
        assert 0 <= (top_ad_rect['y'] - (page_title_hdr_rect['y'] + page_title_hdr_rect['height'])) < 50, \
        "Top ad is not below page title header"

    @allure_step
    def assert_spons_ad_position_mob_is_below_3rd_listing(self):
        spons_ad_rect = self.mob_srp_ad('spons').get_rect()
        listing_3_rect = self.listing_card('3').get_rect()
        assert 0 <= (spons_ad_rect['y'] - (listing_3_rect['y'] + listing_3_rect['height'])) < 100, \
        "Spons ad is not below 3rd listing card"

    @allure_step
    def assert_liner1_ad_position_mob_is_below_9th_listing(self):
        liner1_ad_rect = self.mob_srp_ad('liner1').get_rect()
        listing_9_rect = self.listing_card('9').get_rect()
        assert 0 <= (liner1_ad_rect['y'] - (listing_9_rect['y'] + listing_9_rect['height'])) < 100, \
        "liner1 ad is not below 9th listing card"

    @allure_step
    def assert_liner2_ad_position_mob_is_below_15th_listing(self):
        liner2_ad_rect = self.mob_srp_ad('liner2').get_rect()
        listing_15_rect = self.listing_card('15').get_rect()
        assert 0 <= (liner2_ad_rect['y'] - (listing_15_rect['y'] + listing_15_rect['height'])) < 100, \
        "liner2 ad is not below 15th listing card"

    @allure_step
    def assert_liner3_ad_position_mob_is_below_22nd_listing(self):
        liner3_ad_rect = self.mob_srp_ad('liner3').get_rect()
        listing_22_rect = self.listing_card('22').get_rect()
        assert 0 <= (liner3_ad_rect['y'] - (listing_22_rect['y'] + listing_22_rect['height'])) < 100, \
        "liner3 ad is not below 22nd listing card"

    @allure_step
    def assert_liner4_ad_position_mob_is_below_28th_listing(self):
        liner4_ad_rect = self.mob_srp_ad('liner4').get_rect()
        listing_28_rect = self.listing_card('28').get_rect()
        assert 0 <= (liner4_ad_rect['y'] - (listing_28_rect['y'] + listing_28_rect['height'])) < 100, \
        "liner4 ad is not below 28th listing card"

    @allure_step
    def assert_liner5_ad_position_mob_is_below_34th_listing(self):
        liner5_ad_rect = self.mob_srp_ad('liner5').get_rect()
        listing_34_rect = self.listing_card('34').get_rect()
        assert 0 <= (liner5_ad_rect['y'] - (listing_34_rect['y'] + listing_34_rect['height'])) < 100, \
        "liner5 ad is not below 34th listing card"

    @allure_step
    def assert_liner6_ad_position_mob_is_below_36th_listing(self):
        liner6_ad_rect = self.mob_srp_ad('liner6').get_rect()
        listing_36_rect = self.listing_card('36').get_rect()
        assert 0 <= (liner6_ad_rect['y'] - (listing_36_rect['y'] + listing_36_rect['height'])) < 100, \
        "liner6 ad is not below 36th listing card"

    @allure_step
    def assert_bottom_ad_position_mob_is_below_bottom_pagination(self):
        bottom_ad_rect = self.mob_srp_ad('bottom').get_rect()
        pagination_rect = self.pagination.get_rect()
        assert 0 <= (bottom_ad_rect['y'] - (pagination_rect['y'] + pagination_rect['height'])) < 50, \
        "bottom ad is not below pagination (bottom)"

    @allure_step
    def assert_sticky_footer_ad_position_mob_is_at_current_scroll_height_of_page(self):
        sticky_footer_ad_rect = self.mob_srp_ad('footer').get_rect()
        page_curr_scroll_height_rect = self.get_current_scroll_height()
        assert -1 <= (
            page_curr_scroll_height_rect - (sticky_footer_ad_rect['y'] + sticky_footer_ad_rect['height'])
            ) < 51, \
        "Sticky Footer ad is not at the bottom of Viewport"

    def verify_ad_position_srp_mob(self, ad_name):
        if ad_name == "top":
            return self.assert_top_ad_position_mob_is_below_page_title_header()
        elif ad_name == "spons":
            return self.assert_spons_ad_position_mob_is_below_3rd_listing()
        elif ad_name == "liner1":
            return self.assert_liner1_ad_position_mob_is_below_9th_listing()
        elif ad_name == "liner2":
            return self.assert_liner2_ad_position_mob_is_below_15th_listing()
        elif ad_name == "liner3":
            return self.assert_liner3_ad_position_mob_is_below_22nd_listing()
        elif ad_name == "liner4":
            return self.assert_liner4_ad_position_mob_is_below_28th_listing()
        elif ad_name == "liner5":
            return self.assert_liner5_ad_position_mob_is_below_34th_listing()
        elif ad_name == "liner6":
            return self.assert_liner6_ad_position_mob_is_below_36th_listing()
        elif ad_name == "bottom":
            return self.assert_bottom_ad_position_mob_is_below_bottom_pagination()
        elif ad_name == "footer":
            return self.assert_sticky_footer_ad_position_mob_is_at_current_scroll_height_of_page()
