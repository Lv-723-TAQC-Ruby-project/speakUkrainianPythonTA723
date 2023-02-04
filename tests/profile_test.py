import unittest

from selenium import webdriver

from page_object.home_page import HomePage
from settings.local_settings import admin_email, admin_password
from settings.settings import base_web_url
from page_object.my_profile_page import MyProfilePage
from page_object.edit_profile_modal import EditProfileModale


class ProfileTest(unittest.TestCase):
    driver = None

    @classmethod
    def setUpClass(cls):
        cls.driver = webdriver.Chrome()
        cls.driver.maximize_window()
        cls.driver.get(base_web_url)

    @classmethod
    def tearDownClass(cls):
        cls.driver.quit()

    def test_message_about_incorrectly_entered_last_name(self):
        error_text_more_25_characters = "Прізвище не може містити більше, ніж 25 символів"
        invalid_text_25_characters = "AfBbCcDdEeFfGgHhIiJjKkLlMmNn"
        error_text_numbers = "Прізвище не може містити цифри"
        invalid_text_numbers = "12345"
        error_text_special_characters = "Прізвище не може містити спеціальні символи"
        invalid_text_special_characters = "!@#$%^&,"
        error_25_characters = HomePage(self.driver) \
            .click_drop_down_menu() \
            .click_enter_button() \
            .enter_admin_credentials(admin_email, admin_password)\
            .click_drop_down_menu()\
            .click_my_profile_button()\
            .click_edit_profile_button()\
            .delete_last_name()\
            .enter_last_name(invalid_text_25_characters)\
            .get_error_text()
        self.assertEqual(error_25_characters, error_text_more_25_characters)

        EditProfileModale(self.driver)\
            .delete_last_name()\
            .enter_last_name(invalid_text_numbers)\
            .get_error_text()
        self.assertIn(error_text_numbers, self.driver.page_source)

        EditProfileModale(self.driver) \
            .delete_last_name() \
            .enter_last_name(invalid_text_special_characters) \
            .get_error_text()
        self.assertTrue(error_text_special_characters)



