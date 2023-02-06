from selenium.webdriver.common.by import By

from page_object.Center.add_description_center_modal import AddDescriptionCenterModal
from page_object.base_page_object import BasePageObject


class AddContactsCenterModal(BasePageObject):
    xpath_center_phone = "//input[@id='contacts_contactТелефон']"
    xpath_next_step_button = "//span[contains(text(),'Наступний крок')]"

    def __init__(self, driver: object):
        super().__init__(driver)

    def enter_center_phone(self, center_phone):
        self.driver.find_element(by=By.XPATH, value=self.xpath_center_phone).send_keys(center_phone)
        return self

    def click_next_step_button(self):
        self.driver.find_element(by=By.XPATH, value=self.xpath_next_step_button).click()
        return AddDescriptionCenterModal(self.driver)
