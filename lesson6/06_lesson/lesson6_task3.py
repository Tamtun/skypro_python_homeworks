from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

driver = webdriver.Chrome(
    service=ChromeService(ChromeDriverManager().install())
)

driver.implicitly_wait(10)

driver.get("https://bonigarcia.dev/selenium-webdriver-java/loading-images.html")

images = WebDriverWait(driver, 40).until(
    EC.visibility_of_all_elements_located((By.CSS_SELECTOR, "img.img-fluid"))
)

for img in images:
    print(img.get_attribute("src"))

driver.quit()
