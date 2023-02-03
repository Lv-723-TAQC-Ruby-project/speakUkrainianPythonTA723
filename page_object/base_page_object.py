from selenium.webdriver.common.by import By


class BasePageObject:
    def __init__(self, driver):
        self.driver = driver


    def message(self):
        self.driver.find_element(by=By.XPATH, value="//div[@class='ant-message']").text()
        return self