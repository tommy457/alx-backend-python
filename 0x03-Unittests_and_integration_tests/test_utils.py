#!/usr/bin/env python3
"""
Module for Unittests.
"""
from parameterized import parameterized
import unittest
from utils import access_nested_map


class TestAccessNestedMap(unittest.TestCase):
    """ Unittests """

    @parameterized.expand([
        ({"nested_map": {"a": 1}, "path": ("a",)}, 1),
        ({"nested_map": {"a": {"b": 2}}, "path": ("a",)}, {"b": 2}),
        ({"nested_map": {"a": {"b": 2}}, "path": ("a", "b")}, 2),
    ])
    def test_access_nested_map(self, input_data, expected_output):
        """ tests for the access_nested_map method. """
        self.assertEqual(
            access_nested_map(**input_data), expected_output)


if __name__ == "__main__":
    unittest.main()
