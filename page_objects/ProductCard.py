from selenium.webdriver.common.by import By
from page_objects.BasePage import BasePage


class ProductCard(BasePage):
    DESCRIPTION = (By.CSS_SELECTOR, "a[href^='#tab-description']")
    REVIEW = (By.CSS_SELECTOR, "a[href^='#tab-review']")
    INPUT_QUANTITY = (By.NAME, "quantity")
    BUTTON_CART = (By.CSS_SELECTOR, "[id~=button-cart]")
    COMPARE_PRODUCT = (By.CSS_SELECTOR, "[data-original-title~=Compare]")
