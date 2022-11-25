import allure
import pages.constants_admin_pages


@allure.step("Removing required object")
def remove_object(base_page):
    with allure.step("Chose object"):
        base_page.click_element(pages.constants_admin_pages.CHECKBOX)
    with allure.step("Press delete button"):
        base_page.click_element(pages.constants_admin_pages.DELETE_BUTTON)
    with allure.step("Confirm deletion"):
        base_page.alert(pages.constants_admin_pages.DELETE_CONFIRMATION)


@allure.step("Find required object")
def find_object(base_page, name):
    with allure.step(f"Paste {name} into name field"):
        base_page.input_value(pages.constants_admin_pages.NAME_FIELD, name)
    with allure.step("Click filter button"):
        base_page.click_element(pages.constants_admin_pages.FILTER)


@allure.step("Find required section ")
def go_to_page_in_admin_panel(base_page, button, inner_button):
    with allure.step(f"Click button {button} in navbar"):
        base_page.click_element(button)
    with allure.step(f"Click inner button {inner_button}"):
        base_page.click_element(inner_button)
