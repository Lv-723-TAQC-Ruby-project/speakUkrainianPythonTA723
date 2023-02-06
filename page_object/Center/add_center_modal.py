import time

from selenium.common import NoSuchElementException
from selenium.webdriver import Keys
from selenium.webdriver.common.by import By

from page_object.Center.add_contacts_center_modal import AddContactsCenterModal
from page_object.Center.add_location_modal import AddLocationModal
from page_object.base_page_object import BasePageObject


class AddCenterModal(BasePageObject):
    xpath_next_step_button = "//button[@class='ant-btn ant-btn-default next-btn']"
    xpath_error_message = "//div[contains(text(), 'Некоректна назва центру')]"
    xpath_add_center_input = "//input[@id= 'basic_name']"
    xpath_add_center_location = "//span[contains(text(),'Додати локацію')]"
    xpath_location_to_select = "//div[contains(@class, 'ant-checkbox-group location-list')]/div[last(" \
                               ")]/label/span/input"
    xpath_scroll = "//label[@class='ant-checkbox-wrapper ant-checkbox-wrapper-in-form-item'][1]"
    xpath_scroll_selected = "//label[@class='ant-checkbox-wrapper ant-checkbox-wrapper-checked " \
                            "ant-checkbox-wrapper-in-form-item']"

    def __init__(self, driver: object):
        super().__init__(driver)

    def click_add_task(self):
        self.driver.find_element(by=By.XPATH, value=self.xpath_next_step_button).click()
        return AddCenterModal(self.driver)

    def enter_center_name(self, center_name):
        self.driver.find_element(by=By.XPATH, value=self.xpath_add_center_input).send_keys(center_name)
        return self

    def add_center_location(self):
        self.driver.find_element(by=By.XPATH, value=self.xpath_add_center_location).click()
        time.sleep(3)
        return AddLocationModal(self.driver)

    def select_center_location(self):
        self.driver.find_element(by=By.XPATH, value=self.xpath_scroll).click()
        self.driver.find_element(by=By.XPATH, value=self.xpath_scroll_selected).click()
        self.driver.find_element(by=By.XPATH, value=self.xpath_scroll).send_keys(Keys.END)
        time.sleep(2)
        self.driver.find_element(by=By.XPATH, value=self.xpath_location_to_select).click()
        return self

    def click_next_step_button(self):
        self.driver.find_element(by=By.XPATH, value=self.xpath_next_step_button).click()
        return AddContactsCenterModal(self.driver)

    def is_message_error_center_without_name(self):
        try:
            self.driver.find_element(by=By.XPATH, value=self.xpath_error_message)
        except NoSuchElementException:
            return False
        return True
