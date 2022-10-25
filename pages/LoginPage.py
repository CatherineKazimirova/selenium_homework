from selenium.webdriver.common.by import By
from pages.BasePage import BasePage


class LoginPage(BasePage):
    HEADER = (By.CSS_SELECTOR, '#content div:nth-child(2) h2')
    HEADER_TEXT = 'Returning Customer'
    SECOND_HEADER = (By.CSS_SELECTOR, '#content div:nth-child(2) p strong')
    SECOND_HEADER_TEXT = 'I am a returning customer'
    EMAIL = (By.CSS_SELECTOR, '#input-email')
    PASSWORD = (By.CSS_SELECTOR, '#input-password')
    LOGIN_BUTTON = (By.CSS_SELECTOR, 'input[type=submit]')

    def verify_elements(self):
        self.text(self.HEADER, self.HEADER_TEXT)
        self.text(self.SECOND_HEADER, self.SECOND_HEADER_TEXT)
        self.element(self.EMAIL)
        self.element(self.PASSWORD)
        self.element(self.LOGIN_BUTTON)
