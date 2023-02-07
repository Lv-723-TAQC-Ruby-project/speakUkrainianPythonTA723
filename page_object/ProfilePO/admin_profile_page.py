import time

from selenium.webdriver.common.by import By

from page_object.base_page_object import BasePageObject


class AdminProfilePage(BasePageObject):
    xpath_click_choose_center = "//div[@class='ant-select club-center-select ant-select-single ant-select-show-arrow']"
    xpath_select_center = "//div[@class='ant-select-item ant-select-item-option']"
    xpath_last_page = "//li[contains(@class, 'ant-pagination-item')][last()]"
    xpath_last_center_title = "//div[contains(@class, 'ant-space-item')][last()]/div/div/div/div/div/div/div[2]"

    def __init__(self, driver):
        super().__init__(driver)

    def get_added_center_title(self):
        return self.driver.find_element(by=By.XPATH, value=self.xpath_last_center_title).text

    def switch_to_centers(self):
        self.driver.find_element(by=By.XPATH, value=self.xpath_click_choose_center).click()
        time.sleep(3)
        self.driver.find_element(by=By.XPATH, value=self.xpath_select_center).click()
        time.sleep(3)
        return self

    def get_last_page(self):
        self.driver.find_element(by=By.XPATH, value=self.xpath_last_page).click()
        time.sleep(3)
        return self

