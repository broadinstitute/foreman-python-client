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
from pyforeman.api.generic_content_units_api import GenericContentUnitsApi  # noqa: E501
from pyforeman.rest import ApiException


class TestGenericContentUnitsApi(unittest.TestCase):
    """GenericContentUnitsApi unit test stubs"""

    def setUp(self):
        self.api = (
            pyforeman.api.generic_content_units_api.GenericContentUnitsApi()
        )  # noqa: E501

    def tearDown(self):
        pass

    def test_get_content_units(self):
        """Test case for get_content_units

        List content_units  # noqa: E501
        """
        pass

    def test_get_content_units_compare(self):
        """Test case for get_content_units_compare

        List :resource  # noqa: E501
        """
        pass

    def test_get_content_units_id(self):
        """Test case for get_content_units_id

        Show a content unit  # noqa: E501
        """
        pass

    def test_get_content_view_filters_content_view_filter_id_content_units(self):
        """Test case for get_content_view_filters_content_view_filter_id_content_units

        List content_units  # noqa: E501
        """
        pass

    def test_get_content_views_content_view_id_filters_filter_id_content_units(self):
        """Test case for get_content_views_content_view_id_filters_filter_id_content_units

        List content_units  # noqa: E501
        """
        pass

    def test_get_ostree_refs(self):
        """Test case for get_ostree_refs

        List ostree_refs  # noqa: E501
        """
        pass

    def test_get_ostree_refs_id(self):
        """Test case for get_ostree_refs_id

        Show ostree ref  # noqa: E501
        """
        pass

    def test_get_python_packages(self):
        """Test case for get_python_packages

        List python_packages  # noqa: E501
        """
        pass

    def test_get_python_packages_id(self):
        """Test case for get_python_packages_id

        Show python package  # noqa: E501
        """
        pass

    def test_get_repositories_repository_id_content_units(self):
        """Test case for get_repositories_repository_id_content_units

        List content_units  # noqa: E501
        """
        pass

    def test_get_repositories_repository_id_content_units_id(self):
        """Test case for get_repositories_repository_id_content_units_id

        Show a content unit  # noqa: E501
        """
        pass

    def test_get_repositories_repository_id_ostree_refs_id(self):
        """Test case for get_repositories_repository_id_ostree_refs_id

        Show ostree ref  # noqa: E501
        """
        pass

    def test_get_repositories_repository_id_python_packages_id(self):
        """Test case for get_repositories_repository_id_python_packages_id

        Show python package  # noqa: E501
        """
        pass


if __name__ == "__main__":
    unittest.main()
