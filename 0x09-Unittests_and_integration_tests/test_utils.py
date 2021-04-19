#!/usr/bin/env python3
"""Generic utilities for github org client.
"""
import json
import requests
import unittest
from unittest.mock import patch
from parameterized import parameterized
from typing import (
    Mapping,
    Sequence,
    Any,
    Dict,
    Callable,
)
from utils import access_nested_map, get_json, memoize


class TestAccessNestedMap(unittest.TestCase):
    '''This class tests mapping methods'''
    @parameterized.expand([
        ({"a": 1}, ["a"], 1),
        ({"a": {"b": 2}}, ["a"], {"b": 2}),
        ({"a": {"b": 2}}, ["a", "b"], 2)
    ])
    def test_access_nested_map(self, nested_map: Mapping,
                               path: Sequence, exp: int) -> Any:
        '''This tests correct inputs to the function'''
        self.assertEqual(access_nested_map(nested_map, path), exp)

    @parameterized.expand([
        ({}, ["a"]),
        ({"a": 1}, ["a", "b"])
    ])
    def test_access_nested_map_exception(self, nested_map: Mapping,
                                         path: Sequence) -> Any:
        '''This tests exception handling'''
        self.assertRaises(KeyError, access_nested_map, nested_map, path)


class TestGetJson(unittest.TestCase):
    '''This class testts the get_json function'''
    @parameterized.expand([
        ("http://example.com", {"payload": True}),
        ("http://holberton.io", {"payload": False}),
    ])
    @patch('test_utils.get_json')
    def test_get_json(self, url, payload, mock_get_json):
        # use dot notation to assign the key word value to the mocked func
        mock_get_json.return_value = payload
        result = mock_get_json(url)
        self.assertEqual(result, payload)


class TestMemoize(unittest.TestCase):
    '''This class tests memoization'''
    def test_memoize(self):
        '''Test the memoize and compare results'''
        class TestClass:
            def a_method(self):
                return 42

            @memoize
            def a_property(self):
                return self.a_method()

        with patch.object(TestClass, 'a_method',
                          return_value=42) as mock_a:
            class_test = TestClass()
            a = class_test.a_property
            b = class_test.a_property
            self.assertEqual(a, 42)
            self.assertEqual(b, 42)
            mock_a.assert_called_once()


if __name__ == '__main__':
    unittest.main()
