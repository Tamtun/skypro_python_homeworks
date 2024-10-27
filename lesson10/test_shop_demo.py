import pytest
import allure
from selenium import webdriver
from pages.shop_demo_page import ShopDemoPage  # Импортируем класс страницы

@pytest.fixture
def driver():
    driver = webdriver.Chrome()
    yield driver
    driver.quit()

@allure.title("Тест покупки в магазине")
@allure.description("Проверяет процесс покупки в магазине с демо-аккаунтом.")
@allure.feature("Магазин")
@allure.severity(allure.severity_level.CRITICAL)
def test_shop_demo(driver):
    page = ShopDemoPage(driver)
    
    with allure.step("Авторизация пользователя"):
        page.login("standard_user", "secret_sauce")

    with allure.step("Добавление товаров в корзину"):
        page.add_items_to_cart()
        
    with allure.step("Переход в корзину"):
        page.go_to_cart()

    with allure.step("Оформление заказа"):
        page.checkout("Имя", "Фамилия", "12345")

    with allure.step("Получение итоговой суммы"):
        total_price = page.get_total_price()

    with allure.step("Проверка итоговой суммы"):
        assert total_price == "Total: $58.29", f"Итоговая сумма отличается: {total_price}"
        print("Итоговая сумма верна!")
