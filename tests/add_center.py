import unittest

from selenium import webdriver

from page_object.home_page import HomePage
from settings.settings import (admin_email,
                               admin_password)
from settings.settings import base_web_url


class CheckIfErrorAppearsAfterEmptyFieldsTest(unittest.TestCase):
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
        message = HomePage(self.driver) \
            .click_drop_down_menu() \
            .click_enter_button() \
            .enter_admin_credentials(admin_email, admin_password) \
            .click_drop_down_menu() \
            .click_add_center_button() \
            .is_message_error_center_without_name

        self.assertTrue(message,
                        "Error message 'Некоректна назва центру’ doesn't appear under 'Назва центру' field with empty 'Назва центру' field")
