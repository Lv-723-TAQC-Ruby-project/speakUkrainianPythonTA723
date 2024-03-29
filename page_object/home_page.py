import time

from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.by import By

from page_object.CenterPO.add_center_modal import AddCenterModal
from page_object.add_club_model import AddClubModel
from page_object.advanced_search_page import AdvancedSearchPage
from page_object.base_page_object import BasePageObject
from page_object.ProfilePO.my_profile_page import MyProfilePage
from page_object.register_model import RegisterModel
from page_object.search_page import SearchPage
from page_object.TaskPO.task_page import TaskPage


class HomePage(BasePageObject):
    xpath_profile_menu_button = "//div[contains(@class, 'user-profile')]"
    xpath_enter_button = "//div[contains(text(), 'Увійти')]"
    xpath_register_button = "//div[contains(text(), 'Зареєструватися')]"
    xpath_email_input = "//input[@id='basic_email']"
    xpath_password_input = "//input[@id='basic_password']"
    xpath_login_button = "//button[contains(@class, 'login-button')]"
    xpath_name_input = "//input[@id='firstName']"
    xpath_last_name_input = "//input[@id='lastName']"
    xpath_user_pass_input = "//input[@id='password']"
    xpath_confirm_pass_input = "//input[@id='confirm']"
    xpath_exit_button = "/html/body/div[6]/div/div[2]/div/div[2]/button/span/span"
    xpath_phone_input = "//input[@id='phone']"
    xpath_user_email_input = "//input[@id='email']"
    xpath_content = "//span[contains(text(), 'Контент')]"
    xpath_challenges = "//span[contains(text(), 'Челенджі')]"
    xpath_task = "//a[contains(text(), 'Завдання')]"
    xpath_search_input = "//input[@type='search']"
    xpath_search_button = "//span[@aria-label='search']"
    xpath_advanced_search_button = "//span[@title='Розширений пошук']"
    xpath_my_profile_button = "//a[contains(text(), 'Особистий кабінет')]"
    xpath_add_club_button = "//span[@class='ant-dropdown-menu-title-content']/div[text()='Додати гурток']"
    xpath_add_center_button = "//span[@class='ant-dropdown-menu-title-content']/div[text()='Додати центр']"

    def __init__(self, driver):
        super().__init__(driver)

    def click_drop_down_menu(self):
        self.driver.find_element(by=By.XPATH, value=self.xpath_profile_menu_button).click()
        time.sleep(3)
        return self

    def click_enter_button(self):
        self.driver.find_element(by=By.XPATH, value=self.xpath_enter_button).click()
        time.sleep(3)
        return self

    def click_register_button(self):
        self.driver.find_element(by=By.XPATH, value=self.xpath_register_button).click()
        time.sleep(3)
        return RegisterModel(self.driver)

    def enter_admin_credentials(self, admin_email, admin_password):
        self.driver.find_element(by=By.XPATH, value=self.xpath_email_input).send_keys(admin_email)
        self.driver.find_element(by=By.XPATH, value=self.xpath_password_input).send_keys(admin_password)
        self.driver.find_element(by=By.XPATH, value=self.xpath_login_button).click()
        time.sleep(5)
        return self

    def click_add_center_button(self):
        self.driver.find_element(by=By.XPATH, value=self.xpath_add_center_button).click()
        time.sleep(3)
        return AddCenterModal(self.driver)

    def add_task(self):
        el1 = self.driver.find_element(by=By.XPATH, value=self.xpath_content)
        actions = ActionChains(self.driver)
        actions.move_to_element(el1).perform()
        time.sleep(1)
        el2 = self.driver.find_element(by=By.XPATH, value=self.xpath_challenges)
        actions.move_to_element(el2).perform()
        time.sleep(1)
        el3 = self.driver.find_element(by=By.XPATH, value=self.xpath_task)
        actions.click(el3).perform()
        time.sleep(1)
        return TaskPage(self.driver)

    def enter_search_word(self, key_word):
        self.driver.find_element(by=By.XPATH, value=self.xpath_search_input).send_keys(key_word)
        return self

    def click_search_button(self):
        self.driver.find_element(by=By.XPATH, value=self.xpath_search_button).click()
        time.sleep(3)
        return SearchPage(self.driver)

    def click_advanced_search_button(self):
        self.driver.find_element(by=By.XPATH, value=self.xpath_advanced_search_button).click()
        time.sleep(4)
        return AdvancedSearchPage(self.driver)

    def click_my_profile_button(self):
        self.driver.find_element(by=By.XPATH, value=self.xpath_my_profile_button).click()
        time.sleep(2)
        return MyProfilePage(self.driver)

    def click_add_club_button(self):
        self.driver.find_element(by=By.XPATH, value=self.xpath_add_club_button).click()
        return AddClubModel(self.driver)
