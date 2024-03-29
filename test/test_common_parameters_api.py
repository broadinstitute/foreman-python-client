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
from pyforeman.api.common_parameters_api import CommonParametersApi  # noqa: E501
from pyforeman.rest import ApiException


class TestCommonParametersApi(unittest.TestCase):
    """CommonParametersApi unit test stubs"""

    def setUp(self):
        self.api = (
            pyforeman.api.common_parameters_api.CommonParametersApi()
        )  # noqa: E501

    def tearDown(self):
        pass

    def test_delete_common_parameters_id(self):
        """Test case for delete_common_parameters_id

        Delete a global parameter  # noqa: E501
        """
        pass

    def test_get_common_parameters(self):
        """Test case for get_common_parameters

        List all global parameters  # noqa: E501
        """
        pass

    def test_get_common_parameters_id(self):
        """Test case for get_common_parameters_id

        Show a global parameter  # noqa: E501
        """
        pass

    def test_post_common_parameters(self):
        """Test case for post_common_parameters

        Create a global parameter  # noqa: E501
        """
        pass

    def test_put_common_parameters_id(self):
        """Test case for put_common_parameters_id

        Update a global parameter  # noqa: E501
        """
        pass


if __name__ == "__main__":
    unittest.main()
