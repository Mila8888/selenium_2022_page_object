from page_objects import *
from page_objects.wait import wait_element


def test_login_page_external(driver):
    driver.get(driver.url + "/admin")
    driver.find_element(*AdminPage.USERNAME)
    driver.find_element(*AdminPage.PASSWORD)
    driver.find_element(*AdminPage.FORGOTTEN_PASSWORD)
    driver.find_element(*AdminPage.LOGIN_BUTTON)
    driver.find_element(*AdminPage.OPENCART_LINK)


def test_register_page_external(driver):
    driver.get(driver.url + "/index.php?route=account/register")
    driver.find_element(*RegisterPage.FIRSTNAME)
    driver.find_element(*RegisterPage.LASTNAME)
    driver.find_element(*RegisterPage.EMAIL)
    driver.find_element(*RegisterPage.TELEFONE)
    driver.find_element(*RegisterPage.PASSWORD)
    driver.find_element(*RegisterPage.CONFIRM_PASSWORD)
    driver.find_element(*RegisterPage.CHECKBOX_AGREE)
    driver.find_element(*RegisterPage.CONTINUE_BTN)


def test_main_page(driver):
    driver.get(driver.url)
    driver.find_element(*MainPage.LOGO)
    driver.find_element(*MainPage.SEARCH_INPUT)
    driver.find_element(*MainPage.DESKTOPS_BTN)
    driver.find_element(*MainPage.SHOPPING_CART)
    driver.find_element(*MainPage.LAPTOP)


def test_desktops_page(driver):
    driver.get(driver.url + "/desktops")
    driver.find_element(*DesktopsPage.LIST_SHOW)
    driver.find_element(*DesktopsPage.GRID_SHOW)
    driver.find_element(*DesktopsPage.SORT_BY)
    driver.find_element(*DesktopsPage.AMOUNT_LINES)
    driver.find_element(*DesktopsPage.WISH_LIST)


def test_product_card_mac(driver):
    driver.get(driver.url + "/desktops/mac/imac")
    driver.find_element(*ProductCard.DESCRIPTION)
    driver.find_element(*ProductCard.REVIEW)
    driver.find_element(*ProductCard.INPUT_QUANTITY)
    driver.find_element(*ProductCard.COMPARE_PRODUCT)


def test_alert(driver):
    driver.get(driver.url + "/desktops/mac/imac")
    button_click = driver.find_element(*ProductCard.BUTTON_CART)
    button_click.click()
    wait_element(driver, MainPage.ALERT)
    driver.find_element(*MainPage.CLOSE).click()
