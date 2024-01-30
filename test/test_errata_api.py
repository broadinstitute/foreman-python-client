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
from pyforeman.api.errata_api import ErrataApi  # noqa: E501
from pyforeman.rest import ApiException


class TestErrataApi(unittest.TestCase):
    """ErrataApi unit test stubs"""

    def setUp(self):
        self.api = pyforeman.api.errata_api.ErrataApi()  # noqa: E501

    def tearDown(self):
        pass

    def test_get_errata(self):
        """Test case for get_errata

        List errata  # noqa: E501
        """
        pass

    def test_get_errata_compare(self):
        """Test case for get_errata_compare

        List errata  # noqa: E501
        """
        pass

    def test_get_errata_id(self):
        """Test case for get_errata_id

        Show an erratum  # noqa: E501
        """
        pass

    def test_get_repositories_repository_id_errata_id(self):
        """Test case for get_repositories_repository_id_errata_id

        Show an erratum  # noqa: E501
        """
        pass


if __name__ == "__main__":
    unittest.main()
