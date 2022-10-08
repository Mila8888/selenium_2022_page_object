from selenium.webdriver.common.by import By
from page_objects.BasePage import BasePage


class DesktopsPage(BasePage):
    LIST_SHOW = (By.ID, "list-view")
    GRID_SHOW = (By.ID, "grid-view")
    SORT_BY = (By.ID, "input-sort")
    AMOUNT_LINES = (By.ID, "input-limit")
    WISH_LIST = (By.CSS_SELECTOR, "[data-original-title~=Wish]")
