# coding: utf-8

"""
    Foreman (params in:formData)

     <p>Foreman API v2 is currently the default API version.</p> 

    The version of the OpenAPI document: v2
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from foreman.api.settings_api import SettingsApi


class TestSettingsApi(unittest.TestCase):
    """SettingsApi unit test stubs"""

    def setUp(self) -> None:
        self.api = SettingsApi()

    def tearDown(self) -> None:
        pass

    def test_get_settings(self) -> None:
        """Test case for get_settings

        List all settings
        """
        pass

    def test_get_settings_id(self) -> None:
        """Test case for get_settings_id

        Show a setting
        """
        pass

    def test_put_settings_id(self) -> None:
        """Test case for put_settings_id

        Update a setting
        """
        pass


if __name__ == "__main__":
    unittest.main()