import pages.constantsAdminPages


# Удаление товара или пользователя в админке
def remove_object(base_page):
    base_page.element(pages.constantsAdminPages.CHECKBOX).click()
    base_page.element(pages.constantsAdminPages.DELETE_BUTTON).click()
    base_page.alert(pages.constantsAdminPages.DELETE_CONFIRMATION)


# Поиск товара или пользователя в админке
def find_object(base_page, name):
    base_page.element(pages.constantsAdminPages.NAME_FIELD).send_keys(name)
    base_page.element(pages.constantsAdminPages.FILTER).click()


# Переход на страницу пользователя или товара в админке
def go_to_page_in_admin_panel(base_page, button, inner_button):
    base_page.element(button).click()
    base_page.element(inner_button).click()
