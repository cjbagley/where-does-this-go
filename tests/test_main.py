import unittest

from src.wdtg.wdtg import get_url_end_location


class TestFindUrlEndpoint(unittest.TestCase):
    def test_find_correct_url_endpoint(self):
        endpoint = 'http://bbc.co.uk'
        expected = 'http://www.bbc.co.uk'
        result = get_url_end_location(endpoint)

        self.assertEqual(result, expected)

    def test_incorrect_url_given(self):
        endpoint = 'bbc.co.uk'

        self.assertRaises(ValueError, get_url_end_location, endpoint)
