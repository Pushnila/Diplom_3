from data import BASE_URL
from locators import AuthPageLocators
from pages.base_page import BasePage


class AuthPage(BasePage):
    def register(self, user_data):
        self.open(f'{BASE_URL}register')
        self.get_element(AuthPageLocators.NAME_INPUT).send_keys(user_data['name'])
        self.get_element(AuthPageLocators.EMAIL_INPUT).send_keys(user_data['email'])
        self.get_element(AuthPageLocators.PASSWORD_INPUT).send_keys(user_data['password'])
        self.click(AuthPageLocators.REGISTER_BUTTON)
        self.wait.until(lambda driver: '/login' in self.get_current_url())

    def login(self, user_data):
        self.open(f'{BASE_URL}login')
        self.get_element(AuthPageLocators.EMAIL_INPUT).send_keys(user_data['email'])
        self.get_element(AuthPageLocators.PASSWORD_INPUT).send_keys(user_data['password'])
        self.click(AuthPageLocators.LOGIN_BUTTON)
        self.wait.until(
            lambda driver: self.get_current_url().rstrip('/') == BASE_URL.rstrip('/')
        )
