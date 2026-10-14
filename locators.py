from selenium.webdriver.common.by import By


class MainPageLocators:
    CONSTRUCTOR_LINK = (
        By.XPATH,
        "//p[normalize-space()='Конструктор']/ancestor::a"
    )
    ORDER_FEED_LINK = (
        By.XPATH,
        "//p[normalize-space()='Лента Заказов']/ancestor::a"
    )
    INGREDIENT_DETAILS_TITLE = (
        By.XPATH,
        "//*[normalize-space()='Детали ингредиента']"
    )
    MODAL_CLOSE_BUTTON = (
        By.XPATH,
        "//*[normalize-space()='Детали ингредиента']/ancestor::*[self::section or self::div][1]//button"
    )


class OrderFeedLocators:
    IN_PROGRESS_TITLE = (
        By.XPATH,
        "//*[normalize-space()='В работе:']"
    )


class ConstructorPageLocators:
    BUN_DROP_ZONE = (
        By.XPATH,
        "//*[normalize-space()='Выберите булки']"
    )
    ORDER_BUTTON = (
        By.XPATH,
        "//button[normalize-space()='Оформить заказ']"
    )
    ORDER_STATUS = (
        By.XPATH,
        "//*[normalize-space()='Ваш заказ начали готовить']"
    )
    ORDER_NUMBER = (
        By.XPATH,
        "//*[normalize-space()='Ваш заказ начали готовить']/preceding-sibling::*[1]"
    )


class AuthPageLocators:
    NAME_INPUT = (By.NAME, 'name')
    EMAIL_INPUT = (By.NAME, 'email')
    PASSWORD_INPUT = (By.NAME, 'password')
    REGISTER_BUTTON = (
        By.XPATH,
        "//button[normalize-space()='Зарегистрироваться']"
    )
    LOGIN_BUTTON = (
        By.XPATH,
        "//button[normalize-space()='Войти']"
    )
