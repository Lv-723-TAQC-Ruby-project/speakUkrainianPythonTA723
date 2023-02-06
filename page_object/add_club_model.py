from selenium.webdriver.common.keys import Keys
from page_object.base_page_object import BasePageObject
from selenium.webdriver.common.by import By


class AddClubModel(BasePageObject):

    xpath_name_club_input = "//input[@id='basic_name']"

    def __init__(self, driver):
        super().__init__(driver)

    def enter_name_club(self, name):
        self.driver.find_element(by=By.XPATH, value=self.xpath_name_club_input).send_keys(Keys.CONTROL + "a")
        self.driver.find_element(by=By.XPATH, value=self.xpath_name_club_input).send_keys(Keys.DELETE)
        self.driver.find_element(by=By.XPATH, value=self.xpath_name_club_input).send_keys(name)
        return self
