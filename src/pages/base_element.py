import time

import allure

from selenium.common.exceptions import ElementNotVisibleException, ElementClickInterceptedException, \
    NoSuchElementException, StaleElementReferenceException, ElementNotInteractableException, TimeoutException, \
    InvalidElementStateException
from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.select import Select

SCROLL_SCRIPT = "arguments[0].scrollIntoView({block: 'center', inline: 'nearest'});"


class BaseElement(object):
    time_out = 50
    poll_frequency = 1
    ignored_exceptions = (ElementNotVisibleException,
                          ElementClickInterceptedException,
                          NoSuchElementException,
                          ElementNotInteractableException,
                          StaleElementReferenceException,
                          InvalidElementStateException)

    def __init__(self, driver: WebDriver, locator, prop_name=None, method_name=None, par=None):
        self.driver: WebDriver = driver
        self.locator = locator
        self.prop_name = prop_name
        self.method_name = method_name
        self.par = par

    def get_screenshot(self):
        screen_shot = self.driver.get_screenshot_as_png()
        return allure.attach(body=screen_shot, name="Screenshot", attachment_type=allure.attachment_type.PNG)

    def wait(self, method, message: str, time_out=None, ss_on_fail=False):
        if not time_out:
            time_out = self.time_out
        try:
            return WebDriverWait(
                driver=self.driver,
                timeout=time_out,
                poll_frequency=self.poll_frequency,
                ignored_exceptions=self.ignored_exceptions,
            ).until(method, message)
        except TimeoutException:
            if ss_on_fail:
                self.get_screenshot()
            if "Server Error" in self.driver.title:
                raise Exception("Server Error")
            else:
                raise TimeoutException(message)

    @property
    def name(self):
        if self.prop_name is None:
            name = f"{self.par} {self.method_name}"
        else:
            name = self.prop_name
        return name

    def __find_elements(self, ignore_exception=False) -> list[WebElement]:
        elements = self.driver.find_elements(*self.locator)
        if not elements and ignore_exception:
            return elements
        elif not elements:
            raise NoSuchElementException(f'No element found by {self.locator=}')

        return elements

    def __find_element(self) -> WebElement:
        return self.__find_elements()[0]

    def wait_until_visible(self) -> WebElement:
        def condition(_):
            element = self.__find_element()
            if element.is_displayed():
                return element

        return self.wait(condition, f'Wait until element displayed by {self.locator=}')

    def wait_until_all_elements_visible(self):
        def condition(_):
            elements: list = self.__find_elements()
            if all([i.is_displayed() for i in elements]):
                return elements

        return self.wait(condition, f'Wait until elements are displayed by {self.locator=}')

    def wait_until_all_elements_enabled(self):
        def condition(_):
            elements: list = self.__find_elements()
            if all([i.is_enabled() or i.is_displayed() for i in elements]):
                return elements

        return self.wait(condition, f'Wait until elements are enabled by {self.locator=}')

    def click(self, not_visible=False):
        def condition(_):
            if not_visible:
                element = self.__find_element()
                time.sleep(2)
                element.click()
                return True
            else:
                element = self.wait_until_visible()
                time.sleep(2)
                element.click()
                return True

        with allure.step(f"Click on {self.name}"):
            self.wait(condition, f'Unable to click on {self.locator=}')

    def send_keys(self, *value):
        def condition(_):
            element = self.wait_until_visible()
            element.send_keys(value)
            return True

        with allure.step(f"Type '{value}' into {self.name}"):
            self.wait(condition, f'Unable to sendkeys on {self.locator=}')

    def is_displayed(self, multiple=False, time_out=None, ss_on_fail=False) -> bool:
        def condition(_):
            elements: list[WebElement] = self.__find_elements()
            if not multiple:
                return (elements[0]).is_displayed()

            return all([i.is_displayed() for i in elements])

        with allure.step(f"Check '{self.name}' is displayed?"):
            result = self.wait(
                method=condition, 
                message=f'{self.locator=} is not displayed', 
                time_out=time_out, 
                ss_on_fail=ss_on_fail)
            return result

    def text(self, get_list=False, not_displayed=False):
        def condition(_):
            if not_displayed:
                elements: list[WebElement] = self.__find_elements()
                texts = [i.text for i in elements]

                if get_list or len(elements) != 1:
                    return texts
                else:
                    return texts[0]

            else:
                elements: list[WebElement] = self.wait_until_all_elements_visible()
                texts = [i.text for i in elements]

                if get_list or len(elements) != 1:
                    return texts
                else:
                    return texts[0]

        text = self.wait(condition, f'Unable to get text of {self.locator=}')
        if not get_list:
            with allure.step(f"Got '{text=}' from {self.name}"):
                return text
        else:
            return text

    def select_by_value(self, value):
        def condition(_):
            element = self.wait_until_visible()
            Select(element).select_by_value(value)
            return True

        with allure.step(f"Choose {value} from {self.name}"):
            result = self.wait(condition, f'Unable to select value of {self.locator=}')
            return result

    def select_by_visible_text(self, text):
        def condition(_):
            element = self.wait_until_visible()
            Select(element).select_by_visible_text(text)
            return True

        with allure.step(f"Select {text} from {self.name}"):
            result = self.wait(condition, f'Unable to select value of {self.locator=}')
            return result

    def clear(self):
        def condition(_):
            element = self.wait_until_visible()
            element.clear()
            return True

        with allure.step(f"Cleared text from {self.name}"):
            self.wait(condition, f'Unable to click on {self.locator=}')

    def scroll_to_element(self, dont_wait=False, time_out=None, ss_on_fail=False):
        def condition(_):
            element = self.__find_element()
            self.driver.execute_script(SCROLL_SCRIPT, element)
            return True

        with allure.step(f"Scroll to {self.name}"):
            if dont_wait:
                ele = self.__find_element()
                self.driver.execute_script(SCROLL_SCRIPT, ele)
                return True
            else:
                result = self.wait(condition, f'Not able to scroll to {self.locator=}', time_out=time_out, 
                ss_on_fail=ss_on_fail)
                return result

    def is_selected(self) -> bool:

        def condition(_):
            element = self.__find_element()
            return element.is_selected()

        with allure.step(f"Verify that {self.name} chosen is selected"):
            result = self.wait(condition, f'Unable to select {self.locator=}')
            return result

    def java_script_click(self):

        def condition(_):
            element = self.__find_element()
            self.driver.execute_script("arguments[0].click();", element)
            return True

        with allure.step(f"Click on {self.name}"):
            self.wait(condition, f'Unable to click on {self.locator=}')

    def double_click(self):
        def condition(_):
            element = self.wait_until_visible()
            ActionChains(self.driver).double_click(element).perform()
            return True

        with allure.step(f" Double Click on {self.name}"):
            self.wait(condition, f'Unable to click on {self.locator=}')

    def get_attribute(self, name, get_list=False):
        def condition(_):
            elements: list[WebElement] = self.wait_until_all_elements_visible()

            get_attribute = [i.get_attribute(name) for i in elements]

            if get_list or len(elements) != 1:
                return get_attribute
            else:
                return get_attribute[0]

        attribute = self.wait(condition, f'Unable to get {name} of {self.locator=}')
        with allure.step(f"Got '{attribute=}' from {self.name}"):
            return attribute

    def not_displayed(self) -> bool:
        def condition(_):
            element = self.__find_element()
            if not element.is_displayed():
                return True

        with allure.step(f"Check '{self.name}' is not displayed?"):
            result = self.wait(condition, f'{self.locator=} is displayed')
            return result

    def get_value_of_css_property(self, property_name):
        def condition(_):
            element = self.__find_element()
            css_property_value = element.value_of_css_property(property_name)
            return css_property_value

        result = self.wait(condition, f'Not getting css value of {self.locator=} ')
        with allure.step(f"'{property_name} of {self.name}' is {result}"):
            return result

    def get_location(self):
        def condition(_):
            element: WebElement = self.__find_element()
            location = element.location
            return location

        result = self.wait(condition, f'Not getting css value of {self.locator=} ')
        with allure.step(f"'Location of {self.name}' is {result}"):
            return result

    def get_property(self, name):
        def condition(_):
            element: WebElement = self.__find_element()
            property_of_element = element.get_property(name)
            return property_of_element

        result = self.wait(condition, f'Not getting {name} of {self.locator=} ')
        with allure.step(f"{result} is {name} of {self.name}"):
            return result

    def not_present(self) -> bool:

        def condition(_):
            element = self.__find_elements(ignore_exception=True)
            if len(element) == 0:
                return True

        with allure.step(f"Check '{self.name}' is not present on DOM"):
            result = self.wait(condition, f'{self.locator=} is present on DOM')
            return result
        
    def not_selected(self) -> bool:

        def condition(_):
            element = self.__find_element()
            return not element.is_selected()

        with allure.step(f"Verify that {self.name} chosen is selected"):
            result = self.wait(condition, f'Unable to select {self.locator=}')
            return result
        
    def get_rect(self):
        def condition(_):
            element: WebElement = self.__find_element()
            rect = element.rect
            return rect

        result = self.wait(condition, f'Not getting rect value of {self.locator=} ')
        with allure.step(f"'Rect of {self.name}' is {result}"):
            return result
