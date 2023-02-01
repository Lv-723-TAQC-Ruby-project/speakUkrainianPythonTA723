import unittest
from test import clubName
from test import club
from test import email
from test import password
class MyTestCase(unittest.TestCase):
    def test_search(self):
        self.assertEqual(club, clubName)
        self.assertEqual(email, "admin@gmail.com")
        self.assertEqual(password, "1234567")
        # add assertion here


if __name__ == '__main__':
    unittest.main()
