import time

from page_object.base_page_object import BasePageObject
from selenium.webdriver.common.by import By
from page_object.ProfilePO.edit_profile_modal import EditProfileModale

class MyProfilePage(BasePageObject):
    xpath_edit_profile_button = "//span[text()='Редагувати профіль']"

    def __init__(self, driver):
        super().__init__(driver)

    def click_edit_profile_button(self):
        self.driver.find_element(by=By.XPATH, value=self.xpath_edit_profile_button).click()
        time.sleep(3)
        return EditProfileModale(self.driver)