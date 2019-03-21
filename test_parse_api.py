from unittest.mock import patch
from parse_api import Api
import unittest


class TestApi(unittest.TestCase):
    def setUp(self):
        self.api = Api()

    def test_request_response(self):
        response = self.api.api_response()
        self.assertEqual(response.status_code, 200)

if __name__ == "__main__":
    unittest.main()
