import time

from page_object.base_page_object import BasePageObject
from selenium.webdriver.common.by import By

class AdvancedSearchPage(BasePageObject):
    xpath_sort_descending_button = "//span[@class='anticon anticon-arrow-up control-sort-arrow']"
    xpath_name_card = "//div[text()='Школа танців Dream Team']"
    xpath_radio_center = "//label[.//span[contains(text(),'Центр')]]//span//input[@type='radio']"
    xpath_last_page = "//li[contains(@class, 'ant-pagination-item')][last()]"
    xpath_last_center = "//div[contains(@class, 'content-center-list content-center-block')]/div[last()]"
    def __init__(self, driver):
        super().__init__(driver)

    def click_sort_descending_button(self):
        self.driver.find_element(by=By.XPATH, value=self.xpath_sort_descending_button).click()
        time.sleep(3)
        return AdvancedSearchPage(self.driver)

    def get_name_of_club(self):
        name_card = self.driver.find_element(by=By.XPATH, value=self.xpath_name_card).text
        return name_card

    def get_name_of_club(self):
        name_card = self.driver.find_element(by=By.XPATH, value=self.xpath_name_card).text
        return name_card

    def click_center_button(self):
        self.driver.find_element(by=By.XPATH, value=self.xpath_radio_center).click()
        time.sleep(3)
        return self

    def is_center_added(self, center_name):
        self.driver.find_element(by=By.XPATH, value=self.xpath_last_page).click()
        time.sleep(3)
        print(self.driver.find_element(by=By.XPATH, value=self.xpath_last_center).text)


