import allure
from selenium.webdriver.common.by import By
from pages.base_page import BasePage


class MainPage(BasePage):
    FIRST_SLIDE = (By.CSS_SELECTOR, '#slideshow0 div[class*=swiper-slide-active]')
    SECOND_SLIDE = (By.CSS_SELECTOR, '#slideshow0 div[class*=slide-duplicate-next]')
    HEADER = (By.CSS_SELECTOR, '#content h3')
    TEXT_IN_HEADER = 'Featured'
    FEATURED_PRODUCTS = (By.CSS_SELECTOR, 'div[class*=product-layout]')
    LOWER_CAROUSEL_BULLETS = (By.CSS_SELECTOR, 'div[class*=carousel0] span:nth-child(n)')

    @allure.step("Check top slider")
    def verify_elements_slider(self):
        self.check_element(self.FIRST_SLIDE)
        self.check_element(self.SECOND_SLIDE)

    @allure.step("Check other elements")
    def verify_elements(self):
        self.check_text(self.HEADER, self.TEXT_IN_HEADER)
        self.check_elements(self.FEATURED_PRODUCTS)
        self.check_elements(self.LOWER_CAROUSEL_BULLETS)
