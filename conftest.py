import datetime
import logging
import os

import pytest
from selenium import webdriver


def pytest_addoption(parser):
    # Запуск из cmd -->  Пример: pytest -v --browser chrome
    parser.addoption("--browser", action="store", default="chrome")
    parser.addoption("--executor", action="store", default='192.168.177.208')
    parser.addoption("--mobile", action="store_true")
    parser.addoption("--vnc", action="store_true")
    parser.addoption("--logs", action="store_true")
    parser.addoption("--video", action="store_true")
    parser.addoption("--bv")
    parser.addoption("--headless", action="store_true", help="Без запуска браузера pytest --headless")
    parser.addoption("--url", action="store", default="http://192.168.177.208:8082")
    parser.addoption("--drivers", action="store")
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
    url = request.config.getoption("--url")
    log_level = request.config.getoption("--log_level")

    logger = logging.getLogger(request.node.name)
    file_handler = logging.FileHandler(f'{__name__}.log')
    file_handler.setFormatter(logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s'))
    logger.addHandler(file_handler)
    logger.setLevel(level=log_level)

    logger.info("===> Test {} started at {}".format(request.node.name, datetime.datetime.now()))

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

    driver = webdriver.Remote(
        command_executor=executor_url,
        desired_capabilities=caps
    )

    driver.log_level = log_level
    driver.logger = logger
    driver.test_name = request.node.name

    driver.maximize_window()

    def fin():
        driver.quit()
        logger.info("===> Test {} finished at {}".format(request.node.name, datetime.datetime.now()))

    request.addfinalizer(fin)

    driver.get(url)
    driver.url = url

    return driver
