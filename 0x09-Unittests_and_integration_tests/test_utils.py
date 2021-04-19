#!/usr/bin/env python3
"""Generic utilities for github org client.
"""
import requests
from parameterized import parameterized
from functools import wraps
from typing import (
    Mapping,
    Sequence,
    Any,
    Dict,
    Callable,
)
import unittest
from unittest import mock

__all__ = [
    "access_nested_map",
    "get_json",
    "memoize",
]


def access_nested_map(nested_map: Mapping, path: Sequence) -> Any:
    """Access nested map with key path.
    Parameters
    ----------
    nested_map: Mapping
        A nested map
    path: Sequence
        a sequence of key representing a path to the value
    Example
    -------
    >>> nested_map = {"a": {"b": {"c": 1}}}
    >>> access_nested_map(nested_map, ["a", "b", "c"])
    1
    """
    for key in path:
        if not isinstance(nested_map, Mapping):
            raise KeyError(key)
        nested_map = nested_map[key]

    return nested_map


def get_json(url: str) -> Dict:
    """Get JSON from remote URL.
    """
    response = requests.get(url)
    return response.json()


def memoize(fn: Callable) -> Callable:
    """Decorator to memoize a method.
    Example
    -------
    class MyClass:
        @memoize
        def a_method(self):
            print("a_method called")
            return 42
    >>> my_object = MyClass()
    >>> my_object.a_method
    a_method called
    42
    >>> my_object.a_method
    42
    """
    attr_name = "_{}".format(fn.__name__)

    @wraps(fn)
    def memoized(self):
        """"memoized wraps"""
        if not hasattr(self, attr_name):
            setattr(self, attr_name, fn(self))
        return getattr(self, attr_name)

    return property(memoized)


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
    @mock.patch('test_utils.get_json')
    def test_get_json(self, url, payload, mock_get_json):
        # use dot notation to assign the key word value to the mocked func
        mock_get_json.return_value = payload
        result = mock_get_json(url)
        self.assertEqual(result, payload)


class TestMemoize(unittest.TestCase):
    '''This class tests memoization'''
    def test_memoize(self):
        '''Test the memoize'''
        class TestClass:

            def a_method(self):
                '''This is part of the memoize class'''
                return 42

            @memoize
            def a_property(self):
                '''So is this one'''
                return self.a_method()

        with mock.patch.object(TestClass, 'a_method') as mock_a:
            class_test = TestClass()
            class_test.a_property
            class_test.a_property
            mock_a.assert_called_once()


if __name__ == '__main__':
    unittest.main()
