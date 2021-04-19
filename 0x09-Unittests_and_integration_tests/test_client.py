#!/usr/bin/env python3
'''This module tests the github org functions'''
from parameterized import parameterized
from client import GithubOrgClient
from client import get_json
import unittest
from unittest.mock import patch, PropertyMock


class TestGithubOrgClient(unittest.TestCase):
    '''This class tests some things'''
    @parameterized.expand([
        'google',
        'abc'
    ])
    @patch('client.get_json', return_value={'key': 'value'})
    def test_org(self, org, mock_get_json):
        '''This tests if a mocked up return does some things.'''
        test = GithubOrgClient(org)
        url = "https://api.github.com/orgs/" + org
        self.assertEqual(test.org, {'key': 'value'})
        mock_get_json.assert_called_once_with(url)

    def test_public_repos_url(self):
        '''Tests the GithubOrgClient._public_repos_url function'''
        with patch('client.GithubOrgClient.org',
                   new_callable=PropertyMock) as mockity:
            mockity.return_value = {"repos_url": "http://thisisnotreal.com"}
            test = GithubOrgClient('ThisIsNotARealOrg')
            self.assertEqual(test._public_repos_url,
                             "http://thisisnotreal.com")
