import logging
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
import allure
from allure_commons.types import AttachmentType


class BasePage:
    def __init__(self, driver):
        self.driver = driver

        self.logger = logging.getLogger(type(self).__name__)
        file_handler = logging.FileHandler(f"logs/{self.driver.test_name}.log")
        file_handler.setFormatter(logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s'))
        if self.logger.hasHandlers():
            self.logger.handlers.clear()
        self.logger.addHandler(file_handler)
        self.logger.setLevel(level=self.driver.log_level)

    def get_screen(self):
        allure.attach(self.driver.get_screenshot_as_png(), name="Screenshot", attachment_type=AttachmentType.PNG)

    def check_element(self, locator: tuple):
        try:
            self.logger.info(f"Checking element: {locator}")
            return WebDriverWait(self.driver, 8).until(EC.visibility_of_element_located(locator))
        except TimeoutException:
            self.get_screen()
            self.logger.error(f"The element is not found {locator}")
            raise AssertionError(f"The element is not found {locator}")

    def check_elements(self, locator: tuple):
        try:
            self.logger.info(f"Checking elements: {locator}")
            return WebDriverWait(self.driver, 10).until(EC.visibility_of_all_elements_located(locator))
        except TimeoutException:
            self.get_screen()
            self.logger.error(f"The elements are not found {locator}")
            raise AssertionError(f"The elements are not found {locator}")

    def check_text(self, locator: tuple, text: str):
        try:
            self.logger.info(f"Checking text '{text}' is present in {locator}")
            return WebDriverWait(self.driver, 5).until(EC.text_to_be_present_in_element(locator, text))
        except TimeoutException:
            self.get_screen()
            self.logger.error(f"Text '{text}' is not as we expected in the element {locator}")
            raise AssertionError(f"The {text} in the element not found {locator}")

    def click_element(self, locator: tuple):
        try:
            self.logger.info(f"Click element: {locator}")
            return WebDriverWait(self.driver, 8).until(EC.visibility_of_element_located(locator)).click()
        except TimeoutException:
            self.get_screen()
            self.logger.error(f"The element is not found {locator}")
            raise AssertionError(f"The element is not found {locator}")

    def input_value(self, locator: tuple, value: tuple):
        try:
            self.logger.info(f"Paste {value} into {locator}")
            return WebDriverWait(self.driver, 8).until(EC.visibility_of_element_located(locator)).send_keys(value)
        except TimeoutException:
            self.get_screen()
            self.logger.error(f"The element is not found {locator}")
            raise AssertionError(f"The element is not found {locator}")

    def alert(self, locator: tuple):
        try:
            self.logger.info("Alert has shown")
            WebDriverWait(self.driver, 5).until(EC.alert_is_present())
            self.logger.info("Alert accepted")
            self.driver.switch_to.alert.accept()
            self.logger.info(f"Check delete confirmation in the element: {locator}")
            WebDriverWait(self.driver, 5).until(EC.visibility_of_element_located(locator))
        except TimeoutException:
            self.get_screen()
            self.logger.error(f"Delete confirmation ( {locator} )is not found")
            raise AssertionError(f"Delete confirmation ( {locator} )is not found")
