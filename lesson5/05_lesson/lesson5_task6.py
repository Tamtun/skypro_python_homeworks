from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.firefox.service import Service
from selenium.webdriver.firefox.options import Options
from time import sleep

# Настройки браузера
options = Options()
options.headless = False  # Запуск браузера с интерфейсом

# Путь к geckodriver
service = Service(
    executable_path="C:\\Users\\intes\\OneDrive\\Рабочий стол\\python lessons\\lesson5\\geckodriver.exe"
)

# Инициализация браузера с geckodriver
driver = webdriver.Firefox(service=service, options=options)

# Открываем страницу
driver.get("http://the-internet.herokuapp.com/login")

# Находим поле ввода username и вводим значение
username_field = driver.find_element(By.ID, "username")
username_field.send_keys("tomsmith")

# Находим поле ввода password и вводим значение
password_field = driver.find_element(By.ID, "password")
password_field.send_keys("SuperSecretPassword!")

# Находим кнопку Login и нажимаем её
login_button = driver.find_element(By.CSS_SELECTOR, "button[type='submit']")
login_button.click()

# Задержка на 5 секунд, чтобы увидеть результат
sleep(5)

# Закрываем браузер
driver.quit()
