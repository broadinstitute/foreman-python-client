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
from pyforeman.api.content_view_filter_rules_api import (
    ContentViewFilterRulesApi,
)  # noqa: E501
from pyforeman.rest import ApiException


class TestContentViewFilterRulesApi(unittest.TestCase):
    """ContentViewFilterRulesApi unit test stubs"""

    def setUp(self):
        self.api = (
            pyforeman.api.content_view_filter_rules_api.ContentViewFilterRulesApi()
        )  # noqa: E501

    def tearDown(self):
        pass

    def test_delete_content_view_filters_content_view_filter_id_rules_id(self):
        """Test case for delete_content_view_filters_content_view_filter_id_rules_id

        Delete a filter rule  # noqa: E501
        """
        pass

    def test_get_content_view_filters_content_view_filter_id_rules(self):
        """Test case for get_content_view_filters_content_view_filter_id_rules

        List filter rules  # noqa: E501
        """
        pass

    def test_get_content_view_filters_content_view_filter_id_rules_id(self):
        """Test case for get_content_view_filters_content_view_filter_id_rules_id

        Show filter rule info  # noqa: E501
        """
        pass

    def test_post_content_view_filters_content_view_filter_id_rules(self):
        """Test case for post_content_view_filters_content_view_filter_id_rules

        Create a filter rule. The parameters included should be based upon the filter type.  # noqa: E501
        """
        pass

    def test_put_content_view_filters_content_view_filter_id_rules_id(self):
        """Test case for put_content_view_filters_content_view_filter_id_rules_id

        Update a filter rule. The parameters included should be based upon the filter type.  # noqa: E501
        """
        pass


if __name__ == "__main__":
    unittest.main()
