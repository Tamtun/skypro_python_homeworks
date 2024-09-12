from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from time import sleep

# Указываем путь к драйверу вашего браузера
driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))

# Открываем страницу
driver.get("http://uitestingplayground.com/classattr")

# Находим кнопку по CSS-классу и кликаем на неё
button = driver.find_element(By.CLASS_NAME, "btn-primary")
button.click()


sleep(5)