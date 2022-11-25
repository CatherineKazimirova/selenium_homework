import allure
from selenium.webdriver.common.by import By
from pages.base_page import BasePage


class ProductPage(BasePage):
    PRODUCT = (By.CSS_SELECTOR, 'div.row > div:nth-child(1) div.image')
    TAB_DESCRIPTION = (By.CSS_SELECTOR, '[href = "#tab-description"]')
    TAB_SPEC = (By.CSS_SELECTOR, '[href = "#tab-specification"]')
    TAB_REVIEW = (By.CSS_SELECTOR, '[href = "#tab-review"]')
    FAVORITE_BTN = (By.CSS_SELECTOR, '[data-original-title="Add to Wish List"]')
    COMPARE_BTN = (By.CSS_SELECTOR, '[data-original-title="Compare this Product"]')
    CART_BTN = (By.CSS_SELECTOR, 'div.form-group #button-cart')

    @allure.step("Choose the first product in category")
    def go_to_product_page(self):
        self.click_element(self.PRODUCT)

    @allure.step("Check product card elements")
    def verify_elements(self):
        self.check_element(self.TAB_DESCRIPTION)
        self.check_element(self.TAB_SPEC)
        self.check_element(self.TAB_REVIEW)
        self.check_element(self.FAVORITE_BTN)
        self.check_element(self.COMPARE_BTN)
        self.check_element(self.CART_BTN)
