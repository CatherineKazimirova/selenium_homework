from selenium.webdriver.common.by import By
from pages.BasePage import BasePage
import users


class RegistrationPage(BasePage):
    NAME_FIELD = (By.CSS_SELECTOR, '#input-firstname')
    LASTNAME_FIELD = (By.CSS_SELECTOR, '#input-lastname')
    EMAIL_FIELD = (By.CSS_SELECTOR, '#input-email')
    TELEPHONE_FIELD = (By.CSS_SELECTOR, '#input-telephone')
    PASSWORD_FIELD = (By.CSS_SELECTOR, '#input-password')
    CONFIRM_PASSWORD_FIELD = (By.CSS_SELECTOR, '#input-confirm')
    AGREEMENT_CHECKBOX = (By.CSS_SELECTOR, 'input[type=checkbox]')
    CONTINUE_BUTTON = (By.CSS_SELECTOR, 'input[value=Continue]')
    FIRST_NAME_ERROR = (By.CSS_SELECTOR, '#account div:nth-child(3) div.text-danger')
    FIRST_NAME_TEXT = 'First Name must be between 1 and 32 characters!'
    LAST_NAME_ERROR = (By.CSS_SELECTOR, '#account div:nth-child(4) div.text-danger')
    LAST_NAME_TEXT = 'Last Name must be between 1 and 32 characters!'
    EMAIL_ERROR = (By.CSS_SELECTOR, '#account div:nth-child(5) div.text-danger')
    EMAIL_TEXT = 'E-Mail Address does not appear to be valid!'
    TELEPHONE_ERROR = (By.CSS_SELECTOR, '#account div:nth-child(6) div.text-danger')
    TELEPHONE_TEXT = 'Telephone must be between 3 and 32 characters!'
    ACC_CREATED_HEADER = (By.CSS_SELECTOR, '#content h1')
    ACC_CREATED_TEXT = 'Your Account Has Been Created!'

    def verify_validation_errors(self):
        self.element(self.CONTINUE_BUTTON).click()
        self.text(self.FIRST_NAME_ERROR, self.FIRST_NAME_TEXT)
        self.text(self.LAST_NAME_ERROR, self.LAST_NAME_TEXT)
        self.text(self.EMAIL_ERROR, self.EMAIL_TEXT)
        self.text(self.TELEPHONE_ERROR, self.TELEPHONE_TEXT)

    def registration(self):
        self.element(self.NAME_FIELD).send_keys(users.user["name"])
        self.element(self.LASTNAME_FIELD).send_keys(users.user["lastname"])
        self.element(self.EMAIL_FIELD).send_keys(users.user["email"])
        self.element(self.TELEPHONE_FIELD).send_keys(users.user["phone"])
        self.element(self.PASSWORD_FIELD).send_keys(users.user["password"])
        self.element(self.CONFIRM_PASSWORD_FIELD).send_keys(users.user["password"])
        self.element(self.AGREEMENT_CHECKBOX).click()
        self.element(self.CONTINUE_BUTTON).click()
        self.text(self.ACC_CREATED_HEADER, self.ACC_CREATED_TEXT)
