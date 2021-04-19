#!/usr/bin/env python3
'''This module tests the github org functions'''
from parameterized import parameterized
from client import GithubOrgClient
from utils import get_json
import unittest
from unittest.mock import patch


class TestGithubOrgClient(unittest.TestCase):
    '''This class tests some things'''
    @parameterized.expand([
        'google',
        'abc'
    ])
    @patch('get_json', return_value={'key': 'value'})
    def test_org(self, org, mock_get_json):
        '''This tests if a mocked up return does some things.'''
        test = GithubOrgClient(org)
        url = "https://api.github.com/orgs/" + org
        self.assertEqual(test_obj.org, {'key': 'value'})
        mock_get_json.assert_called_once_with(url)
