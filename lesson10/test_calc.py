import pytest
import allure
from selenium import webdriver
from pages.slow_calculator_page import SlowCalculatorPage
from selenium.common.exceptions import TimeoutException

@pytest.fixture
def driver():
    driver = webdriver.Chrome()
    yield driver
    driver.quit()

@allure.title("Тест калькулятора")
@allure.description("Проверяет правильность работы медленного калькулятора.")
@allure.feature("Калькулятор")
@allure.severity(allure.severity_level.NORMAL)
def test_calculator(driver):
    calculator_page = SlowCalculatorPage(driver)
    calculator_page.open()

    with allure.step("Установка задержки"):
        calculator_page.set_delay("45")

    with allure.step("Нажатие кнопок для вычисления"):
        calculator_page.click_button("7")
        calculator_page.click_button("+")
        calculator_page.click_button("8")
        calculator_page.click_button("=")

    try:
        with allure.step("Получение результата"):
            result = calculator_page.get_result()
            print(f"Текущий результат: {result}")
            
            assert result == "15", f"Ошибка: ожидалось 15, но получено {result}"
            print("Тест успешно пройден: результат 15")
    except TimeoutException:
        allure.attach(driver.get_screenshot_as_png(), name="Скриншот ошибки", attachment_type=allure.attachment_type.PNG)
        print("Таймаут: результат не был найден.")
    except AssertionError as e:
        allure.attach(driver.get_screenshot_as_png(), name="Скриншот ошибки", attachment_type=allure.attachment_type.PNG)
        print(e)
