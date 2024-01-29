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
from pyforeman.api.alternate_content_sources_api import (
    AlternateContentSourcesApi,
)  # noqa: E501
from pyforeman.rest import ApiException


class TestAlternateContentSourcesApi(unittest.TestCase):
    """AlternateContentSourcesApi unit test stubs"""

    def setUp(self):
        self.api = (
            pyforeman.api.alternate_content_sources_api.AlternateContentSourcesApi()
        )  # noqa: E501

    def tearDown(self):
        pass

    def test_delete_alternate_content_sources_id(self):
        """Test case for delete_alternate_content_sources_id

        Destroy an alternate content source.  # noqa: E501
        """
        pass

    def test_get_alternate_content_sources(self):
        """Test case for get_alternate_content_sources

        List alternate content sources.  # noqa: E501
        """
        pass

    def test_get_alternate_content_sources_id(self):
        """Test case for get_alternate_content_sources_id

        Show an alternate content source.  # noqa: E501
        """
        pass

    def test_post_alternate_content_sources(self):
        """Test case for post_alternate_content_sources

        Create an alternate content source to download content from during repository syncing.  Note: alternate content sources are global and affect ALL sync actions on their smart proxies regardless of organization.  # noqa: E501
        """
        pass

    def test_post_alternate_content_sources_id_refresh(self):
        """Test case for post_alternate_content_sources_id_refresh

        Refresh an alternate content source. Refreshing, like repository syncing, is required before using an alternate content source.  # noqa: E501
        """
        pass

    def test_put_alternate_content_sources_id(self):
        """Test case for put_alternate_content_sources_id

        Update an alternate content source.  # noqa: E501
        """
        pass


if __name__ == "__main__":
    unittest.main()
