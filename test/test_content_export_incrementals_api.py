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
from pyforeman.api.content_export_incrementals_api import (
    ContentExportIncrementalsApi,
)  # noqa: E501
from pyforeman.rest import ApiException


class TestContentExportIncrementalsApi(unittest.TestCase):
    """ContentExportIncrementalsApi unit test stubs"""

    def setUp(self):
        self.api = (
            pyforeman.api.content_export_incrementals_api.ContentExportIncrementalsApi()
        )  # noqa: E501

    def tearDown(self):
        pass

    def test_post_content_export_incrementals_library(self):
        """Test case for post_content_export_incrementals_library

        Performs an incremental-export of the repositories in library.  # noqa: E501
        """
        pass

    def test_post_content_export_incrementals_repository(self):
        """Test case for post_content_export_incrementals_repository

        Performs a incremental-export of the repository in library.  # noqa: E501
        """
        pass

    def test_post_content_export_incrementals_version(self):
        """Test case for post_content_export_incrementals_version

        Performs an incremental-export of a content view version.  # noqa: E501
        """
        pass


if __name__ == "__main__":
    unittest.main()
