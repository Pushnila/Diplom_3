from data import BASE_URL
from locators import OrderFeedLocators
from pages.base_page import BasePage


class FeedPage(BasePage):
    def open(self):
        super().open(f'{BASE_URL}feed')
        self.get_element(OrderFeedLocators.IN_PROGRESS_TITLE)

    def get_total_completed_count(self):
        counter = self.get_element(OrderFeedLocators.TOTAL_COMPLETED_COUNTER)
        return int(counter.text)

    def get_today_completed_count(self):
        counter = self.get_element(OrderFeedLocators.TODAY_COMPLETED_COUNTER)
        return int(counter.text)

    def wait_for_total_completed_increase(self, initial_count):
        return self.wait.until(
            lambda driver: self.get_total_completed_count() > initial_count
        )

    def wait_for_today_completed_increase(self, initial_count):
        return self.wait.until(
            lambda driver: self.get_today_completed_count() > initial_count
        )

    def order_is_in_progress(self, order_number):
        return bool(
            self.get_elements(OrderFeedLocators.order_in_progress(order_number))
        )

    def wait_until_order_is_in_progress(self, order_number):
        return self.wait.until(
            lambda driver: self.order_is_in_progress(order_number)
        )
