import unittest
from unittest.mock import MagicMock

import requests

from homework4.task2 import count_dots_on_i


class TestCountDots(unittest.TestCase):
    def test_count_dots_on_i(self):
        url = "http://www.example.com"
        count_dots_on_i = MagicMock(return_value=10)
        self.assertEqual(count_dots_on_i(url), 10)

    def test_count_dots_with_exception(self):
        url = "http://www.example.com"
        requests.get = MagicMock(side_effect=ConnectionError)
        with self.assertRaises(ValueError, msg=f"Unreachable {url}"):
            count_dots_on_i(url)
