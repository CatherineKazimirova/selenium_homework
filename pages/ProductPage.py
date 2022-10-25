from selenium.webdriver.common.by import By
from pages.BasePage import BasePage


class ProductPage(BasePage):
    PRODUCT = (By.CSS_SELECTOR, 'div.row > div:nth-child(1) div.image')
    TAB_DESCRIPTION = (By.CSS_SELECTOR, '[href = "#tab-description"]')
    TAB_SPEC = (By.CSS_SELECTOR, '[href = "#tab-specification"]')
    TAB_REVIEW = (By.CSS_SELECTOR, '[href = "#tab-review"]')
    FAVORITE_BTN = (By.CSS_SELECTOR, '[data-original-title="Add to Wish List"]')
    COMPARE_BTN = (By.CSS_SELECTOR, '[data-original-title="Compare this Product"]')
    CART_BTN = (By.CSS_SELECTOR, '#button-cart')

    def go_to_product_page(self):
        self.element(self.PRODUCT).click()

    def verify_elements(self):
        self.element(self.TAB_DESCRIPTION)
        self.element(self.TAB_SPEC)
        self.element(self.TAB_REVIEW)
        self.element(self.FAVORITE_BTN)
        self.element(self.COMPARE_BTN)
        self.element(self.CART_BTN)
