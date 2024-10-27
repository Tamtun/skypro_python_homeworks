from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class ShopDemoPage:
    def __init__(self, driver):
        self.driver = driver

    def login(self, username: str, password: str) -> None:
        """Авторизует пользователя на сайте.

        :param username: Имя пользователя.
        :param password: Пароль пользователя.
        """
        self.driver.get("https://www.saucedemo.com/")
        WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located((By.ID, "user-name"))
        ).send_keys(username)
        WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located((By.ID, "password"))
        ).send_keys(password)
        WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.ID, "login-button"))
        ).click()

    def add_items_to_cart(self) -> None:
        """Добавляет товары в корзину."""
        items_to_add = [
            "add-to-cart-sauce-labs-backpack",
            "add-to-cart-sauce-labs-bolt-t-shirt",
            "add-to-cart-sauce-labs-onesie",
        ]
        for item in items_to_add:
            WebDriverWait(self.driver, 10).until(
                EC.element_to_be_clickable((By.ID, item))
            ).click()

    def go_to_cart(self) -> None:
        """Переходит в корзину."""
        WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.CLASS_NAME, "shopping_cart_link"))
        ).click()

    def checkout(self, first_name: str, last_name: str, postal_code: str) -> None:
        """Оформляет заказ.

        :param first_name: Имя покупателя.
        :param last_name: Фамилия покупателя.
        :param postal_code: Почтовый код.
        """
        WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.ID, "checkout"))
        ).click()
        WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located((By.ID, "first-name"))
        ).send_keys(first_name)
        WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located((By.ID, "last-name"))
        ).send_keys(last_name)
        WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located((By.ID, "postal-code"))
        ).send_keys(postal_code)
        WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.ID, "continue"))
        ).click()

    def get_total_price(self) -> str:
        """Получает итоговую сумму заказа.

        :return: Итоговая сумма как текст.
        """
        total_price_element = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located((By.CLASS_NAME, "summary_total_label"))
        )
        return total_price_element.text
