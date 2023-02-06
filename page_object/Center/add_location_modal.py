import time

from page_object.base_page_object import BasePageObject
from selenium.webdriver.common.by import By


class AddLocationModal(BasePageObject):
    xpath_add_location_button = "//div[@class='add-club-content-footer add-club-add-location-button']//button[" \
                                "@type='submit']"
    xpath_location_name = "//input[@id='name']"
    xpath_location_address = "//input[@id='address']"
    xpath_location_coordinates = "//input[@id='coordinates']"
    xpath_location_phone = "//input[@id='phone']"
    xpath_choose_city = "//input[@id='cityName']"

    def __init__(self, driver: object):
        super().__init__(driver)

    def enter_location_name(self, location_name):
        self.driver.find_element(by=By.XPATH, value=self.xpath_location_name).send_keys(location_name)
        return self

    def enter_location_address(self, location_address):
        self.driver.find_element(by=By.XPATH, value=self.xpath_location_address).send_keys(location_address)
        return self

    def enter_location_coordinates(self, location_coordinates):
        self.driver.find_element(by=By.XPATH, value=self.xpath_location_coordinates).send_keys(location_coordinates)
        return self

    def enter_location_phone(self, location_phone):
        self.driver.find_element(by=By.XPATH, value=self.xpath_location_phone).send_keys(location_phone)
        return self

    def choose_location_city(self, city_name):
        self.driver.find_element(by=By.XPATH, value=self.xpath_choose_city).click()
        time.sleep(1)
        xpath_with_city = "//div[@class ='ant-select-item-option-content'][contains(text(), '" + city_name + "')]"
        self.driver.find_element(by=By.XPATH, value=xpath_with_city).click()
        return self

    def click_add_location_button(self):
        self.driver.find_element(by=By.XPATH, value=self.xpath_add_location_button).click()
        time.sleep(3)
        from page_object.Center.add_center_modal import AddCenterModal
        return AddCenterModal(self.driver)
