import allure
import os
import requests

from src.decorators.property import allure_step
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.alert import Alert 
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.remote.webdriver import WebDriver
from selenium.common.exceptions import ElementNotVisibleException, ElementClickInterceptedException, \
    NoSuchElementException, StaleElementReferenceException, ElementNotInteractableException, NoAlertPresentException


class BasePage:

    def __init__(self, driver):
        self.driver: WebDriver = driver

    time_out = 40
    poll_frequency = 1
    ignored_exceptions = (ElementNotVisibleException,
                          ElementClickInterceptedException,
                          NoSuchElementException,
                          ElementNotInteractableException,
                          StaleElementReferenceException,
                          NoAlertPresentException,
                          KeyError)
    view_port_script = "return window.innerHeight;" 
    current_scroll_height_script = "return window.pageYOffset + window.innerHeight"

    def wait(self, method, message: str):
        return WebDriverWait(
            self.driver,
            self.time_out,
            self.poll_frequency,
            self.ignored_exceptions,
        ).until(method, message)
    
    def add_cookie_for_rv_trader(self, url):
        if "rvtrader" in url:
            cookie = {'name' : 'CANARY_VALUE', 'value' : 'alpha', 'url': url}
            self.driver.execute_cdp_cmd('Network.enable', {})
            self.driver.execute_cdp_cmd('Network.setCookie', cookie)
            self.driver.execute_cdp_cmd('Network.disable', {})

    @allure_step
    def go(self, url, cond=None):
        if "DESIGN" in os.environ and os.environ["DESIGN"] == "old":
            self.add_cookie_for_rv_trader(url)

        def condition(_):
            self.driver.get(url)
            if url in self.driver.current_url:
                return True

        if cond:
            return self.wait(condition, f'redirecting to incorrect URL {self.driver.current_url}')
        else:
            return self.driver.get(url)
        
    # To open the URL, if cond=False, it won't use selenium wait
    # If dev=True, Then it will switch the environment to dev before opening the page, irrespective of env given in "ENV"
    def open(self, name, url, cond=True, dev=False):
        if dev and "prod" in url:
            url = url.replace("prod", "dev")
        with allure.step(f'''Open {name},
                         URL = {url}'''):
            self.go(url, cond=cond)
            self.get_screenshot()
            res = requests.get(self.driver.current_url)
            status_code = res.status_code
            if status_code < 200 and status_code >= 300:
                raise Exception(f"Page not accessible - status_code: {status_code}")
            elif "Server Error" in self.driver.title:
                raise Exception("Server Error")

    @allure_step
    def scroll_to_bottom(self):
        self.driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")

    @allure.step("Page is refreshed")
    def refresh(self):
        self.driver.refresh()

    def get_title(self):
        return self.driver.title

    def quit(self):
        self.driver.delete_all_cookies()
        self.driver.quit()

    @property
    def current_url(self):
        url = self.driver.current_url

        with allure.step(f"The current URL of the page is {url}"):
            return url

    @allure.step("Scroll to top of the page")
    def scroll_to_top(self):
        self.driver.execute_script("window.scrollTo(0,0)")
        self.get_screenshot()

    def pause(self, time):
        return ActionChains(self.driver).pause(time).perform()

    def switch_to_iframe(self, iframe):
        self.driver.switch_to.frame(iframe)

    def switch_to_default(self):
        self.driver.switch_to.default_content()

    @allure.step("Screenshot")
    def get_screenshot(self):
        screen_shot = self.driver.get_screenshot_as_png()
        return allure.attach(body=screen_shot, name="Screenshot", attachment_type=allure.attachment_type.PNG)

    @allure.step("Set device = 'MOBILE'")
    def set_mobile(self):
        self.driver.set_window_size("390", "844")

    @allure.step("Set device = 'TABLET'")
    def set_tablet(self):
        self.driver.set_window_size("820", "1180")

    def page_source(self):
        return self.driver.page_source

    def add_page_source_and_screenshot_when_test_ends(self, errors, id_name):
        """Take a page source driver homepage, when it Failed."""
        for method, error in errors:
            if error:
                with allure.step("PageSource for failed test"):
                    page_source = self.page_source()
                    allure.attach(body=page_source, name=f"page_source_{id_name}",
                              attachment_type=allure.attachment_type.HTML)
        self.get_screenshot()

    def get_viewport_height(self):
        viewport_height = self.driver.execute_script(self.view_port_script)
        with allure.step(f"Viewport height is {viewport_height}"):
            return viewport_height
        
    def get_current_scroll_height(self):
        curr_scroll_height = self.driver.execute_script(self.current_scroll_height_script)
        with allure.step(f"Current scroll height of page is {curr_scroll_height}"):
            return curr_scroll_height
    
    # ---- Switch to the alert, get its text, and handles it based on the accept or dismiss params.
    # ---- Return alert text.
    @allure_step
    def switch_to_alert_n_get_alert_text(self, accept=False, dismiss=False):   
        def condition(_):
            alert = Alert(self.driver)
            text = alert.text
            if accept:
                alert.accept()
            elif dismiss:
                alert.dismiss()
            return text
               
        return self.wait(condition, "No alert is present")
    
    def set_geolocation(self, lat, long):
        params = {
            "latitude": lat,
            "longitude": long,
            "accuracy": 100
        }
        self.driver.execute_cdp_cmd("Browser.grantPermissions", {
            "permissions": ["geolocation"]
        })
        self.driver.execute_cdp_cmd("Emulation.setGeolocationOverride", params
            )
