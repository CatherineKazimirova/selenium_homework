from selenium.webdriver.common.by import By
from pages.BasePage import BasePage


class CatalogPage(BasePage):
    LAPTOP_CATEGORY = (By.CSS_SELECTOR, 'li[class=dropdown] > a[href$="/laptop-notebook"]')
    LAPTOP_CATEGORY_DROPDOWN = (By.CSS_SELECTOR, 'div[class=dropdown-menu] a[href$="/laptop-notebook"]')
    LIST_VIEW_BUTTON = (By.CSS_SELECTOR, '#list-view')
    GRID_VIEW_BUTTON = (By.CSS_SELECTOR, '#grid-view')
    COMPARE_LINK = (By.CSS_SELECTOR, '#compare-total')
    SORT_DROPDOWN = (By.CSS_SELECTOR, '#input-sort')
    SORT_DROPDOWN_LIST = (By.CSS_SELECTOR, '#input-sort > option:nth-child(n)')
    SHOW_DROPDOWN = (By.CSS_SELECTOR, '#input-limit')
    SHOW_DROPDOWN_LIST = (By.CSS_SELECTOR, '#input-limit > option:nth-child(n)')

    def go_to_category_page(self):
        self.element(self.LAPTOP_CATEGORY).click()
        self.element(self.LAPTOP_CATEGORY_DROPDOWN).click()

    def verify_elements(self):
        self.element(self.LIST_VIEW_BUTTON)
        self.element(self.GRID_VIEW_BUTTON)
        self.element(self.COMPARE_LINK)
        self.element(self.SORT_DROPDOWN).click()
        self.elements(self.SORT_DROPDOWN_LIST)
        self.element(self.SHOW_DROPDOWN).click()
        self.elements(self.SHOW_DROPDOWN_LIST)
