import unittest
import requests


class GetCategoryById(unittest.TestCase):
    BASE_API_URL = "https://speak-ukrainian.org.ua/dev/api/"
    category_id = 2

    def test_get_category_by_id(self):
        response = requests.get(self.BASE_API_URL + "category/" + str(self.category_id))
        response_json = response.json()
        assert response.status_code == 200
        assert response_json.get("name") == "Танці, хореографія"
