import allure 
from src.pages.base_element import BaseElement
from src.pages.base_page import BasePage
from selenium.common.exceptions import TimeoutException
import time


class AdsVerificationUtil(BasePage):

    def verification_of_ads_by_criteria(
              self, ads_list, ads_loc, ads_iframe_loc: BaseElement, ads_pos_verifictn_meth, url=None):
        issues = []
        self.pause(3)
        for num, ad_name in enumerate(ads_list, start=1):
            try:
                with allure.step(f"{num} Verify '{ad_name.upper()}' ad when moving down"):
                    ad: BaseElement = ads_loc(ad_name)
                    ad.scroll_to_element(time_out=20, ss_on_fail=True)
                    self.get_screenshot()
                    if url:
                        ads_pos_verifictn_meth(url=url, ad_name=ad_name)
                    else:
                        ads_pos_verifictn_meth(ad_name)
                    with allure.step(f"Assert {ad_name} ad loaded"):
                        ads_iframe: BaseElement = ads_iframe_loc(ad_name)
                        ads_iframe.is_displayed(time_out=20, ss_on_fail=True)
                    self.get_screenshot()
            except TimeoutException as e:
                issues.append((f"{ad_name} failed (Moving down)", e.msg))
            except AssertionError as e:
                issues.append((f"{ad_name} failed (Moving down)", e.args))

        # with allure.step("Scroll to bottom of the page. Then, while scrolling back up, \
        #                 verify that ads are displayed."):
        #     self.scroll_to_bottom()

        # for num, ad_name in enumerate(reversed(ads_list)):
        #     try:
        #         with allure.step(f"{len(ads_list)-num} Verify '{ad_name.upper()}' ad when moving up"):
        #             ad: BaseElement = ads_loc(ad_name)
        #             ad.scroll_to_element(time_out=5, ss_on_fail=True)
        #             self.get_screenshot()
        #             if url:
        #                 ads_pos_verifictn_meth(url=url, ad_name=ad_name)
        #             else:
        #                 ads_pos_verifictn_meth(ad_name)
        #             with allure.step(f"Assert {ad_name} ad loaded"):
        #                 ads_iframe: BaseElement = ads_iframe_loc(ad_name)
        #                 ads_iframe.is_displayed(time_out=12, ss_on_fail=True)
        #             self.get_screenshot()
        #     except TimeoutException as e:
        #         issues.append((f"{ad_name} failed (Moving up)", e.msg))
        #     except AssertionError as e:
        #         issues.append((f"{ad_name} failed (Moving up)", e.args))

        return issues
