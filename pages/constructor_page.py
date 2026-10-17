from selenium.webdriver import ActionChains
from selenium.webdriver.support import expected_conditions as expected

from locators import ConstructorPageLocators, MainPageLocators
from pages.base_page import BasePage


class ConstructorPage(BasePage):
    def get_ingredient_counter(self, ingredient_name):
        cards = self.get_elements(MainPageLocators.ingredient_card(ingredient_name))

        if not cards:
            return 0

        counters = cards[0].find_elements(*MainPageLocators.INGREDIENT_COUNTER)
        return int(counters[0].text) if counters else 0

    def add_bun_to_constructor(self, bun_name):
        source = self.wait.until(
            expected.element_to_be_clickable(
                MainPageLocators.ingredient_card(bun_name)
            )
        )
        target = self.get_element(ConstructorPageLocators.BUN_DROP_ZONE)

        ActionChains(self.driver).drag_and_drop(source, target).perform()

    def wait_for_counter_increase(self, bun_name, initial_counter):
        return self.wait.until(
            lambda driver: self.get_ingredient_counter(bun_name) > initial_counter
        )

    def create_order(self):
        self.click(ConstructorPageLocators.ORDER_BUTTON)
        self.get_element(ConstructorPageLocators.ORDER_STATUS)
        order_number = self.get_element(ConstructorPageLocators.ORDER_NUMBER)
        return order_number.text
