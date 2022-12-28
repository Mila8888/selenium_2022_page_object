import datetime
import logging
import os

import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromiumService
from selenium.webdriver.firefox.service import Service as FFService


def pytest_addoption(parser):
    # Запуск из cmd -->  Пример: pytest -v --browser chrome
    parser.addoption("--browser", action="store", default="chrome")
    parser.addoption("--executor", action="store", default="192.168.2.123")
    parser.addoption("--mobile", action="store_true")
    parser.addoption("--vnc", action="store_true")
    parser.addoption("--logs", action="store_true")
    parser.addoption("--video", action="store_true")
    parser.addoption("--bv")
    parser.addoption("--headless", action="store_true", help="Без запуска браузера pytest --headless")
    parser.addoption("--url", action="store", default="http://192.168.2.123:8082")
    parser.addoption("--drivers", action="store", default=os.path.expanduser("~/Documents/drivers"))
    parser.addoption("--log_level", action="store", default="DEBUG")


@pytest.fixture
def driver(request):
    # Сбор параметров запуска для pytest
    browser = request.config.getoption("--browser")
    executor = request.config.getoption("--executor")
    version = request.config.getoption("--bv")
    vnc = request.config.getoption("--vnc")
    logs = request.config.getoption("--logs")
    video = request.config.getoption("--video")
    headless = request.config.getoption("--headless")
    url = request.config.getoption("--url")
    drivers = request.config.getoption("--drivers")
    log_level = request.config.getoption("--log_level")

    logger = logging.getLogger(request.node.name)
    file_handler = logging.FileHandler(f'{__name__}.log')
    file_handler.setFormatter(logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s'))
    logger.addHandler(file_handler)
    logger.setLevel(level=log_level)

    logger.info("===> Test {} started at {}".format(request.node.name, datetime.datetime.now()))

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

    executor_url = f"http://{executor}:4444/wd/hub"

    caps = {
        "browserName": browser,
        "browserVersion": version,
        "selenoid:options": {
            "enableVNC": vnc,
            "enableVideo": video,
            "enableLog": logs
        }
    }

    driver.log_level = log_level
    driver.logger = logger
    driver.test_name = request.node.name
    driver = webdriver.Remote(
        command_executor=executor_url,
        desired_capabilities=caps
    )

    driver.maximize_window()

    def fin():
        driver.quit()
        logger.info("===> Test {} finished at {}".format(request.node.name, datetime.datetime.now()))

    request.addfinalizer(fin)

    driver.get(url)
    driver.url = url

    return driver
