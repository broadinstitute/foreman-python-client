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
from pyforeman.api.subnet_disks_api import SubnetDisksApi  # noqa: E501
from pyforeman.rest import ApiException


class TestSubnetDisksApi(unittest.TestCase):
    """SubnetDisksApi unit test stubs"""

    def setUp(self):
        self.api = pyforeman.api.subnet_disks_api.SubnetDisksApi()  # noqa: E501

    def tearDown(self):
        pass

    def test_get_bootdisk_subnets_subnet_id(self):
        """Test case for get_bootdisk_subnets_subnet_id

        Download subnet generic image  # noqa: E501
        """
        pass


if __name__ == "__main__":
    unittest.main()
