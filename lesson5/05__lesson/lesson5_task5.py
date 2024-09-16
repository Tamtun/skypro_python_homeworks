from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.firefox.service import Service
from selenium.webdriver.firefox.options import Options
from time import sleep

# Настройки браузера
options = Options()
options.headless = False  # Запуск браузера с интерфейсом

# Инициализация браузера с geckodriver
driver = webdriver.Firefox()

# Открываем страницу
driver.get("http://the-internet.herokuapp.com/inputs")

# Находим поле ввода по его локатору
input_field = driver.find_element(By.CSS_SELECTOR, "input[type='number']")

# Вводим текст "1000"
input_field.send_keys("1000")

# Задержка на 5 секунд, чтобы увидеть результат
sleep(5)

# Очищаем поле
input_field.clear()

# Задержка на 2 секунды, чтобы увидеть результат
sleep(2)

# Вводим текст "999"
input_field.send_keys("999")

# Задержка на 5 секунд, чтобы увидеть результат
sleep(5)

# Закрываем браузер
driver.quit()
