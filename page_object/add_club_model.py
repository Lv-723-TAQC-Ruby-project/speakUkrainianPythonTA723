from selenium.webdriver.common.keys import Keys
from page_object.base_page_object import BasePageObject
from selenium.webdriver.common.by import By


class AddClubModel(BasePageObject):

    xpath_name_club_input = "//input[@id='basic_name']"
    xpath_category_by_name = "//input[@value='Спортивні секції']"
    xpath_age_from = "//input[@id='basic_ageFrom']"
    xpath_age_to = "//input[@id='basic_ageTo']"
    xpath_next_step = "//span[contains(text(),'Наступний крок')]"
    xpath_phone_number = "//input[@id='basic_contactТелефон']"
    xpath_description = "//input[@id='basic_description']"

    def __init__(self, driver):
        super().__init__(driver)

    def enter_name_club(self, name):
        self.driver.find_element(by=By.XPATH, value=self.xpath_name_club_input).send_keys(Keys.CONTROL + "a")
        self.driver.find_element(by=By.XPATH, value=self.xpath_name_club_input).send_keys(Keys.DELETE)
        self.driver.find_element(by=By.XPATH, value=self.xpath_name_club_input).send_keys(name)
        return self

    def select_category_by_name(self):
        self.driver.find_element(by=By.XPATH, value=self.xpath_category_by_name).click()
        return self

    def enter_age_from(self, age_from):
        self.driver.find_element(by=By.XPATH, value=self.xpath_age_from).send_keys(age_from)
        return self

    def enter_age_to(self, age_to):
        self.driver.find_element(by=By.XPATH, value=self.xpath_age_to).send_keys(age_to)
        return self

    def click_next_step(self):
        self.driver.find_element(by=By.XPATH, value=self.xpath_next_step).click()
        return self

    def enter_phone_number(self, phone_number):
        self.driver.find_element(by=By.XPATH, value=self.xpath_phone_number).send_keys(phone_number)
        return self

    def enter_description(self, description):
        self.driver.find_element(by=By.XPATH, value=self.xpath_description).send_keys(description)
        return self