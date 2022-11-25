import allure
from selenium.webdriver.common.by import By
from pages.base_page import BasePage


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

    @allure.step("Open category page")
    def go_to_category_page(self):
        with allure.step("Click category button in header"):
            self.click_element(self.LAPTOP_CATEGORY)
        with allure.step("Chose category in dropdown menu"):
            self.click_element(self.LAPTOP_CATEGORY_DROPDOWN)

    @allure.step("Check elements on catalog page")
    def verify_elements(self):
        self.check_element(self.LIST_VIEW_BUTTON)
        self.check_element(self.GRID_VIEW_BUTTON)
        self.check_element(self.COMPARE_LINK)
        self.check_element(self.SORT_DROPDOWN).click()
        self.check_elements(self.SORT_DROPDOWN_LIST)
        self.check_element(self.SHOW_DROPDOWN).click()
        self.check_elements(self.SHOW_DROPDOWN_LIST)
