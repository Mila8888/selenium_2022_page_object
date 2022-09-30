from selenium.webdriver.common.by import By
from page_objects.BasePage import BasePage
from generator.generator import generated_person


class RegisterPage(BasePage):
    PATH = "/index.php?route=account/register"
    FIRSTNAME = (By.CSS_SELECTOR, "#input-firstname")
    LASTNAME = (By.CSS_SELECTOR, "#input-lastname")
    EMAIL = (By.CSS_SELECTOR, "#input-email")
    TELEFONE = (By.CSS_SELECTOR, "#input-telephone")
    PASSWORD = (By.NAME, "password")
    CONFIRM_PASSWORD = (By.NAME, "confirm")
    CHECKBOX_AGREE = (By.CSS_SELECTOR, ".col-sm-10 > label > input[value='1']")
    PRIVACY_POLICY = (By.CSS_SELECTOR, "input[type=checkbox]")
    CONTINUE_BTN = (By.CSS_SELECTOR, "input.btn.btn-primary")
    SUCCESS_CREAT_ACCOUNT = (By.CSS_SELECTOR, "#common-success > ul > li > a[href$='success']")
    TEXT_SUCCESS = (By.CSS_SELECTOR, "#content > h1")

    def register(self):
        person = generated_person()
        self._input(self.element_is_visible(self.FIRSTNAME), person.first_name)
        self._input(self.element_is_visible(self.LASTNAME), person.last_name)
        self._input(self.element_is_visible(self.EMAIL), person.email)
        self._input(self.element_is_visible(self.TELEFONE), person.phone_number)
        self._input(self.element_is_visible(self.PASSWORD), person.password)
        self._input(self.element_is_visible(self.CONFIRM_PASSWORD), person.password)
        self.click(self.element_is_visible(self.CHECKBOX_AGREE))
        self.click(self.element_is_visible(self.PRIVACY_POLICY))
        self.click(self.element_is_visible(self.CONTINUE_BTN))
        return self

    def page_creat_account(self):
        self.element_is_visible(self.SUCCESS_CREAT_ACCOUNT)
        result_text = self.element_is_visible(self.TEXT_SUCCESS).text
        return result_text
