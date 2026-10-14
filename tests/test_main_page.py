import allure

from pages.constructor_page import ConstructorPage
from pages.main_page import MainPage


TEST_INGREDIENT_NAME = 'Краторная булка N-200i'


@allure.epic('Stellar Burgers UI')
@allure.feature('Главная страница')
class TestMainPage:

    @allure.title('Переход в конструктор по клику на «Конструктор»')
    def test_click_constructor_opens_constructor(self, driver, base_url):
        main_page = MainPage(driver)
        main_page.open(base_url)

        main_page.click_order_feed()
        main_page.click_constructor()

        assert driver.current_url.rstrip('/') == base_url.rstrip('/')

    @allure.title('Переход в ленту заказов по клику на «Лента Заказов»')
    def test_click_order_feed_opens_order_feed(self, driver, base_url):
        main_page = MainPage(driver)
        main_page.open(base_url)

        main_page.click_order_feed()

        assert '/feed' in driver.current_url

    @allure.title('Открывается окно с деталями ингредиента')
    def test_click_ingredient_opens_details_modal(self, driver, base_url):
        main_page = MainPage(driver)
        main_page.open(base_url)

        main_page.click_ingredient(TEST_INGREDIENT_NAME)

        assert main_page.ingredient_details_are_opened()

    @allure.title('Окно деталей ингредиента закрывается по клику на крестик')
    def test_close_ingredient_details_modal(self, driver, base_url):
        main_page = MainPage(driver)
        main_page.open(base_url)

        main_page.click_ingredient(TEST_INGREDIENT_NAME)
        main_page.close_ingredient_details()

        assert main_page.ingredient_details_are_closed()

    @allure.title('Счётчик ингредиента увеличивается после добавления в заказ')
    def test_add_bun_increases_ingredient_counter(self, driver, base_url):
        main_page = MainPage(driver)
        constructor_page = ConstructorPage(driver)
        main_page.open(base_url)

        initial_counter = constructor_page.get_ingredient_counter(
            TEST_INGREDIENT_NAME
        )
        constructor_page.add_bun_to_constructor(TEST_INGREDIENT_NAME)
        new_counter = constructor_page.wait_for_counter_increase(
            TEST_INGREDIENT_NAME,
            initial_counter
        )

        assert new_counter > initial_counter
