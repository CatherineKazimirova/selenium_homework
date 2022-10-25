from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException


class BasePage:
    def __init__(self, driver):
        self.driver = driver

    def element(self, locator: tuple):
        try:
            return WebDriverWait(self.driver, 8).until(EC.visibility_of_element_located(locator))
        except TimeoutException:
            raise AssertionError(f"The element is not found {locator}")

    def elements(self, locator: tuple):
        try:
            return WebDriverWait(self.driver, 10).until(EC.visibility_of_all_elements_located(locator))
        except TimeoutException:
            raise AssertionError(f"The elements are not found {locator}")

    def text(self, locator: tuple, text: str):
        try:
            return WebDriverWait(self.driver, 5).until(EC.text_to_be_present_in_element(locator, text))
        except TimeoutException:
            raise AssertionError(f"The text in the element not found {locator}")

    def alert(self, locator: tuple):
        try:
            WebDriverWait(self.driver, 5).until(EC.alert_is_present())
            self.driver.switch_to.alert.accept()
            WebDriverWait(self.driver, 5).until(EC.visibility_of_element_located(locator))
        except TimeoutException:
            raise AssertionError(f"Delete confirmation is not found {locator}")
