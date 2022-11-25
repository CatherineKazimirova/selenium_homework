from selenium.webdriver.common.by import By
from pages.base_page import BasePage
import credentials
import allure


class AdminPanel(BasePage):
    url = 'admin'
    USERNAME_FIELD = (By.CSS_SELECTOR, "#input-username")
    PASSWORD_FIELD = (By.CSS_SELECTOR, "#input-password")
    LOGIN_BUTTON = (By.CSS_SELECTOR, "button[type=submit]")
    LOGIN = credentials.admin["login"]
    PASSWORD = credentials.admin["password"]

    @allure.step("Login as admin")
    def login(self):
        with allure.step("Paste login into username field"):
            self.input_value(self.USERNAME_FIELD, self.LOGIN)
        with allure.step("Paste password into password field"):
            self.input_value(self.PASSWORD_FIELD, self.PASSWORD)
        with allure.step("Press login button"):
            self.click_element(self.LOGIN_BUTTON)
