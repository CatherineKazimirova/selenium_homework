from selenium.webdriver.common.by import By
from pages.BasePage import BasePage
import credentials


class AdminPanel(BasePage):
    url = 'admin'
    USERNAME_FIELD = (By.CSS_SELECTOR, "#input-username")
    PASSWORD_FIELD = (By.CSS_SELECTOR, "#input-password")
    LOGIN_BUTTON = (By.CSS_SELECTOR, "button[type=submit]")
    LOGIN = credentials.admin["login"]
    PASSWORD = credentials.admin["password"]

    def login(self):
        self.element(self.USERNAME_FIELD).send_keys(self.LOGIN)
        self.element(self.PASSWORD_FIELD).send_keys(self.PASSWORD)
        self.element(self.LOGIN_BUTTON).send_keys(self.LOGIN_BUTTON)
