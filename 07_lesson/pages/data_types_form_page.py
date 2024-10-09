from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException

class DataTypesFormPage:
    def __init__(self, driver):
        self._driver = driver
        self.url = "https://bonigarcia.dev/selenium-webdriver-java/data-types.html"

    def open(self):
        self._driver.get(self.url)

    def fill_form(self, first_name, last_name, address, email, phone, zip_code, city, country, job_position, company):
        self._driver.find_element(By.NAME, "first-name").send_keys(first_name)
        self._driver.find_element(By.NAME, "last-name").send_keys(last_name)
        self._driver.find_element(By.NAME, "address").send_keys(address)
        self._driver.find_element(By.NAME, "e-mail").send_keys(email)
        self._driver.find_element(By.NAME, "phone").send_keys(phone)
        self._driver.find_element(By.NAME, "zip-code").send_keys(zip_code)  # Оставляем пустым
        self._driver.find_element(By.NAME, "city").send_keys(city)
        self._driver.find_element(By.NAME, "country").send_keys(country)
        self._driver.find_element(By.NAME, "job-position").send_keys(job_position)
        self._driver.find_element(By.NAME, "company").send_keys(company)

    def submit(self):
        self._driver.find_element(By.CSS_SELECTOR, "button[type='submit']").click()

    def wait_for_zip_code_field(self):
        WebDriverWait(self._driver, 10).until(
            EC.presence_of_element_located((By.NAME, "zip-code"))
        )

    def is_zip_code_highlighted_red(self):
        zip_code_field = self._driver.find_element(By.NAME, "zip-code")
        return "border-color: red;" in zip_code_field.get_attribute("style")

    def is_field_highlighted_green(self, field_name):
        input_field = self._driver.find_element(By.NAME, field_name)
        return "border-color: green;" in input_field.get_attribute("style")
