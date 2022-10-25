from selenium.webdriver.common.by import By
from pages.BasePage import BasePage


class MainPage(BasePage):
    FIRST_SLIDE = (By.CSS_SELECTOR, '#slideshow0 div[class*=swiper-slide-active]')
    SECOND_SLIDE = (By.CSS_SELECTOR, '#slideshow0 div[class*=slide-duplicate-next]')
    HEADER = (By.CSS_SELECTOR, '#content h3')
    TEXT_IN_HEADER = 'Featured'
    FEATURED_PRODUCTS = (By.CSS_SELECTOR, 'div[class*=product-layout]')
    LOWER_CAROUSEL_BULLETS = (By.CSS_SELECTOR, 'div[class*=carousel0] span:nth-child(n)')

    def verify_elements(self):
        self.element(self.FIRST_SLIDE)
        self.element(self.SECOND_SLIDE)
        self.text(self.HEADER, self.TEXT_IN_HEADER)
        self.elements(self.FEATURED_PRODUCTS)
        self.elements(self.LOWER_CAROUSEL_BULLETS)
