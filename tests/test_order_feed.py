import allure
import pytest

from pages.constructor_page import ConstructorPage
from pages.feed_page import FeedPage
from pages.main_page import MainPage


TEST_BUN_NAME = 'Краторная булка N-200i'


@pytest.fixture
def created_order(driver, base_url, logged_in_user):
    feed_page = FeedPage(driver)
    main_page = MainPage(driver)
    constructor_page = ConstructorPage(driver)

    feed_page.open(base_url)

    order_data = {
        'total_before': feed_page.get_total_completed_count(),
        'today_before': feed_page.get_today_completed_count()
    }

    main_page.open(base_url)
    constructor_page.add_bun_to_constructor(TEST_BUN_NAME)

    order_data['number'] = constructor_page.create_order()

    return order_data


@allure.epic('Stellar Burgers UI')
@allure.feature('Лента заказов')
class TestOrderFeed:

    @allure.title('После создания заказа увеличивается счётчик «Выполнено за всё время»')
    def test_total_completed_counter_increases(
        self,
        driver,
        base_url,
        created_order
    ):
        feed_page = FeedPage(driver)
        feed_page.open(base_url)

        actual_count = feed_page.wait_for_total_completed_increase(
            created_order['total_before']
        )

        assert actual_count > created_order['total_before']

    @allure.title('После создания заказа увеличивается счётчик «Выполнено за сегодня»')
    def test_today_completed_counter_increases(
        self,
        driver,
        base_url,
        created_order
    ):
        feed_page = FeedPage(driver)
        feed_page.open(base_url)

        actual_count = feed_page.wait_for_today_completed_increase(
            created_order['today_before']
        )

        assert actual_count > created_order['today_before']

    @allure.title('Номер созданного заказа отображается в разделе «В работе»')
    def test_created_order_number_is_in_progress(
        self,
        driver,
        base_url,
        created_order
    ):
        feed_page = FeedPage(driver)
        feed_page.open(base_url)

        assert feed_page.wait_until_order_is_in_progress(
            created_order['number']
        )
