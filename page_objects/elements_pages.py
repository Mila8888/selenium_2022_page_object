from selenium.webdriver.common.by import By


class AdminPage:
    USERNAME = (By.CSS_SELECTOR, "#input-username")
    PASSWORD = (By.NAME, "password")
    FORGOTTEN_PASSWORD = (By.CSS_SELECTOR, "span > a[href$='route=common/forgotten']")
    LOGIN_BUTTON = (By.CSS_SELECTOR, "button[type='submit']")
    OPENCART_LINK = (By.XPATH, "//*[text()='OpenCart']")


class RegisterPage:
    FIRSTNAME = (By.CSS_SELECTOR, "#input-firstname")
    LASTNAME = (By.CSS_SELECTOR, "#input-lastname")
    EMAIL = (By.CSS_SELECTOR, "#input-email")
    TELEFONE = (By.CSS_SELECTOR, "#input-telephone")
    PASSWORD = (By.NAME, "password")
    CONFIRM_PASSWORD = (By.NAME, "confirm")
    CHECKBOX_AGREE = (By.NAME, "agree")
    CONTINUE_BTN = (By.CSS_SELECTOR, "input.btn.btn-primary")


class MainPage:
    LOGO = (By.ID, "logo")
    SEARCH_INPUT = (By.NAME, "search")
    DESKTOPS_BTN = (By.CSS_SELECTOR, "#menu > div > ul > li:nth-child(1)")
    SHOPPING_CART = (By.CSS_SELECTOR, "#cart")
    LAPTOP = (By.CSS_SELECTOR, "[title~=MacBook]")
    SWIPER = (By.CSS_SELECTOR, ".swiper-slide-duplicate.swiper-slide-active > a")
    # алерт есть на каждой странице
    ALERT = (By.CSS_SELECTOR, ".alert-success")
    CLOSE = (By.CSS_SELECTOR, "[data-dismiss~=alert]")


class DesktopsPage:
    LIST_SHOW = (By.ID, "list-view")
    GRID_SHOW = (By.ID, "grid-view")
    SORT_BY = (By.ID, "input-sort")
    AMOUNT_LINES = (By.ID, "input-limit")
    WISH_LIST = (By.CSS_SELECTOR, "[data-original-title~=Wish]")


class ProductCard:
    DESCRIPTION = (By.CSS_SELECTOR, "a[href^='#tab-description']")
    REVIEW = (By.CSS_SELECTOR, "a[href^='#tab-review']")
    INPUT_QUANTITY = (By.NAME, "quantity")
    BUTTON_CART = (By.CSS_SELECTOR, "[id~=button-cart]")
    COMPARE_PRODUCT = (By.CSS_SELECTOR, "[data-original-title~=Compare]")
