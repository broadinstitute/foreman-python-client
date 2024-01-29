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
from pyforeman.api.content_view_versions_api import ContentViewVersionsApi  # noqa: E501
from pyforeman.rest import ApiException


class TestContentViewVersionsApi(unittest.TestCase):
    """ContentViewVersionsApi unit test stubs"""

    def setUp(self):
        self.api = (
            pyforeman.api.content_view_versions_api.ContentViewVersionsApi()
        )  # noqa: E501

    def tearDown(self):
        pass

    def test_delete_content_view_versions_id(self):
        """Test case for delete_content_view_versions_id

        Remove content view version  # noqa: E501
        """
        pass

    def test_get_content_view_versions(self):
        """Test case for get_content_view_versions

        List content view versions  # noqa: E501
        """
        pass

    def test_get_content_view_versions_id(self):
        """Test case for get_content_view_versions_id

        Show content view version  # noqa: E501
        """
        pass

    def test_get_content_views_content_view_id_content_view_versions(self):
        """Test case for get_content_views_content_view_id_content_view_versions

        List content view versions  # noqa: E501
        """
        pass

    def test_post_content_view_versions_id_promote(self):
        """Test case for post_content_view_versions_id_promote

        Promote a content view version  # noqa: E501
        """
        pass

    def test_post_content_view_versions_incremental_update(self):
        """Test case for post_content_view_versions_incremental_update

        Perform an Incremental Update on one or more Content View Versions  # noqa: E501
        """
        pass

    def test_put_content_view_versions_id(self):
        """Test case for put_content_view_versions_id

        Update a content view version  # noqa: E501
        """
        pass

    def test_put_content_view_versions_id_republish_repositories(self):
        """Test case for put_content_view_versions_id_republish_repositories

        Forces a republish of the version's repositories' metadata  # noqa: E501
        """
        pass


if __name__ == "__main__":
    unittest.main()
