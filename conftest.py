import allure
import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options as ChromeOptions
from selenium.webdriver.firefox.options import Options as FirefoxOptions

from data import TEST_INGREDIENT_NAME
from helpers import generate_user_data
from pages.auth_page import AuthPage
from pages.constructor_page import ConstructorPage
from pages.feed_page import FeedPage
from pages.main_page import MainPage


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
def logged_in_user(driver):
    user_data = generate_user_data()
    auth_page = AuthPage(driver)
    auth_page.register(user_data)
    auth_page.login(user_data)
    return user_data


@pytest.fixture
def created_order(driver, logged_in_user):
    feed_page = FeedPage(driver)
    main_page = MainPage(driver)
    constructor_page = ConstructorPage(driver)

    feed_page.open()
    order_data = {
        'total_before': feed_page.get_total_completed_count(),
        'today_before': feed_page.get_today_completed_count()
    }

    main_page.open()
    constructor_page.add_bun_to_constructor(TEST_INGREDIENT_NAME)
    order_data['number'] = constructor_page.create_order()

    return order_data


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
