import random

from selenium.webdriver.common.by import By
from page_objects.BasePage import BasePage


class MainPage(BasePage):
    PATH = "/index.php?route=common/home"
    LOGO = (By.ID, "logo")
    SEARCH_INPUT = (By.NAME, "search")
    DESKTOPS_BTN = (By.CSS_SELECTOR, "#menu > div > ul > li:nth-child(1)")
    SHOPPING_CART = (By.CSS_SELECTOR, "#cart")
    LAPTOP = (By.CSS_SELECTOR, "[title~=MacBook]")
    SWIPER = (By.CSS_SELECTOR, ".swiper-slide-duplicate.swiper-slide-active > a")
    CURRENCY = (By.CSS_SELECTOR, "#form-currency")
    LIST_CURRENCY = (By.CSS_SELECTOR, ".currency-select")
    # алерт есть на каждой странице
    ALERT = (By.CSS_SELECTOR, ".alert-success")
    CLOSE = (By.CSS_SELECTOR, "[data-dismiss~=alert]")

    def choose_currency(self):
        self.click(self.element_is_visible(self.CURRENCY))
        all_currency = self.elements_are_visible(self.LIST_CURRENCY)
        random_currency = random.choice(all_currency).text
        return random_currency
