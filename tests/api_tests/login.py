import unittest
import requests


from settings.settings import admin_email,admin_password

class LoginTest(unittest.TestCase):

    def test_login(self):
        body = {'email': admin_email, 'password' : admin_password }

        response = requests.post("https://speak-ukrainian.org.ua/dev/api/signin",json=body)

        assert response.status_code == 200
        assert response.json().get("roleName") == "ROLE_ADMIN"
        assert response.json().get("id") == 1