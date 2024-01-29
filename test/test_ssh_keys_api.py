# coding: utf-8

"""
    Foreman (params in:formData)

     <p>Foreman API v2 is currently the default API version.</p>   # noqa: E501

    OpenAPI spec version: v2

    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


from __future__ import absolute_import

import unittest

import pyforeman
from pyforeman.api.ssh_keys_api import SshKeysApi  # noqa: E501
from pyforeman.rest import ApiException


class TestSshKeysApi(unittest.TestCase):
    """SshKeysApi unit test stubs"""

    def setUp(self):
        self.api = pyforeman.api.ssh_keys_api.SshKeysApi()  # noqa: E501

    def tearDown(self):
        pass

    def test_delete_users_user_id_ssh_keys_id(self):
        """Test case for delete_users_user_id_ssh_keys_id

        Delete an SSH key for a user  # noqa: E501
        """
        pass

    def test_get_users_user_id_ssh_keys(self):
        """Test case for get_users_user_id_ssh_keys

        List all SSH keys for a user  # noqa: E501
        """
        pass

    def test_get_users_user_id_ssh_keys_id(self):
        """Test case for get_users_user_id_ssh_keys_id

        Show an SSH key from a user  # noqa: E501
        """
        pass

    def test_post_users_user_id_ssh_keys(self):
        """Test case for post_users_user_id_ssh_keys

        Add an SSH key for a user  # noqa: E501
        """
        pass


if __name__ == "__main__":
    unittest.main()
