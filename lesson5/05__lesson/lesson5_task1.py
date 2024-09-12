from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from time import sleep

# Настройка драйвера
driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
driver.maximize_window()

# Шаг 1: Откройте страницу
driver.get("http://the-internet.herokuapp.com/add_remove_elements/")

# Шаг 2: Пять раз кликните на кнопку "Add Element"
add_button = driver.find_element(By.CSS_SELECTOR, "button[onclick='addElement()']")
for _ in range(5):
    add_button.click()

# Шаг 3: Соберите со страницы список кнопок "Delete"
delete_buttons = driver.find_elements(By.CSS_SELECTOR, "button.added-manually")

# Шаг 4: Выведите на экран размер списка
print(f"Количество кнопок Delete: {len(delete_buttons)}")

# Задержка для наглядности
sleep(5)
