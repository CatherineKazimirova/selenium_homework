from selenium.webdriver.common.by import By
from pages.BasePage import BasePage
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

    def add_new_product(self):
        self.element(self.ADD_BUTTON).click()
        self.element(self.PRODUCT_NAME_FIELD).send_keys(self.NAME)
        self.element(self.TAG_TITLE_FIELD).send_keys(self.TAG_TITLE)
        self.element(self.TAB_DATA).click()
        self.element(self.MODEL_FIELD).send_keys(self.MODEL)
        self.element(self.SAVE_BUTTON).click()
