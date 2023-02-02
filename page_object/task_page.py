import time

from page_object.base_page_object import BasePageObject
from selenium.webdriver.common.by import By

class TaskPage(BasePageObject):
    xpath_add_task_button = "//button[contains(@class, 'add-btn')]"

    def __init__(self, driver: object) -> object:
        super().__init__(driver)

    def click_add_task(self):
        self.driver.find_element(by=By.XPATH, value=self.xpath_add_task_button).click()
        time.sleep(4)
        return self