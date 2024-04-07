#!/usr/bin/env python3
"""
Unittests for the  client module.
"""
from client import GithubOrgClient
from parameterized import parameterized
import unittest
from unittest.mock import patch, PropertyMock


class TestGithubOrgClient(unittest.TestCase):
    """ Tests for Githib org client. """

    @parameterized.expand([
        ("google"), ("abc")
    ])
    @patch("client.get_json")
    def test_org(self, input_data, mock_get_json):
        """ Test that `org` method returns the expected  correct value. """
        obj = GithubOrgClient(input_data)
        obj.org()
        test_url = obj.ORG_URL.format(org=input_data)

        mock_get_json.assert_called_once_with(test_url)

    @parameterized.expand([
        ({"repos_url": "google"}, "google"),
    ])
    def test_public_repos_url(self, payload, expected_output):
        """Test that `_public_repos_url` method returns the expected value"""
        with patch("client.GithubOrgClient.org",
                   new_callable=PropertyMock) as mocked_property:
            mocked_property.return_value = payload
            obj = GithubOrgClient("test")

            self.assertEqual(obj._public_repos_url, expected_output)

    @parameterized.expand([
        ([{"name": "google"}, {"name": "abc"}], ["google", "abc"])
    ])
    @patch("client.get_json")
    def test_public_repos(self, payload, expected_output, mock_get_json):
        """ Test for the `public_repos` method returns the expected value. """
        mock_get_json.return_value = payload
        with patch("client.GithubOrgClient._public_repos_url",
                   new_callable=PropertyMock) as mocked_property:
            mocked_property.return_value = "repos_url"

            obj = GithubOrgClient("test")
            self.assertEqual(obj.public_repos(), expected_output)

            mock_get_json.assert_called_once()
            mocked_property.assert_called_once()

    @parameterized.expand([
        ({"license": {"key": "my_license"}}, "my_license", True),
        ({"license": {"key": "other_license"}}, "my_license", False)
    ])
    def test_has_license(self, repo, license_key, expected):
        """ Test for the `has_license` method returns the expected  value. """
        self.assertEqual(GithubOrgClient.has_license(repo, license_key),
                         expected)


@parameterized_class(("org_payload",
                      "repos_payload",
                      "expected_repos",
                      "apache2_repos",),
                     fixtures.TEST_PAYLOAD)
class TestIntegrationGithubOrgClient(unittest.TestCase):
    """ Integration tests """
    @classmethod
    def setUpClass(cls):
        """ method called before any tests have been run. """
        config = {'return_value.json.side_effect': [cls.org_payload,
                                                    cls.repos_payload,
                                                    cls.expected_repos,
                                                    cls.apache2_repos]}
        cls.get_patcher = patch('requests.get', **config)
        cls.get_patcher.start()
        cls.obj = GithubOrgClient("google")

    def test_public_repos(self):
        """ Test thet  `public_repos` return correct output. """
        self.assertEqual(self.obj.public_repos(), self.expected_repos)

    def test_public_repos_with_license(self):
        """ Test thet  `public_repos` return correct output with license. """

        self.assertEqual(
                self.obj.public_repos("apache-2.0"), self.apache2_repos
        )

    @classmethod
    def tearDownClass(cls):
        """ method called after all tests have been run. """
        cls.get_patcher.stop()


if __name__ == "__main__":
    unittest.main()
