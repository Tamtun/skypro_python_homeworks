from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException

driver = webdriver.Chrome()

driver.get("https://bonigarcia.dev/selenium-webdriver-java/data-types.html")

driver.find_element(By.NAME, "first-name").send_keys("Иван")
driver.find_element(By.NAME, "last-name").send_keys("Петров")
driver.find_element(By.NAME, "address").send_keys("Ленина, 55-3")
driver.find_element(By.NAME, "e-mail").send_keys("test@skypro.com")
driver.find_element(By.NAME, "phone").send_keys("+7985899998787")
driver.find_element(By.NAME, "zip-code").send_keys("")  # Оставляем пустым
driver.find_element(By.NAME, "city").send_keys("Москва")
driver.find_element(By.NAME, "country").send_keys("Россия")
driver.find_element(By.NAME, "job-position").send_keys("QA")
driver.find_element(By.NAME, "company").send_keys("SkyPro")

driver.find_element(By.CSS_SELECTOR, "button[type='submit']").click()

try:
    WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.NAME, "zip-code"))
    )

    zip_code_field = driver.find_element(By.NAME, "zip-code")
    assert "border-color: red;" in zip_code_field.get_attribute(
        "style"
    ), "Zip code field is not highlighted red"

    fields_to_check = [
        "firstname",
        "lastname",
        "address",
        "email",
        "phone",
        "city",
        "country",
        "job",
        "company",
    ]

    for field in fields_to_check:
        input_field = driver.find_element(By.NAME, field)
        assert "border-color: green;" in input_field.get_attribute(
            "style"
        ), f"{field} field is not highlighted green"

except TimeoutException:
    print("Timed out waiting for elements to be present.")

driver.quit()
