# coding: utf-8

"""
    Foreman (params in:formData)

     <p>Foreman API v2 is currently the default API version.</p> 

    The version of the OpenAPI document: v2
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from foreman.api.ssh_keys_api import SshKeysApi


class TestSshKeysApi(unittest.TestCase):
    """SshKeysApi unit test stubs"""

    def setUp(self) -> None:
        self.api = SshKeysApi()

    def tearDown(self) -> None:
        pass

    def test_delete_users_user_id_ssh_keys_id(self) -> None:
        """Test case for delete_users_user_id_ssh_keys_id

        Delete an SSH key for a user
        """
        pass

    def test_get_users_user_id_ssh_keys(self) -> None:
        """Test case for get_users_user_id_ssh_keys

        List all SSH keys for a user
        """
        pass

    def test_get_users_user_id_ssh_keys_id(self) -> None:
        """Test case for get_users_user_id_ssh_keys_id

        Show an SSH key from a user
        """
        pass

    def test_post_users_user_id_ssh_keys(self) -> None:
        """Test case for post_users_user_id_ssh_keys

        Add an SSH key for a user
        """
        pass


if __name__ == "__main__":
    unittest.main()
