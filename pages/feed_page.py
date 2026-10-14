from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as expected
from selenium.webdriver.support.ui import WebDriverWait

from locators import OrderFeedLocators


class FeedPage:
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)

    def open(self, base_url):
        self.driver.get(f'{base_url}feed')
        self.wait.until(
            expected.visibility_of_element_located(
                OrderFeedLocators.IN_PROGRESS_TITLE
            )
        )

    def get_total_completed_count(self):
        counter_locator = (
            By.XPATH,
            "//*[normalize-space()='Выполнено за все время:']"
            "/following-sibling::*[1]"
        )
        counter = self.wait.until(
            expected.visibility_of_element_located(counter_locator)
        )
        return int(counter.text)

    def get_today_completed_count(self):
        counter_locator = (
            By.XPATH,
            "//*[normalize-space()='Выполнено за сегодня:']"
            "/following-sibling::*[1]"
        )
        counter = self.wait.until(
            expected.visibility_of_element_located(counter_locator)
        )
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
        order_locator = (
            By.XPATH,
            "//*[normalize-space()='В работе:']"
            f"/following-sibling::*[1]//*[contains(normalize-space(), '{order_number}')]"
        )
        return bool(self.driver.find_elements(*order_locator))

    def wait_until_order_is_in_progress(self, order_number):
        return self.wait.until(
            lambda driver: self.order_is_in_progress(order_number)
        )
