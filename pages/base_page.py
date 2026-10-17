from selenium.webdriver.support import expected_conditions as expected
from selenium.webdriver.support.ui import WebDriverWait


class BasePage:
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)

    def open(self, url):
        self.driver.get(url)

    def click(self, locator):
        self.wait.until(expected.element_to_be_clickable(locator)).click()

    def get_element(self, locator):
        return self.wait.until(expected.visibility_of_element_located(locator))

    def get_elements(self, locator):
        return self.driver.find_elements(*locator)

    def is_element_visible(self, locator):
        return self.get_element(locator).is_displayed()

    def is_element_absent(self, locator):
        return not self.get_elements(locator)

    def get_current_url(self):
        return self.driver.current_url
