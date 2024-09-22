from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

driver = webdriver.Chrome(
    service=ChromeService(ChromeDriverManager().install())
)

driver.get("https://bonigarcia.dev/selenium-webdriver-java/loading-images.html")

WebDriverWait(driver, 40, 0.1).until(
    EC.presence_of_element_located((By.CSS_SELECTOR, "img#award"))
)

third_image = driver.find_element(By.CSS_SELECTOR, "img#award")

image_src = third_image.get_attribute("src")
print(image_src)

driver.implicitly_wait(10)

driver.quit()
