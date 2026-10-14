from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as expected
from selenium.webdriver.support.ui import WebDriverWait

from locators import ConstructorPageLocators


class ConstructorPage:
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)

    def get_ingredient_counter(self, ingredient_name):
        ingredient_card = (
            By.XPATH,
            f"//p[normalize-space()='{ingredient_name}']/ancestor::li[1]"
        )
        cards = self.driver.find_elements(*ingredient_card)

        if not cards:
            return 0

        counters = cards[0].find_elements(
            By.XPATH,
            ".//*[contains(@class, 'counter__num')]"
        )

        return int(counters[0].text) if counters else 0

    def add_bun_to_constructor(self, bun_name):
        bun_card = (
            By.XPATH,
            f"//p[normalize-space()='{bun_name}']/ancestor::li[1]"
        )
        source = self.wait.until(
            expected.element_to_be_clickable(bun_card)
        )
        target = self.wait.until(
            expected.visibility_of_element_located(
                ConstructorPageLocators.BUN_DROP_ZONE
            )
        )

        ActionChains(self.driver).drag_and_drop(source, target).perform()

    def wait_for_counter_increase(self, bun_name, initial_counter):
        return self.wait.until(
            lambda driver: self.get_ingredient_counter(bun_name) > initial_counter
        )

    def create_order(self):
        self.wait.until(
            expected.element_to_be_clickable(
                ConstructorPageLocators.ORDER_BUTTON
            )
        ).click()

        self.wait.until(
            expected.visibility_of_element_located(
                ConstructorPageLocators.ORDER_STATUS
            )
        )

        order_number = self.wait.until(
            expected.visibility_of_element_located(
                ConstructorPageLocators.ORDER_NUMBER
            )
        )

        return order_number.text
