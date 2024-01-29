# coding: utf-8

"""
    Foreman (params in:formData)

     <p>Foreman API v2 is currently the default API version.</p> 

    The version of the OpenAPI document: v2
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from foreman.api.capsules_api import CapsulesApi


class TestCapsulesApi(unittest.TestCase):
    """CapsulesApi unit test stubs"""

    def setUp(self) -> None:
        self.api = CapsulesApi()

    def tearDown(self) -> None:
        pass

    def test_get_capsules(self) -> None:
        """Test case for get_capsules

        List all smart proxies that have content
        """
        pass

    def test_get_capsules_id(self) -> None:
        """Test case for get_capsules_id

        Show the smart proxy details
        """
        pass


if __name__ == "__main__":
    unittest.main()
