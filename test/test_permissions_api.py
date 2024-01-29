# coding: utf-8

"""
    Foreman (params in:formData)

     <p>Foreman API v2 is currently the default API version.</p> 

    The version of the OpenAPI document: v2
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from foreman.api.permissions_api import PermissionsApi


class TestPermissionsApi(unittest.TestCase):
    """PermissionsApi unit test stubs"""

    def setUp(self) -> None:
        self.api = PermissionsApi()

    def tearDown(self) -> None:
        pass

    def test_get_permissions(self) -> None:
        """Test case for get_permissions

        List all permissions
        """
        pass

    def test_get_permissions_id(self) -> None:
        """Test case for get_permissions_id

        Show a permission
        """
        pass

    def test_get_permissions_resource_types(self) -> None:
        """Test case for get_permissions_resource_types

        List available resource types
        """
        pass


if __name__ == "__main__":
    unittest.main()