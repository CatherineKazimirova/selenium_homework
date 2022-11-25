import allure
from selenium.webdriver.common.by import By
from pages.base_page import BasePage
import products


class AdminProductsPage(BasePage):
    ADD_BUTTON = (By.CSS_SELECTOR, "[data-original-title='Add New']")
    PRODUCT_NAME_FIELD = (By.CSS_SELECTOR, "#input-name1")
    TAG_TITLE_FIELD = (By.CSS_SELECTOR, "#input-meta-title1")
    TAB_DATA = (By.CSS_SELECTOR, "a[href='#tab-data']")
    MODEL_FIELD = (By.CSS_SELECTOR, "#input-model")
    SAVE_BUTTON = (By.CSS_SELECTOR, "[data-original-title='Save']")
    NAME = products.product['name']
    TAG_TITLE = products.product['tag-title']
    MODEL = products.product['model']

    @allure.step("Create new product")
    def add_new_product(self):
        with allure.step("Click '+' button"):
            self.click_element(self.ADD_BUTTON)
        with allure.step("Fill product name/tag fields"):
            self.input_value(self.PRODUCT_NAME_FIELD, self.NAME)
            self.input_value(self.TAG_TITLE_FIELD, self.TAG_TITLE)
        with allure.step("Choose Data tab"):
            self.click_element(self.TAB_DATA)
        with allure.step("Fill model field"):
            self.input_value(self.MODEL_FIELD, self.MODEL)
        with allure.step("Click Save button"):
            self.click_element(self.SAVE_BUTTON)
