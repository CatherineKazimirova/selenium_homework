import allure
from selenium.webdriver.common.by import By
from pages.base_page import BasePage
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

    @allure.step("Check validation errors in registration form")
    def verify_validation_errors(self):
        with allure.step("Click continue button without filling the form"):
            self.click_element(self.CONTINUE_BUTTON)
        with allure.step("Check validation errors"):
            self.check_text(self.FIRST_NAME_ERROR, self.FIRST_NAME_TEXT)
            self.check_text(self.LAST_NAME_ERROR, self.LAST_NAME_TEXT)
            self.check_text(self.EMAIL_ERROR, self.EMAIL_TEXT)
            self.check_text(self.TELEPHONE_ERROR, self.TELEPHONE_TEXT)

    @allure.step("New user registration")
    def registration(self):
        with allure.step("Fill mandatory fields"):
            with allure.step("Name field"):
                self.input_value(self.NAME_FIELD, users.user["name"])
            with allure.step("Lastname field"):
                self.input_value(self.LASTNAME_FIELD, users.user["lastname"])
            with allure.step("Email field"):
                self.input_value(self.EMAIL_FIELD, users.user["email"])
            with allure.step("Phone field"):
                self.input_value(self.TELEPHONE_FIELD, users.user["phone"])
            with allure.step("Password field"):
                self.input_value(self.PASSWORD_FIELD, users.user["password"])
            with allure.step("Confirm password field"):
                self.input_value(self.CONFIRM_PASSWORD_FIELD, users.user["password"])
        with allure.step("Accept privacy policy"):
            self.click_element(self.AGREEMENT_CHECKBOX)
        with allure.step("Click continue button"):
            self.click_element(self.CONTINUE_BUTTON)
        with allure.step("Check confirmation of registration on the next page"):
            self.check_text(self.ACC_CREATED_HEADER, self.ACC_CREATED_TEXT)
