import pytest
from selenium import webdriver
from selenium.webdriver.edge.service import Service as EdgeService
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.firefox.service import Service as FirefoxService

from utilities.baseclass import BaseClass

driver = None
url = None


@pytest.fixture(scope="class")
def setup(request):
    global driver
    global url
    browser_name = request.config.getoption("--browser_name")
    BaseClass.get_logger().info("Browser initialisation")
    url = request.config.getoption("--url")
    #url = HomepageData.getExcelTestData("Qa")["Url"]
    print(url)
    if browser_name == "edge":
        service_obj = EdgeService()
        driver = webdriver.Edge(service=service_obj)
        driver.maximize_window()
    elif browser_name == "chrome":
        service_objs = ChromeService()
        driver = webdriver.Chrome(service=service_objs)
        driver.maximize_window()

    elif browser_name == "firefox":
        service_objm = FirefoxService("c:/Users/ayyappan.g/Downloads/geckodriver-v0.33.0-win64 (1)/geckodriver.exe")
        driver = webdriver.Firefox(service=service_objm)
        driver.maximize_window()
    else:
        service_objk = ChromeService(
            "c:/Users/ayyappan.g/Downloads/chromedriver-win64 (3)/chromedriver-win64/chromedriver.exe")
        driver = webdriver.Chrome(service=service_objk)
        driver.maximize_window()

    driver.implicitly_wait(20)
    BaseClass.get_logger().info("Launching url")

    driver.get(url)

    request.cls.driver = driver
    request.cls.url = url
    # return driver
    yield
    driver.close()


#
# def __init__(self, driver):
#     self.driver = driver


def pytest_addoption(parser):
    parser.addoption(
        "--browser_name", action="store", default="edge"
    )
    parser.addoption(
        "--url", action="store", default="https://core-qa.atlasbyelements.com/#/login"
    )

@pytest.mark.hookwrapper
def pytest_runtest_makereport(item):
    """
        Extends the PyTest Plugin to take and embed screenshot in html report, whenever test fails.
        :param item:
        """
    pytest_html = item.config.pluginmanager.getplugin('html')
    outcome = yield
    report = outcome.get_result()
    extra = getattr(report, 'extra', [])

    if report.when == 'call' or report.when == "setup":
        xfail = hasattr(report, 'wasxfail')
        if (report.skipped and xfail) or (report.failed and not xfail):
            file_name = report.nodeid.replace("::", "_") + ".png"
            _capture_screenshot(file_name)
            if file_name:
                html = '<div><img src="%s" alt="screenshot" style="width:304px;height:228px;" ' \
                       'onclick="window.open(this.src)" align="right"/></div>' % file_name
                extra.append(pytest_html.extras.html(html))
        report.extra = extra


def _capture_screenshot(name):
    BaseClass.get_logger().info("Taking Screenshot")
    driver.get_screenshot_as_file(name)
