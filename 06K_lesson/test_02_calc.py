from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import (
    TimeoutException,
)  # Импортируем TimeoutException

driver = webdriver.Chrome()

try:
    driver.get(
        "https://bonigarcia.dev/selenium-webdriver-java/slow-calculator.html"
    )

    delay_input = driver.find_element(By.CSS_SELECTOR, "#delay")
    delay_input.clear()
    delay_input.send_keys("45")

    buttons = driver.find_elements(
        By.CSS_SELECTOR,
        "span.btn.btn-outline-primary, span.operator.btn.btn-outline-success, span.btn.btn-outline-warning",
    )

    for button in buttons:
        if button.text == "7":
            button.click()
            break

    for button in buttons:
        if button.text == "+":
            button.click()
            break

    for button in buttons:
        if button.text == "8":
            button.click()
            break

    for button in buttons:
        if button.text == "=":
            button.click()
            break

    try:
        WebDriverWait(driver, 90).until(
            EC.presence_of_element_located((By.CSS_SELECTOR, ".screen"))
        )

        result = driver.find_element(By.CSS_SELECTOR, ".screen").text

        print(f"Текущий результат: {result}")

        assert result == "15", f"Ошибка: ожидалось 15, но получено {result}"
        print("Тест успешно пройден: результат 15")
    except TimeoutException:
        print("Таймаут: результат не был найден.")
    except AssertionError as e:
        print(e)

finally:
    driver.quit()