import allure
import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options as ChromeOptions
from selenium.webdriver.firefox.options import Options as FirefoxOptions

from helpers import generate_user_data
from pages.auth_page import AuthPage


BASE_URL = 'https://stellarburgers.education-services.ru/'


def pytest_addoption(parser):
    parser.addoption(
        '--browser',
        action='store',
        default='chrome',
        choices=['chrome', 'firefox'],
        help='Browser for UI tests'
    )


@pytest.fixture
def driver(request):
    browser_name = request.config.getoption('--browser')

    if browser_name == 'chrome':
        browser = webdriver.Chrome(options=ChromeOptions())
    else:
        browser = webdriver.Firefox(options=FirefoxOptions())

    browser.set_window_size(1440, 900)
    request.node.driver = browser

    yield browser

    browser.quit()


@pytest.fixture
def base_url():
    return BASE_URL


@pytest.fixture
def user_data():
    return generate_user_data()


@pytest.fixture
def logged_in_user(driver, base_url, user_data):
    auth_page = AuthPage(driver)
    auth_page.register(base_url, user_data)
    auth_page.login(base_url, user_data)
    return user_data


@pytest.hookimpl(hookwrapper=True)
def pytest_runtest_makereport(item, call):
    outcome = yield
    report = outcome.get_result()

    if report.when != 'call' or not report.failed:
        return

    browser = getattr(item, 'driver', None)

    if browser:
        allure.attach(
            browser.get_screenshot_as_png(),
            name='Failure screenshot',
            attachment_type=allure.attachment_type.PNG
        )