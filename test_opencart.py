import allure
import pytest
from pages import constants_admin_pages
from pages.main_page import MainPage
from pages.catalog_page import CatalogPage
from pages.registration_page import RegistrationPage
from pages.product_page import ProductPage
from pages.login_page import LoginPage
from pages.admin_products_page import AdminProductsPage
from pages.header import Header
from pages.admin_panel import AdminPanel
from pages.shared_admin_pages_functions import remove_object
from pages.shared_admin_pages_functions import find_object
from pages.shared_admin_pages_functions import go_to_page_in_admin_panel


@pytest.mark.skip(reason="Incorrect test, will fix later")
@allure.feature('Checking elements')
@allure.severity(allure.severity_level.MINOR)
@allure.title('Checking elements on the main page')
def test_main(browser):
    MainPage(browser).verify_elements_slider()
    MainPage(browser).verify_elements()


@allure.feature('Checking elements')
@allure.severity(allure.severity_level.MINOR)
@allure.title('Checking elements on the category page')
def test_catalog(browser):
    CatalogPage(browser).go_to_category_page()
    CatalogPage(browser).verify_elements()


@allure.feature('Checking elements')
@allure.severity(allure.severity_level.CRITICAL)
@allure.title('Checking elements on the product card')
def test_product_card(browser):
    CatalogPage(browser).go_to_category_page()
    ProductPage(browser).go_to_product_page()
    ProductPage(browser).verify_elements()


@allure.feature('Checking elements')
@allure.severity(allure.severity_level.NORMAL)
@allure.title('Checking validation errors on registration form')
def test_registration_page(browser):
    Header(browser).go_to_registration_page()
    RegistrationPage(browser).verify_validation_errors()


@allure.feature('Checking elements')
@allure.severity(allure.severity_level.NORMAL)
@allure.title('Checking elements on login form')
def test_login(browser):
    Header(browser).go_to_login_page()
    LoginPage(browser).verify_elements()


@allure.feature('Test registration')
@allure.severity(allure.severity_level.CRITICAL)
@allure.title('User registration and deletion')
def test_user_create_delete(browser):
    Header(browser).go_to_registration_page()
    RegistrationPage(browser).registration()
    browser.get(url=browser.base_url + AdminPanel.url)
    AdminPanel(browser).login()
    go_to_page_in_admin_panel(AdminPanel(browser), constants_admin_pages.CUSTOMERS_BUTTON,
                              constants_admin_pages.CUSTOMERS_INNER_BUTTON)
    find_object(AdminPanel(browser), constants_admin_pages.CUSTOMER_NAME)
    remove_object(AdminPanel(browser))


@allure.feature('Test product creation')
@allure.severity(allure.severity_level.NORMAL)
@allure.title('Product creation and deletion')
def test_product_create_delete(browser):
    browser.get(url=browser.base_url + AdminPanel.url)
    AdminPanel(browser).login()
    go_to_page_in_admin_panel(AdminPanel(browser), constants_admin_pages.PRODUCTS_BUTTON,
                              constants_admin_pages.PRODUCTS_INNER_BUTTON)
    AdminProductsPage(browser).add_new_product()
    find_object(AdminPanel(browser), constants_admin_pages.PRODUCT_NAME)
    remove_object(AdminPanel(browser))


@allure.feature('Test choosing currency')
@allure.severity(allure.severity_level.NORMAL)
@allure.title('Choosing each currency')
def test_currency_change(browser):
    Header(browser).change_currency()
