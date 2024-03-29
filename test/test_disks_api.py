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
from pyforeman.api.disks_api import DisksApi  # noqa: E501
from pyforeman.rest import ApiException


class TestDisksApi(unittest.TestCase):
    """DisksApi unit test stubs"""

    def setUp(self):
        self.api = pyforeman.api.disks_api.DisksApi()  # noqa: E501

    def tearDown(self):
        pass

    def test_get_bootdisk(self):
        """Test case for get_bootdisk

        Boot disks  # noqa: E501
        """
        pass

    def test_get_bootdisk_generic(self):
        """Test case for get_bootdisk_generic

        Download generic image  # noqa: E501
        """
        pass

    def test_get_bootdisk_hosts_host_id(self):
        """Test case for get_bootdisk_hosts_host_id

        Download host image  # noqa: E501
        """
        pass


if __name__ == "__main__":
    unittest.main()
