#!/usr/bin/env python3
'''This module tests the github org functions'''
from parameterized import parameterized, parameterized_class
from client import GithubOrgClient
from client import get_json
import unittest
import requests
from unittest.mock import patch, PropertyMock
from fixtures import TEST_PAYLOAD


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

    @patch('client.get_json')
    def test_public_repos(self, mock_get_json):
        '''Tests the public repos function'''
        with patch('client.GithubOrgClient._public_repos_url',
                   new_callable=PropertyMock) as mockItUp:
            fakeload = {'Date': '11/22/2013',
                        'name': 'zaphod Beeblbrox',
                        'repos_url': 'http://thisisnotreal.com'}
            test = GithubOrgClient('NotReal')
            mock_get_json.return_value = fakeload
            org_name = test.org
            mockItUp.return_value = org_name.get('repos_url')
            self.assertEqual(test._public_repos_url,
                             "http://thisisnotreal.com")
            mock_get_json.assert_called_once()
            mockItUp.assert_called_once()

    @parameterized.expand([
        ({"license": {"key": "my_license"}}, "my_license", True),
        ({"license": {"key": "other_license"}}, "my_license", False)
    ])
    def test_has_license(self, repo, license_key, exp):
        '''Test for the assert license function'''
        test = GithubOrgClient('ThisIsNotARealOrg')
        self.assertEqual(test.has_license(repo, license_key), exp)

@parameterized_class(
    ('org_payload', 'repos_payload', 'expected_repos', 'apache2_repos'),
    [TEST_PAYLOAD[0][0],
     TEST_PAYLOAD[0][1],
     TEST_PAYLOAD[0][2],
     TEST_PAYLOAD[0][3]]
)
class TestIntegrationGithubOrgClient(unittest.TestCase):
    '''Integration testing class'''
    @classmethod
    def setUpClass(cls):
        '''Mock requests.get()'''
        # patch requests.get()
        cls.get_patcher = patch('requests.get')
        # set side_effect
        cls.get_patcher.side_effect = repos_payload
        #start the patcher
        cls.get_patcher.start()

    @classmethod
    def tearDownClass(cls):
        '''"STOP MOCKING ME", requests.get() said'''
        #stop patcher
        cls.get_patcher.stop()
