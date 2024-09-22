from time import sleep
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

driver = webdriver.Chrome(
    service=ChromeService(ChromeDriverManager().install())
)
driver.get("http://uitestingplayground.com/ajax")


driver.find_element(By.CSS_SELECTOR, "button#ajaxButton").click()

text_element = WebDriverWait(driver, 60, 0.1).until(
    EC.text_to_be_present_in_element(
        (By.CSS_SELECTOR, "div#content > p.bg-success"),
        "Data loaded with AJAX get request.",
    )
)

loaded_text = driver.find_element(
    By.CSS_SELECTOR, "div#content > p.bg-success"
).text
print(loaded_text)

sleep(5)

driver.quit()
