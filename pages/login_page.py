import allure
from selenium.webdriver.common.by import By
from pages.base_page import BasePage


class LoginPage(BasePage):
    HEADER = (By.CSS_SELECTOR, '#content div:nth-child(2) h2')
    HEADER_TEXT = 'Returning 1111Customer'
    SECOND_HEADER = (By.CSS_SELECTOR, '#content div:nth-child(2) p strong')
    SECOND_HEADER_TEXT = 'I am a returning customer'
    EMAIL = (By.CSS_SELECTOR, '#input-email')
    PASSWORD = (By.CSS_SELECTOR, '#input-password')
    LOGIN_BUTTON = (By.CSS_SELECTOR, 'input[type=submit]')

    @allure.step("Check login page elements")
    def verify_elements(self):
        self.check_text(self.HEADER, self.HEADER_TEXT)
        self.check_text(self.SECOND_HEADER, self.SECOND_HEADER_TEXT)
        self.check_element(self.EMAIL)
        self.check_element(self.PASSWORD)
        self.check_element(self.LOGIN_BUTTON)
