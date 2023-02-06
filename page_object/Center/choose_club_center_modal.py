import time

from selenium.webdriver import Keys
from selenium.webdriver.common.by import By

from page_object.admin_profile_page import AdminProfilePage
from page_object.base_page_object import BasePageObject


class ChooseClubCenterModal(BasePageObject):
    xpath_list_of_clubs = "//div[@class='checkbox-item'][1]/label"
    xpath_club_to_select = "//div[@class='checkbox-item'][last()]/label"
    xpath_finish_button = "//button[@class='finish-btn']"

    def __init__(self, driver: object):
        super().__init__(driver)

    def select_club(self):
        self.driver.find_element(by=By.XPATH, value=self.xpath_list_of_clubs).click()
        self.driver.find_element(by=By.XPATH, value=self.xpath_list_of_clubs).click()
        self.driver.find_element(by=By.XPATH, value=self.xpath_list_of_clubs).send_keys(Keys.END)
        self.driver.find_element(by=By.XPATH, value=self.xpath_club_to_select).click()
        return self

    def click_finish_button(self):
        self.driver.find_element(by=By.XPATH, value=self.xpath_finish_button).click()
        time.sleep(5)
        return AdminProfilePage(self.driver)
