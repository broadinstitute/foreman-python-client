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
from pyforeman.api.sync_api import SyncApi  # noqa: E501
from pyforeman.rest import ApiException


class TestSyncApi(unittest.TestCase):
    """SyncApi unit test stubs"""

    def setUp(self):
        self.api = pyforeman.api.sync_api.SyncApi()  # noqa: E501

    def tearDown(self):
        pass

    def test_get_repositories_repository_id_sync(self):
        """Test case for get_repositories_repository_id_sync

        Get status of synchronisation for given repository  # noqa: E501
        """
        pass


if __name__ == "__main__":
    unittest.main()
