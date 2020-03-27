from .base_page import BasePage
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import random

"""
Для запуска тестов использовать команду:
pytest -s -v --browser_name=firefox test_main_page.py --alluredir=allure_results

Для просмотра результатов:
allure serve allure_results
"""

class MainPage(BasePage):
    def go_to_register_page(self):
        driver = self.browser

        driver.find_element(By.CSS_SELECTOR, "#email_create").send_keys('kurchik.sasha@gmail.com')
        driver.find_element(By.CSS_SELECTOR, "#SubmitCreate").click()

        if WebDriverWait(driver, 10).until(
            EC.visibility_of_element_located((By.ID, 'create_account_error'))):

            driver.find_element(By.CSS_SELECTOR, "#email_create").send_keys(str(random.randint(0, 999)))
            driver.find_element(By.CSS_SELECTOR, "#SubmitCreate").click()

        WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.XPATH, '//h3[text()="Your personal information"]'))
        )


