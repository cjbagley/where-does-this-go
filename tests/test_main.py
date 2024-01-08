import unittest
from src.wdtg.wdtg import get_url_end_location, is_valid_url, sanitise_url


class TestMain(unittest.TestCase):
    def test_find_correct_url_endpoint(self):
        endpoint = 'https://bbc.co.uk'
        expected = 'https://www.bbc.co.uk'
        result = get_url_end_location(endpoint)
        self.assertEqual(result, expected)

    def test_incorrect_url_given(self):
        endpoint = 'bbc.co.uk'
        self.assertRaises(ValueError, get_url_end_location, endpoint)

    def test_sanitise_url(self):
        value_1 = 'https://bbc.co.uk'
        expected_1 = 'https://bbc.co.uk'
        result_1 = sanitise_url(value_1)
        self.assertEqual(result_1, expected_1)

        value_2 = 'https://bbc.co.uk?test=2&3 \';`; DROP *'
        expected_2 = 'https://bbc.co.uk?test=2&3'
        result_2 = sanitise_url(value_2)
        self.assertEqual(result_2, expected_2)

    def test_is_valid_url(self):
        value_1 = 'https://bbc.co.uk'
        expected_1 = True
        result_1 = is_valid_url(value_1)
        self.assertEqual(expected_1, result_1)

        value_2 = 'bbc.co.uk'
        expected_2 = False
        result_2 = is_valid_url(value_2)
        self.assertEqual(expected_2, result_2)
