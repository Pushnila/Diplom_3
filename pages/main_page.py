from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as expected
from selenium.webdriver.support.ui import WebDriverWait

from locators import MainPageLocators


class MainPage:
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)

    def open(self, base_url):
        self.driver.get(base_url)
        self.wait.until(
            expected.element_to_be_clickable(
                MainPageLocators.CONSTRUCTOR_LINK
            )
        )

    def click_constructor(self):
        self.wait.until(
            expected.element_to_be_clickable(
                MainPageLocators.CONSTRUCTOR_LINK
            )
        ).click()

    def click_order_feed(self):
        self.wait.until(
            expected.element_to_be_clickable(
                MainPageLocators.ORDER_FEED_LINK
            )
        ).click()

    def click_ingredient(self, ingredient_name):
        ingredient_locator = (
            By.XPATH,
            f"//p[normalize-space()='{ingredient_name}']"
        )
        self.wait.until(
            expected.element_to_be_clickable(ingredient_locator)
        ).click()

    def ingredient_details_are_opened(self):
        return self.wait.until(
            expected.visibility_of_element_located(
                MainPageLocators.INGREDIENT_DETAILS_TITLE
            )
        ).is_displayed()

    def close_ingredient_details(self):
        self.wait.until(
            expected.element_to_be_clickable(
                MainPageLocators.MODAL_CLOSE_BUTTON
            )
        ).click()

    def ingredient_details_are_closed(self):
        return not self.driver.find_elements(
            *MainPageLocators.INGREDIENT_DETAILS_TITLE
        )
