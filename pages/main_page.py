from data import BASE_URL
from locators import MainPageLocators
from pages.base_page import BasePage


class MainPage(BasePage):
    def open(self):
        super().open(BASE_URL)
        self.get_element(MainPageLocators.CONSTRUCTOR_LINK)

    def click_constructor(self):
        self.click(MainPageLocators.CONSTRUCTOR_LINK)

    def click_order_feed(self):
        self.click(MainPageLocators.ORDER_FEED_LINK)

    def click_ingredient(self, ingredient_name):
        self.click(MainPageLocators.ingredient(ingredient_name))

    def ingredient_details_are_opened(self):
        return self.is_element_visible(MainPageLocators.INGREDIENT_DETAILS_TITLE)

    def close_ingredient_details(self):
        self.click(MainPageLocators.MODAL_CLOSE_BUTTON)

    def ingredient_details_are_closed(self):
        return self.is_element_absent(MainPageLocators.INGREDIENT_DETAILS_TITLE)

    def constructor_is_opened(self):
        return self.get_current_url().rstrip('/') == BASE_URL.rstrip('/')

    def order_feed_is_opened(self):
        return self.get_current_url().rstrip('/').endswith('/feed')
