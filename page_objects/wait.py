from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.support.wait import WebDriverWait


def wait_element(driver,  selector, timeout=3):
    try:
        return WebDriverWait(driver=driver, timeout=timeout).until(EC.visibility_of_element_located(selector))
    except TimeoutException:
        raise AssertionError("Элемента не дождался: {}".format(selector))
