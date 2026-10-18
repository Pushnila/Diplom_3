import allure

from pages.feed_page import FeedPage


@allure.epic('Stellar Burgers UI')
@allure.feature('Лента заказов')
class TestOrderFeed:

    @allure.title(
        'После создания заказа увеличивается счётчик «Выполнено за всё время»'
    )
    def test_total_completed_counter_increases(self, driver, created_order):
        feed_page = FeedPage(driver)
        feed_page.open()

        actual_count = feed_page.wait_for_total_completed_increase(
            created_order['total_before']
        )

        assert actual_count > created_order['total_before']

    @allure.title(
        'После создания заказа увеличивается счётчик «Выполнено за сегодня»'
    )
    def test_today_completed_counter_increases(self, driver, created_order):
        feed_page = FeedPage(driver)
        feed_page.open()

        actual_count = feed_page.wait_for_today_completed_increase(
            created_order['today_before']
        )

        assert actual_count > created_order['today_before']

    @allure.title('Номер созданного заказа отображается в разделе «В работе»')
    def test_created_order_number_is_in_progress(self, driver, created_order):
        feed_page = FeedPage(driver)
        feed_page.open()

        assert feed_page.wait_until_order_is_in_progress(
            created_order['number']
        )
