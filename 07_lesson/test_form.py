import pytest
from selenium import webdriver
from pages.data_types_form_page import DataTypesFormPage  # Импортируем класс страницы

@pytest.fixture
def driver():
    driver = webdriver.Chrome()
    yield driver
    driver.quit()

def test_form_submission(driver):
    page = DataTypesFormPage(driver)
    page.open()
    
    # Заполняем форму
    page.fill_form("Иван", "Петров", "Ленина, 55-3", "test@skypro.com", "+7985899998787", "", "Москва", "Россия", "QA", "SkyPro")
    page.submit()

    # Ждем загрузки поля zip-code
    page.wait_for_zip_code_field()

    # Проверяем стиль поля Zip code после нажатия на кнопку Submit
    assert page.is_zip_code_highlighted_red(), "Zip code field is not highlighted red"

    # Проверяем остальные поля
    fields_to_check = ["first-name", "last-name", "address", "e-mail", "phone", "city", "country", "job-position", "company"]
    for field in fields_to_check:
        assert page.is_field_highlighted_green(field), f"{field} field is not highlighted green"
