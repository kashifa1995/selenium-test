from selenium import webdriver
import random
from os import path
import pytest
from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.core.driver_cache import DriverCacheManager
from retry import retry
from selenium.webdriver.chrome.options import Options

root_dir = path.abspath(f'{__file__}/../../../')
cache_manager = DriverCacheManager(root_dir=root_dir)


class BrowserManager(object):

    @classmethod
    @retry(delay=1, tries=5)
    def get_chrome(cls) -> WebDriver:
        options = Options()
        options.add_argument("--window-size=1920,1080")
        options.add_argument('--disable-dev-shm-usage')
        # user_agent = "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/126.0.6478.127 Safari/537.36"
        # options.add_argument(f"--useragent={user_agent}")
        options.add_argument('--no-sandbox')
        # options.add_argument("--headless")
        options.add_experimental_option("excludeSwitches", [
            "enable-automation",
            "enable-logging",
        ])
        options.add_experimental_option("prefs", {
            'credentials_enable_service': False,
            'profile': {'password_manager_enabled': False},
        })
        options.add_argument("disable-infobars")
        options.add_argument("--disable-blink-features=AutomationControlled")
        options.add_experimental_option("prefs", {"profile.block_third_party_cookies": False})
        options.add_experimental_option('useAutomationExtension', False)
        # options.set_capability('pageLoadStrategy', 'eager')
        return webdriver.Chrome(service=ChromeService(
            ChromeDriverManager(cache_manager=cache_manager).install()), options=options)

    @classmethod
    def get_edge(cls):
        raise NotImplementedError('Edge Browser is not supported')
    
