from selenium.common import NoSuchElementException

from page_object.base_page_object import BasePageObject
from selenium.webdriver.common.by import By


class AddCenterModal(BasePageObject):
    xpath_next_step_button = "//button[@class='ant-btn ant-btn-default next-btn']"
    xpath_error_message = "//div[contains(text(), 'Некоректна назва центру')]"

    def __init__(self, driver: object) -> object:
        super().__init__(driver)

    def click_add_task(self):
        self.driver.find_element(by=By.XPATH, value=self.xpath_next_step_button).click()
        return AddCenterModal(self.driver)

    def is_message_error_center_without_name(self):
        try:
            self.driver.find_element(by=By.XPATH, value=self.xpath_error_message)
        except NoSuchElementException:
            return False
        return True
