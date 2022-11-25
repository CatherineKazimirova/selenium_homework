import datetime
from selenium.webdriver.firefox.service import Service as FirefoxService
from webdriver_manager.firefox import GeckoDriverManager
import logging
import os.path
from selenium import webdriver
import pytest

drivers = os.path.expanduser("~/drivers")
path_to_binary_location_opera = '/Applications/Opera.app/Contents/MacOS/Opera'


def pytest_addoption(parser):
    parser.addoption(
        "--url",
        default="http://192.168.0.6:8081/"
    )

    parser.addoption(
        "--browser",
        default="chrome"
    )

    parser.addoption(
        "--log_level",
        default="DEBUG"
    )

    parser.addoption(
        "--executor",
        default="192.168.0.6"
    )

    parser.addoption(
        "--browser_version"
    )

    parser.addoption(
        "--vnc",
        default=True
    )

    parser.addoption(
        "--video",
        default=False
    )

    parser.addoption(
        "--tester_name",
        default="Catherine"
    )

    parser.addoption(
        "--screen_resolution",
        default="1920x1080"
    )


@pytest.fixture
def browser(request):
    browser = request.config.getoption("--browser")
    base_url = request.config.getoption("--url")
    log_level = request.config.getoption("--log_level")
    executor = request.config.getoption("--executor")
    browser_version = request.config.getoption("--browser_version")
    vnc = request.config.getoption("--vnc")
    video = request.config.getoption("--video")
    tester_name = request.config.getoption("--tester_name")
    screen_resolution = request.config.getoption("--screen_resolution")

    logger = logging.getLogger(request.node.name)
    file_handler = logging.FileHandler(f"logs/{request.node.name}.log")
    file_handler.setFormatter(logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s'))
    logger.addHandler(file_handler)
    logger.setLevel(level=log_level)

    logger.info("===> Test {} started at {}".format(request.node.name, datetime.datetime.now()))

    if browser == "chrome":
        options = webdriver.ChromeOptions()
        options.headless = True
        driver = webdriver.Chrome(options=options)
    elif browser == "yandex":
        options = webdriver.ChromeOptions()
        driver = webdriver.Chrome(executable_path=f"{drivers}/yandexdriver", options=options)
    elif browser == "firefox":
        service = FirefoxService(executable_path=GeckoDriverManager().install())
        driver = webdriver.Firefox(service=service)
    elif browser == "safari":
        driver = webdriver.Safari()
    else:
        raise Exception("Driver not found!")

    capabilities = {
        "browserName": browser,
        "browserVersion": browser_version,
        "selenoid:options": {
            "enableVNC": vnc,
            "enableVideo": video,
            "name": tester_name,
            "screenResolution": screen_resolution
        }
    }

    driver = webdriver.Remote(
        command_executor=f"http://{executor}:4444/wd/hub",
        desired_capabilities=capabilities
    )

    driver.base_url = base_url
    driver.get(base_url)
    driver.maximize_window()

    driver.log_level = log_level
    driver.logger = logger
    driver.test_name = request.node.name
    logger.info("Browser:{}".format(browser, driver.desired_capabilities))

    def fin():
        driver.quit()
        logger.info("===> Test {} finished at {}".format(request.node.name, datetime.datetime.now()))

    request.addfinalizer(fin)

    return driver
