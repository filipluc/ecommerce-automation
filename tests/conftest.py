import pytest
from base.webdriverfactory import WebDriverFactory
import utilities.custom_logger as cl
import logging
from utilities.util import current_time as current_time

log = cl.customLogger(logging.DEBUG)

@pytest.fixture()
def setUp():
    log.info("Running method level setUp")
    yield
    log.info("Running method level tearDown")

@pytest.fixture(scope="class")
def oneTimeSetUp(request, browser):
    log.info("=== TEST CASE " + request.node.name + " STARTED at " + current_time + " ===")
    log.info("Running one time setUp")
    wdf = WebDriverFactory(browser)
    driver = wdf.getWebDriverInstance()

    if request.cls is not None:
        request.cls.driver = driver
    yield driver
    driver.quit()
    log.info("Running one time tearDown")
    log.info("=== TEST CASE " + request.node.name + " FINISHED at " + current_time + " ===")

def pytest_addoption(parser):
    parser.addoption("--browser")
    parser.addoption("--osType", help="Type of operating system")

@pytest.fixture(scope="session")
def browser(request):
    return request.config.getoption("--browser")

@pytest.fixture(scope="session")
def osType(request):
    return request.config.getoption("--osType")