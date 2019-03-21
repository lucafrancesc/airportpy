from unittest.mock import patch
from parse_api import Api
import unittest


class TestApi(unittest.TestCase):
    def setUp(self):
        self.api = Api()
        self.response = self.api.api_response()
        self.parsed_response = self.api.parsed_response()

    @patch('parse_api.requests.get')

    def test_response(self, mock_get):
        mock_get.return_value.status_code = 200
        self.assertEqual(self.response.status_code, 200)


if __name__ == "__main__":
    unittest.main()
