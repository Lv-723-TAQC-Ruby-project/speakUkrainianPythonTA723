import unittest
import requests

class TestRegistration(unittest.TestCase):
    def test_resgistration(self):
        body = {"id": 25,"email": "daisy@gmail.com", "firstName":"Daisy","lastName" : "Test",
                "phone":"0678954127", "password": "123456789",
                "roleName":"ROLE_USER","verificationCode":"123456","urlLogo":"urlLogo","status": "true" }

        response = requests.post("https://speak-ukrainian.org.ua/dev/api/signup",json=body)

        assert response.status_code == 400
        assert response.json().get("message") == "password must contain at least one number and special symbol and password must contain at least one uppercase and lowercase letter"