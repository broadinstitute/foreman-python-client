# coding: utf-8

"""
    Foreman (params in:formData)

     <p>Foreman API v2 is currently the default API version.</p> 

    The version of the OpenAPI document: v2
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from foreman.api.disks_api import DisksApi


class TestDisksApi(unittest.TestCase):
    """DisksApi unit test stubs"""

    def setUp(self) -> None:
        self.api = DisksApi()

    def tearDown(self) -> None:
        pass

    def test_get_bootdisk(self) -> None:
        """Test case for get_bootdisk

        Boot disks
        """
        pass

    def test_get_bootdisk_generic(self) -> None:
        """Test case for get_bootdisk_generic

        Download generic image
        """
        pass

    def test_get_bootdisk_hosts_host_id(self) -> None:
        """Test case for get_bootdisk_hosts_host_id

        Download host image
        """
        pass


if __name__ == "__main__":
    unittest.main()
