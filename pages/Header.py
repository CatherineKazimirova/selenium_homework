from selenium.webdriver.common.by import By
from pages.BasePage import BasePage


class Header(BasePage):
    MY_ACCOUNT = (By.CSS_SELECTOR, 'a[title="My Account"]')
    LOGIN = (By.CSS_SELECTOR, 'ul[class*=dropdown-menu] a[href*=login]')
    REGISTRATION = (By.CSS_SELECTOR, 'ul[class*=dropdown-menu] a[href*=register]')
    CURRENCIES_BUTTON = (By.CSS_SELECTOR, '#form-currency')
    CURRENCY_SYMBOL_IN_HEADER = (By.CSS_SELECTOR, '#form-currency strong')
    EUR_BUTTON = (By.CSS_SELECTOR, 'button[name=EUR]')
    DOLLAR_BUTTON = (By.CSS_SELECTOR, 'button[name=EUR]')
    POUND_BUTTON = (By.CSS_SELECTOR, 'button[name=GBP]')

    def go_to_login_page(self):
        self.element(self.MY_ACCOUNT).click()
        self.element(self.LOGIN).click()

    def go_to_registration_page(self):
        self.element(self.MY_ACCOUNT).click()
        self.element(self.REGISTRATION).click()

    def change_currency(self):
        currencies = [self.EUR_BUTTON, self.DOLLAR_BUTTON, self.POUND_BUTTON]
        for el in currencies:
            self.element(self.CURRENCIES_BUTTON).click()
            currency_symbol = self.element(el).text
            self.element(el).click()
            currency_in_header_text = self.element(self.CURRENCY_SYMBOL_IN_HEADER).text
            assert currency_symbol[0] == currency_in_header_text
