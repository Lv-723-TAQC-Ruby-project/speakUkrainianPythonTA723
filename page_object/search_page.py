from page_object.base_page_object import BasePageObject
from selenium.webdriver.common.by import By

class SearchPage(BasePageObject):

    xpath_name_of_club = "//div[@class='name']"

    def __init__(self, driver):
        super().__init__(driver)

    def get_name_of_club(self):
        name = self.driver.find_element(by=By.XPATH, value=self.xpath_name_of_club).text
        return name


