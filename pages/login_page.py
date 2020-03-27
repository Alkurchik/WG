from .base_page import BasePage
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import allure


class LoginPage(BasePage):
    def should_be_register_page(self):
        driver = self.browser
        with allure.step('select gender (select)'):
            self.browser.find_element(By.ID, 'id_gender1').click()

        with allure.step('name entry'):
            self.fill_in_the_input_field('customer_firstname', 'Al')

        with allure.step('last name entry'):
            self.fill_in_the_input_field('customer_lastname', 'Kurchik')

        with allure.step('password entry'):
            self.fill_in_the_input_field('passwd', 'Kurchik123')

        with allure.step('date selection'):
            self.choise_select('days', '#days > option[value="4"]')

        with allure.step('month selection'):
            self.choise_select('months', '#months > option[value="6"]')

        with allure.step('year selection'):
            self.choise_select('years', '#years > option[value="1997"]')

        with allure.step('firstname entry'):
            self.fill_in_the_input_field('firstname', 'Al')

        with allure.step('second entry'):
            self.fill_in_the_input_field('lastname', 'Kurchik')

        with allure.step('company entry'):
            self.fill_in_the_input_field('company', 'Skipper')

        with allure.step('address entry'):
            self.fill_in_the_input_field('address1', 'Belarus')

        with allure.step('state choice'):
            self.choise_select('id_state', '#id_state > option[value="12"]')

        with allure.step('address 2 entry'):
            self.fill_in_the_input_field('address2', 'Minsk region')

        with allure.step('city entry'):
            self.fill_in_the_input_field('city', 'Solihorsk')

        with allure.step('postcode entry'):
            self.fill_in_the_input_field('postcode', '22371')

        with allure.step('input in other field'):
            self.fill_in_the_input_field('other', 'I\'ll be able')

        with allure.step('phone number entry'):
            self.fill_in_the_input_field('phone_mobile', '+375291338075')

        with allure.step('email entry'):
            self.fill_in_the_input_field('alias', 'alex@alex.alex')

        with allure.step('submit'):
            self.browser.find_element(By.ID, 'submitAccount').click()

        # with allure.step('page check'):
        # WebDriverWait(driver, 10).until(
        #     EC.presence_of_element_located((By.XPATH, '//h1[text()="My account"]')))

        if WebDriverWait(driver, 10).until(
            EC.visibility_of_element_located((By.CLASS_NAME, 'alert-danger'))):
            self.browser.save_screenshot('Error.png')
            allure.attach(self.browser.get_screenshot_as_png(), name='Error.png',
                          attachment_type=allure.attachment_type.PNG)
            assert False, 'The user is not registered'

        elif self.browser.find_element(By.XPATH, '//h1[text()="My account"]').click():
            True

        # elif WebDriverWait(driver, 10).until(
        #         EC.presence_of_element_located((By.XPATH, '//h1[text()="My account"]'))):
        #     True

    def fill_in_the_input_field(self, id_selector, text):
        self.browser.find_element(By.ID, id_selector).send_keys(text)

    def choise_select(self, select, option):
        self.browser.find_element(By.ID, select).click()
        self.browser.find_element(By.CSS_SELECTOR, option).click()
