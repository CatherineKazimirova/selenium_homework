from selenium.webdriver.common.by import By
from pages.base_page import BasePage
import allure


class Header(BasePage):
    MY_ACCOUNT = (By.CSS_SELECTOR, 'a[title="My Account"]')
    LOGIN = (By.CSS_SELECTOR, 'ul[class*=dropdown-menu] a[href*=login]')
    REGISTRATION = (By.CSS_SELECTOR, 'ul[class*=dropdown-menu] a[href*=register]')
    CURRENCIES_BUTTON = (By.CSS_SELECTOR, '#form-currency')
    CURRENCY_SYMBOL_IN_HEADER = (By.CSS_SELECTOR, '#form-currency strong')
    EUR_BUTTON = (By.CSS_SELECTOR, 'button[name=USD]')
    DOLLAR_BUTTON = (By.CSS_SELECTOR, 'button[name=EUR]')
    POUND_BUTTON = (By.CSS_SELECTOR, 'button[name=GBP]')

    @allure.step("Open login page")
    def go_to_login_page(self):
        with allure.step("Click my account button in header"):
            self.check_element(self.MY_ACCOUNT).click()
        with allure.step("Choose login option in dropdown menu"):
            self.check_element(self.LOGIN).click()

    @allure.step("Open registration page")
    def go_to_registration_page(self):
        with allure.step("Choose login option in dropdown menu"):
            self.click_element(self.MY_ACCOUNT)
        with allure.step("Choose registration option in dropdown menu"):
            self.click_element(self.REGISTRATION)

    @allure.step("Pick currency")
    def change_currency(self):
        currencies = [self.EUR_BUTTON, self.DOLLAR_BUTTON, self.POUND_BUTTON]
        for el in currencies:
            with allure.step(f"Pick currency {el}"):
                self.click_element(self.CURRENCIES_BUTTON)
                currency_symbol = self.check_element(el).text
                self.click_element(el)
                currency_in_header_text = self.check_element(self.CURRENCY_SYMBOL_IN_HEADER).text
                assert currency_symbol[0] == currency_in_header_text
