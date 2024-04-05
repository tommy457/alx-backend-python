#!/usr/bin/env python3
"""
Module for Unittests.
"""
from parameterized import parameterized
import unittest
from unittest.mock import patch
from utils import access_nested_map, get_json, memoize


class TestAccessNestedMap(unittest.TestCase):
    """ Unittests """

    @parameterized.expand([
        ({"nested_map": {"a": 1}, "path": ("a",)}, 1),
        ({"nested_map": {"a": {"b": 2}}, "path": ("a",)}, {"b": 2}),
        ({"nested_map": {"a": {"b": 2}}, "path": ("a", "b")}, 2),
    ])
    def test_access_nested_map(self, input_data, expected_output):
        """tests for the access_nested_map returns correct expected_output."""
        self.assertEqual(
            access_nested_map(**input_data), expected_output)

    @parameterized.expand([
        ({"nested_map": {}, "path": ("a",)}, "'a'"),
        ({"nested_map": {"a": 1}, "path": ("a", "b")}, "'b'"),
    ])
    def test_access_nested_map_exception(self, input_data, error_msg):
        """ test that a KeyError is raised for the input_data. """
        with self.assertRaises(KeyError) as e:
            access_nested_map(**input_data)
        self.assertEqual(str(e.exception), error_msg)


class TestGetJson(unittest.TestCase):
    """ Unittests """
    @parameterized.expand([
        ({"test_url": "http://example.com", "test_payload": True},),
        ({"test_url": "http://holberton.io", "test_payload": False},),
    ])
    @patch("requests.get", )
    def test_get_json(self, input_data, mock_get):
        """ test that get_json returns the expected result. """
        mock_get.return_value.json.return_value = input_data["test_payload"]

        data = get_json(input_data["test_url"])

        mock_get.assert_called_once_with(input_data["test_url"])
        self.assertEqual(data, input_data["test_payload"])


class TestMemoize(unittest.TestCase):
    """ Unittests """
    def test_memoize(self):
        """ test the correct result is returned. """
        class TestClass:

            def a_method(self):
                return 42

            @memoize
            def a_property(self):
                return self.a_method()

        with patch.object(TestClass, "a_method") as mocked_method:
            obj = TestClass()
            obj.a_property()
            obj.a_property()

        mocked_method.assert_called_once()


if __name__ == "__main__":
    unittest.main()
