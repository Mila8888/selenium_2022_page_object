from selenium.webdriver.common.by import By
from page_objects.BasePage import BasePage


class AdminPage(BasePage):
    PATH = "/admin"
    # Поля для ввода данных для входа
    USERNAME = (By.ID, "input-username")
    PASSWORD = (By.NAME, "password")
    FORGOTTEN_PASSWORD = (By.CSS_SELECTOR, "span > a[href$='route=common/forgotten']")
    LOGIN_BUTTON = (By.CSS_SELECTOR, "button[type='submit']")
    OPENCART_LINK = (By.XPATH, "//*[text()='OpenCart']")
    # Раздел навигации
    MENU_NAVIGATION = (By.CSS_SELECTOR, "#menu")
    MENU_CATALOG = (By.CSS_SELECTOR, "#menu-catalog")
    PRODUCT_LIST = (By.CSS_SELECTOR, "#collapse1 > li > a[href*='product']")
    BTN_ADD_NEW = (By.CSS_SELECTOR, "i.fa-plus")
    BTN_DEL_NEW = (By.CSS_SELECTOR, "i.fa-trash-o") # Кнопка удаления

    #  Add Product - заполнение полей для новой карточки
    PRODUCT_NAME_IN_NEW_CART = (By.CSS_SELECTOR, "#input-name1") # for section general
    META_TAG_TITLE_IN_NEW_CART = (By.CSS_SELECTOR, "#input-meta-title1") # for section general
    DATA_IN_NEW_CART = (By.CSS_SELECTOR, "a[href='#tab-data']") # section data
    MODEL_IN_NEW_CART = (By.CSS_SELECTOR, "#input-model") # for section data
    BTN_SAVE_NEW_CART = (By.CSS_SELECTOR, "button[form=form-product]")

    # Список продуктов добавленных
    RESULT_NEW_PRODUCT = (By.XPATH, "//div[@class='table-responsive']//td[3]")
    CHECKBOX_PRODUCT = (By.CSS_SELECTOR, "input[type=checkbox]")
    NO_RESULT = (By.CSS_SELECTOR, "td[colspan='8']")

    # Поля фильтрации
    FILTER_PRODUCT_NAME = (By.CSS_SELECTOR, "input[name='filter_name']")
    BTN_FILTER = (By.CSS_SELECTOR, "div>#button-filter")

    def login(self, username, password):
        self._input(self.element_is_visible(self.USERNAME), username)
        self._input(self.element_is_visible(self.PASSWORD), password)
        self.click(self.element_is_visible(self.LOGIN_BUTTON))
        return self

    def choose_element_catalog_menu(self):
        self.click(self.element_is_visible(self.MENU_CATALOG))
        self.click(self.element_is_visible(self.PRODUCT_LIST))
        return self

    def add_new_product(self):
        name_product = 'last iPhone'
        model = 'Model LIPH'
        self.click(self.element_is_visible(self.BTN_ADD_NEW))
        self._input(self.element_is_visible(self.PRODUCT_NAME_IN_NEW_CART), name_product)
        self._input(self.element_is_visible(self.META_TAG_TITLE_IN_NEW_CART), 'iPhone_new')
        self.click(self.element_is_visible(self.DATA_IN_NEW_CART))
        self._input(self.element_is_visible(self.MODEL_IN_NEW_CART), model)
        self.click(self.element_is_visible(self.BTN_SAVE_NEW_CART))
        return name_product

    def form_result(self):
        result_cart = self.elements_are_visible(self.RESULT_NEW_PRODUCT)
        result_text = [i.text for i in result_cart]
        return result_text

    def serch_product(self, name_product):
        self._input(self.element_is_visible(self.FILTER_PRODUCT_NAME), name_product)
        self.click(self.element_is_visible(self.BTN_FILTER))
        return name_product

    def del_product(self):
        self.click(self.element_is_visible(self.CHECKBOX_PRODUCT))
        self.click(self.element_is_visible(self.BTN_DEL_NEW))
        self.alert_accept()
        text_result = self.element_is_visible(self.NO_RESULT).text
        return text_result
