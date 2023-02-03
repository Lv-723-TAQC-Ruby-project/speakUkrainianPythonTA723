import time

from page_object.home_page import HomePage
from settings.settings import (admin_email,
                               admin_password)

from page_object.base_page_object import BasePageObject
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains


class RegisterModel(BasePageObject):
    xpath_name_input = "//input[@id='firstName']"
    xpath_last_name_input = "//input[@id='lastName']"
    xpath_user_pass_input = "//input[@id='password']"
    xpath_confirm_pass_input = "//input[@id='confirm']"
    xpath_exit_button = "//button[contains(@class, 'ant-modal-close')]"
    xpath_phone_input = "//input[@id='phone']"
    xpath_user_email_input = "//input[@id='email']"
    xpath_content = "//span[contains(text(), 'Контент')]"
    xpath_challenges = "//span[contains(text(), 'Челенджі')]"
    xpath_task = "//a[contains(text(), 'Завдання')]"


    def __init__(self, driver):
        super().__init__(driver)

    def enter_register_data(self):
            self.driver.find_element(by=By.XPATH, value=self.xpath_name_input).send_keys("Daisy")
            self.driver.find_element(by=By.XPATH, value=self.xpath_last_name_input).send_keys("Test")
            self.driver.find_element(by=By.XPATH, value=self.xpath_user_email_input).send_keys("daisy@gmail.com")
            self.driver.find_element(by=By.XPATH, value=self.xpath_phone_input).send_keys("0673456785")
            self.driver.find_element(by=By.XPATH, value=self.xpath_user_pass_input).send_keys("123456789")
            self.driver.find_element(by=By.XPATH, value=self.xpath_confirm_pass_input).send_keys("123456789")
            return self

    def click_exit_button(self):
            self.driver.find_element(by=By.XPATH, value=self.xpath_exit_button).click()
            time.sleep(3)
            return HomePage(self.driver)