from selenium.webdriver.support import expected_conditions as expected
from selenium.webdriver.support.ui import WebDriverWait

from locators import AuthPageLocators


class AuthPage:
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)

    def register(self, base_url, user_data):
        self.driver.get(f'{base_url}register')

        self.wait.until(
            expected.visibility_of_element_located(
                AuthPageLocators.NAME_INPUT
            )
        ).send_keys(user_data['name'])

        self.driver.find_element(
            *AuthPageLocators.EMAIL_INPUT
        ).send_keys(user_data['email'])

        self.driver.find_element(
            *AuthPageLocators.PASSWORD_INPUT
        ).send_keys(user_data['password'])

        self.driver.find_element(
            *AuthPageLocators.REGISTER_BUTTON
        ).click()

        self.wait.until(expected.url_contains('/login'))

    def login(self, base_url, user_data):
        self.driver.get(f'{base_url}login')

        self.wait.until(
            expected.visibility_of_element_located(
                AuthPageLocators.EMAIL_INPUT
            )
        ).send_keys(user_data['email'])

        self.driver.find_element(
            *AuthPageLocators.PASSWORD_INPUT
        ).send_keys(user_data['password'])

        self.driver.find_element(
            *AuthPageLocators.LOGIN_BUTTON
        ).click()

        self.wait.until(
            lambda driver: driver.current_url.rstrip('/') == base_url.rstrip('/')
        )
