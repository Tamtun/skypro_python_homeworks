import pytest
import allure
from selenium import webdriver
from pages.data_types_form_page import DataTypesFormPage  # Импортируем класс страницы

@pytest.fixture
def driver():
    driver = webdriver.Chrome()
    yield driver
    driver.quit()

@allure.title("Тест отправки формы")
@allure.description("Проверяет правильность работы формы с данными.")
@allure.feature("Форма")
@allure.severity(allure.severity_level.NORMAL)
def test_form_submission(driver):
    page = DataTypesFormPage(driver)
    page.open()
    
    with allure.step("Заполнение формы"):
        # Заполняем форму
        page.fill_form("Иван", "Петров", "Ленина, 55-3", "test@skypro.com", "+7985899998787", "", "Москва", "Россия", "QA", "SkyPro")
        
    with allure.step("Отправка формы"):
        page.submit()

    with allure.step("Ожидание поля Zip code"):
        # Ждем загрузки поля zip-code
        page.wait_for_zip_code_field()

    with allure.step("Проверка стиля поля Zip code после отправки"):
        # Проверяем стиль поля Zip code после нажатия на кнопку Submit
        assert page.is_zip_code_highlighted_red(), "Поле Zip code не подсвечено красным"

    with allure.step("Проверка остальных полей"):
        # Проверяем остальные поля
        fields_to_check = ["first-name", "last-name", "address", "e-mail", "phone", "city", "country", "job-position", "company"]
        for field in fields_to_check:
            assert page.is_field_highlighted_green(field), f"{field} поле не подсвечено зеленым"
