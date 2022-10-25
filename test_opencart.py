from pages import constantsAdminPages
from pages.MainPage import MainPage
from pages.CatalogPage import CatalogPage
from pages.RegistrationPage import RegistrationPage
from pages.ProductPage import ProductPage
from pages.LoginPage import LoginPage
from pages.AdminPoductsPage import AdminProductsPage
from pages.Header import Header
from pages.AdminPanel import AdminPanel
from pages.sharedAdminPagesFunctions import remove_object
from pages.sharedAdminPagesFunctions import find_object
from pages.sharedAdminPagesFunctions import go_to_page_in_admin_panel


def test_main(browser):
    # Проверка элементов
    MainPage(browser).verify_elements()


def test_catalog(browser):
    # Переход на страницу категории
    CatalogPage(browser).go_to_category_page()
    # Проверка элементов
    CatalogPage(browser).verify_elements()


def test_product_card(browser):
    # Переход на страницу категории, а затем в карточку товара
    CatalogPage(browser).go_to_category_page()
    ProductPage(browser).go_to_product_page()
    # Проверка элементов
    ProductPage(browser).verify_elements()


def test_registration_page(browser):
    # Переход на страницу регистрации
    Header(browser).go_to_registration_page()
    # Проверка элементов
    RegistrationPage(browser).verify_validation_errors()


def test_login(browser):
    # Переход на страницу авторизации
    Header(browser).go_to_login_page()
    # Проверка элементов
    LoginPage(browser).verify_elements()


def test_user_create_delete(browser):
    # Переход на страницу регистрации
    Header(browser).go_to_registration_page()
    # Создаем аккаунт
    RegistrationPage(browser).registration()
    # Заходим под админом
    browser.get(url=browser.base_url + AdminPanel.url)
    AdminPanel(browser).login()
    # Удаляем аккаунт
    go_to_page_in_admin_panel(AdminPanel(browser), constantsAdminPages.CUSTOMERS_BUTTON, constantsAdminPages.CUSTOMERS_INNER_BUTTON)
    find_object(AdminPanel(browser), constantsAdminPages.CUSTOMER_NAME)
    remove_object(AdminPanel(browser))


def test_product_create_delete(browser):
    # Заходим под админом
    browser.get(url=browser.base_url + AdminPanel.url)
    AdminPanel(browser).login()
    # Создаем товар
    go_to_page_in_admin_panel(AdminPanel(browser), constantsAdminPages.PRODUCTS_BUTTON,
                              constantsAdminPages.PRODUCTS_INNER_BUTTON)
    AdminProductsPage(browser).add_new_product()
    # Удаляем товар
    find_object(AdminPanel(browser), constantsAdminPages.PRODUCT_NAME)
    remove_object(AdminPanel(browser))


def test_currency_change(browser):
    # Проверка переключения валют
    Header(browser).change_currency()
