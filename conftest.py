import os

import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromiumService
from selenium.webdriver.firefox.service import Service as FFService


def pytest_addoption(parser):
    # Запуск из cmd -->  Пример: pytest -v --browser chrome
    parser.addoption("--browser", action="store", default="chrome")
    parser.addoption("--headless", action="store_true", help="Без запуска браузера pytest --headless")
    parser.addoption("--url", action="store", default="http://192.168.1.50:8082")
    parser.addoption("--drivers", action="store", default=os.path.expanduser("~/Documents/drivers"))


@pytest.fixture
def driver(request):
    # Сбор параметров запуска для pytest
    browser = request.config.getoption("--browser")
    headless = request.config.getoption("--headless")
    url = request.config.getoption("--url")
    drivers = request.config.getoption("--drivers")

    if browser == "chrome":
        options = webdriver.ChromeOptions()
        service = ChromiumService(executable_path=drivers + "/chromedriver")
        if headless:
            options.headless = True
        driver = webdriver.Chrome(service=service, options=options)
    elif browser == "firefox":
        service = FFService(executable_path=drivers + "/geckodriver")
        driver = webdriver.Firefox(service=service)
    elif browser == "opera":
        driver = webdriver.Opera(executable_path=drivers + "/operadriver")
    else:
        driver = webdriver.Safari()

    driver.maximize_window()

    request.addfinalizer(driver.close)

    driver.get(url)
    driver.url = url

    return driver
