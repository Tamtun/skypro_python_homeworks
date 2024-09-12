from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.firefox.service import Service
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from time import sleep

# Настройки браузера
options = Options()
options.headless = False  # Запуск браузера с интерфейсом

# Путь к geckodriver
service = Service(executable_path='C:\\Users\\intes\\OneDrive\\Рабочий стол\\python lessons\\lesson5\\geckodriver.exe')

# Инициализация браузера с geckodriver
driver = webdriver.Firefox(service=service, options=options)

# Открываем страницу
driver.get("http://the-internet.herokuapp.com/entry_ad")

# Ожидание модального окна и нажатие на кнопку Close
WebDriverWait(driver, 10).until(
    EC.element_to_be_clickable((By.CSS_SELECTOR, "div.modal-footer > p"))
).click()

# Задержка на 5 секунд перед закрытием браузера
sleep(5)

# Закрываем браузер
driver.quit()
