import unittest
from unittest.mock import patch
import requests
from main import get_company_information
from dotenv import load_dotenv
import os

load_dotenv() 


class TestCompanyInformation(unittest.TestCase):
    def setUp(self):
        """
        Set up the necessary variables for testing.
        """
        self.api_key = os.getenv("HOUSE_API_KEY")
        self.search_term = "sono"

    @patch.object(requests, 'get')
    def test_get_company_information_success(self, mock_get):
        """
        Test the success scenario of get_company_information function.
        Mocks the API response and verifies that the function returns the expected number of results.
        """
        mock_response = mock_get.return_value
        mock_response.status_code = 200
        mock_response.json.return_value = {
            "total_results": 2,
            "items": [
                {
                    "title": "Sono Company 1",
                    "company_type": "limited",
                    # Add other relevant fields as needed
                },
                {
                    "title": "Sono Company 2",
                    "company_type": "limited",
                    # Add other relevant fields as needed
                }
            ]
        }


        company_information = get_company_information(self.search_term, self.api_key)
        self.assertEqual(len(company_information), 2)

    @patch.object(requests, 'get')
    def test_get_company_information_error(self, mock_get):
        """
        Test the error scenario of get_company_information function.
        Mocks an error response from the API and ensures that the function returns None.
        """
        mock_response = mock_get.return_value
        mock_response.status_code = 500

        company_information = get_company_information(self.search_term, self.api_key)
        self.assertIsNone(company_information)


if __name__ == '__main__':
    unittest.main()
