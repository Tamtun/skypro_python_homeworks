from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class SlowCalculatorPage:
    def __init__(self, driver):
        """
        Инициализирует класс SlowCalculatorPage.

        :param driver: WebDriver для управления браузером.
        """
        self.driver = driver

    def open(self):
        """Открывает страницу медленного калькулятора."""
        self.driver.get("https://bonigarcia.dev/selenium-webdriver-java/slow-calculator.html")

    def set_delay(self, delay: str) -> None:
        """
        Устанавливает задержку для калькулятора.

        :param delay: Задержка в секундах, которую нужно установить.
        """
        delay_input = self.driver.find_element(By.CSS_SELECTOR, "#delay")
        delay_input.clear()
        delay_input.send_keys(delay)

    def click_button(self, button_text: str) -> None:
        """
        Нажимает на кнопку с заданным текстом.

        :param button_text: Текст кнопки, которую нужно нажать.
        """
        buttons = self.driver.find_elements(By.CSS_SELECTOR, "span.btn.btn-outline-primary, span.operator.btn.btn-outline-success, span.btn.btn-outline-warning")
        for button in buttons:
            if button.text == button_text:
                button.click()
                break

    def get_result(self) -> str:
        """
        Получает результат вычислений из калькулятора.

        :return: Текст результата на экране калькулятора.
        """
        WebDriverWait(self.driver, 90).until(EC.presence_of_element_located((By.CSS_SELECTOR, ".screen")))
        return self.driver.find_element(By.CSS_SELECTOR, ".screen").text
