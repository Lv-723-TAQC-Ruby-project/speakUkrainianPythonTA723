import unittest
from settings.settings import base_web_url

from selenium import webdriver

from page_object.home_page import HomePage

from settings.settings import (admin_email,
                               admin_password)


class LoginHomePageTest(unittest.TestCase):

    driver = None

    @classmethod
    def setUpClass(cls):
        cls.driver = webdriver.Chrome()
        cls.driver.maximize_window()
        cls.driver.get(base_web_url)

    @classmethod
    def tearDownClass(cls):
        cls.driver.quit()

    def test_login(self):
        HomePage(self.driver) \
            .click_drop_down_menu() \
            .click_enter_button() \
            .enter_admin_credentials(admin_email, admin_password) \
            .click_drop_down_menu()
        self.assertIn("Додати центр", self.driver.page_source)
