import unittest
from datetime import datetime

from selenium import webdriver

from page_object.home_page import HomePage
from settings.settings import (admin_email,
                               admin_password)
from settings.settings import base_web_url


class CheckIfErrorWhenAddCenterWithoutName(unittest.TestCase):
    driver = None
    dt = datetime.now()
    center_name = "New CenterPO Name " + str(dt)
    phone_number = "0661111111"

    @classmethod
    def setUpClass(cls):
        cls.driver = webdriver.Chrome()
        cls.driver.maximize_window()
        cls.driver.get(base_web_url)

    @classmethod
    def tearDownClass(cls):
        cls.driver.quit()

    def test_add_center_without_name(self):
        message = HomePage(self.driver) \
            .click_drop_down_menu() \
            .click_enter_button() \
            .enter_admin_credentials(admin_email, admin_password) \
            .click_drop_down_menu() \
            .click_add_center_button() \
            .is_message_error_center_without_name

        self.assertTrue(message,
                        "Error message 'Некоректна назва центру’ doesn't appear under 'Назва центру' field with empty "
                        "'Назва центру' field")

    def test_add_center_with_valid_data(self):
        added_center_title = HomePage(self.driver) \
            .click_drop_down_menu() \
            .click_enter_button() \
            .enter_admin_credentials(admin_email, admin_password) \
            .click_drop_down_menu() \
            .click_add_center_button() \
            .enter_center_name(self.center_name) \
            .add_center_location() \
            .enter_location_name("New Location name " + str(self.dt)) \
            .enter_location_address("New Location address") \
            .enter_location_coordinates("49.9935, 36.2304") \
            .enter_location_phone(self.phone_number) \
            .choose_location_city("Київ") \
            .click_add_location_button() \
            .select_center_location() \
            .click_next_step_button() \
            .enter_center_phone(self.phone_number) \
            .click_next_step_button() \
            .add_description(
            "There are many variations of passages of Lorem Ipsum available, but the majority have suffered "
            "alteration in some form, by injected humour, or randomised words which don't look even slightly "
            "believable. If you are going to use a passage of Lorem Ipsum, you need to be sure there isn't anything "
            "embarrassing hidden in the middle of text. All the Lorem Ipsum generators on the Internet tend to repeat "
            "predefined chunks as necessary, making this the first true generator on") \
            .click_next_step_button() \
            .select_club() \
            .click_finish_button()\
            .switch_to_centers()\
            .get_last_page()\
            .get_added_center_title()

        self.assertEqual(added_center_title, self.center_name)
