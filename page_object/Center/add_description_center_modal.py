from selenium.webdriver.common.by import By

from page_object.Center.choose_club_center_modal import ChooseClubCenterModal
from page_object.base_page_object import BasePageObject


class AddDescriptionCenterModal(BasePageObject):
    xpath_add_description = "//textarea[@id='basic_description']"
    xpath_next_step_button = "//span[contains(text(),'Наступний крок')]"

    def __init__(self, driver: object):
        super().__init__(driver)

    def add_description(self, description):
        self.driver.find_element(by=By.XPATH, value=self.xpath_add_description).send_keys(description)
        return self

    def click_next_step_button(self):
        self.driver.find_element(by=By.XPATH, value=self.xpath_next_step_button).click()
        return ChooseClubCenterModal(self.driver)
