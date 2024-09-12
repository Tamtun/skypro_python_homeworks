from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from time import sleep

# Настройки Chrome для игнорирования ошибок SSL
chrome_options = Options()
chrome_options.add_argument("--ignore-certificate-errors")
chrome_options.add_argument("--ignore-ssl-errors")

# Запуск драйвера с указанными опциями
driver = webdriver.Chrome(
    service=ChromeService(ChromeDriverManager().install()), options=chrome_options
)
driver.maximize_window()

driver.get("http://uitestingplayground.com/dynamicid")

# Шаг 2: Кликните на синюю кнопку
# Синяя кнопка не имеет постоянного ID, поэтому ищем её по тексту.
blue_button = driver.find_element(By.XPATH, "//button[text()='Button with Dynamic ID']")
blue_button.click()


sleep(3)
