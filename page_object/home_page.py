import time
from settings import (admin_email,
                      admin_password)

from page_object.base_page_object import BasePageObject
from selenium.webdriver.common.by import By


class HomePage(BasePageObject):
    xpath_profile_menu_button = "//div[contains(@class, 'user-profile')]"
    xpath_enter_button = "//div[contains(text(), 'Увійти')]"
    xpath_email_input = "//input[@id='basic_email']"
    xpath_password_input = "//input[@id='basic_password']"
    xpath_login_button = "//button[contains(@class, 'login-button')]"

    def __init__(self, driver):
        super().__init__(driver)

    def click_drop_down_menu(self):
        self.driver.find_element(by=By.XPATH, value=self.xpath_profile_menu_button).click()
        time.sleep(3)
        return self

    def click_enter_button(self):
        self.driver.find_element(by=By.XPATH, value=self.xpath_enter_button).click()
        time.sleep(3)
        return self

    def enter_admin_credentials(self):
        self.driver.find_element(by=By.XPATH, value=self.xpath_email_input).send_keys(admin_email)
        self.driver.find_element(by=By.XPATH, value=self.xpath_password_input).send_keys(admin_password)
        self.driver.find_element(by=By.XPATH, value=self.xpath_login_button).click()
        time.sleep(3)
        return self
