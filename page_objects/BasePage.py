import time
import logging

import allure
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By

from selenium.common.exceptions import TimeoutException
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


# logger = logging.getLogger(__name__)
# logger.setLevel('DEBUG')
# print(logger.level)

class BasePage:
    def __init__(self, driver, timeout=5):
        self.driver = driver
        self.wait = WebDriverWait(driver, timeout)
        self.actions = ActionChains(driver)
        self.logger = logging.getLogger(type(self).__name__)
        file_handler = logging.FileHandler(f'{__name__}.log')
        file_handler.setFormatter(logging.Formatter('%(name)s - %(levelname)s - %(message)s'))
        self.logger.addHandler(file_handler)

    @allure.step("Открываю эндпоинт {path}")
    def open(self, path):
        self.logger.info("Открыли страницу: {}".format(self.driver.url + path))
        self.driver.get(self.driver.url + path)

    @allure.step("Выполняю клик по элементу {element}")
    def click(self, element):
        self.logger.info("Нажали на элемент: {}".format(element))
        self.actions.move_to_element(element).pause(0.1).click().perform()

    @allure.step("Выполняю ввод {value} в элементе {element}")
    def _input(self, element, value):
        self.logger.info("Значение {} в окне ввода {}".format(value, element))
        self.click(element)
        element.clear()
        element.send_keys(value)

    def element_in_element(self, parent_locator: tuple, child_locator: tuple):
        return self.element_in_element(parent_locator).find_element(*child_locator)

    @allure.step("Нахожу элемент {locator}")
    def element_is_visible(self, locator: tuple):
        try:
            return self.wait.until(EC.visibility_of_element_located(locator))
        except TimeoutException:
            allure.attach(
                body=self.driver.get_screenshot_as_png(),
                name="screenshot_image",
                attachment_type=allure.attachment_type.PNG
            )
            self.logger.error("Элемент {} НЕ существует".format(locator))
            raise AssertionError(f"Не дождался видимости элемента {locator}")

    @allure.step("Нахожу элементы {locator}")
    def elements_are_visible(self, locator: tuple):
        try:
            return self.wait.until(EC.visibility_of_all_elements_located(locator))
        except TimeoutException:
            allure.attach(
                body=self.driver.get_screenshot_as_png(),
                name="screenshot_image",
                attachment_type=allure.attachment_type.PNG
            )
            self.logger.error("Элементы {} НЕ существует".format(locator))
            raise AssertionError(f"Не дождался видимости элементов {locator}")

    @allure.step("Проверили товар {product_name}")
    def verify_product_item(self, product_name):
        self.logger.info("Проверили товар: {}".format(product_name))
        return self.element((By.LINK_TEXT, product_name))

    @allure.step("Закрыли алерт")
    def alert_accept(self):
        self.logger.info("Тут был алерт!")
        alert = self.wait.until(EC.alert_is_present())
        alert.accept()
        time.sleep(1)
