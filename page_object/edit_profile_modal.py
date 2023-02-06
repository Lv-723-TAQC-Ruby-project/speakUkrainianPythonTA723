import time

from page_object.base_page_object import BasePageObject
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

class EditProfileModale(BasePageObject):
    xpath_edit_last_name_field = "//input[@id='edit_lastName']"
    xpath_error_text = "//div[@class='ant-form-item-explain-error']"

    def __init__(self, driver):
        super().__init__(driver)

    def delete_last_name(self):
        self.driver.find_element(by=By.XPATH, value=self.xpath_edit_last_name_field).send_keys(Keys.CONTROL + "a")
        self.driver.find_element(by=By.XPATH, value=self.xpath_edit_last_name_field).send_keys(Keys.DELETE)
        time.sleep(3)
        return self

    def enter_last_name(self, last_name):
        self.driver.find_element(by=By.XPATH, value=self.xpath_edit_last_name_field).send_keys(last_name)
        time.sleep(3)
        return self

    def get_error_text(self):
        error_text = self.driver.find_element(by=By.XPATH, value=self.xpath_error_text).text
        return error_text




