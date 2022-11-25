from selenium.webdriver.common.by import By
import users
import products

CHECKBOX = (By.CSS_SELECTOR, "tbody input[type=checkbox]")
DELETE_BUTTON = (By.CSS_SELECTOR, "[data-original-title='Delete']")
NAME_FIELD = (By.CSS_SELECTOR, "#input-name")
CUSTOMER_NAME = users.user["name"] + ' ' + users.user["lastname"]
PRODUCT_NAME = products.product['name']
CUSTOMERS_BUTTON = (By.CSS_SELECTOR, "#menu-customer")
CUSTOMERS_INNER_BUTTON = (By.CSS_SELECTOR, "#collapse5 a[href*='customer/customer&']")
PRODUCTS_BUTTON = (By.CSS_SELECTOR, "#menu-catalog")
PRODUCTS_INNER_BUTTON = (By.CSS_SELECTOR, "#collapse1 a[href*='catalog/product&']")
FILTER = (By.CSS_SELECTOR, "#button-filter")
DELETE_CONFIRMATION = (By.CSS_SELECTOR, "div[class*=alert-success]")
