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
from pyforeman.api.media_api import MediaApi  # noqa: E501
from pyforeman.rest import ApiException


class TestMediaApi(unittest.TestCase):
    """MediaApi unit test stubs"""

    def setUp(self):
        self.api = pyforeman.api.media_api.MediaApi()  # noqa: E501

    def tearDown(self):
        pass

    def test_delete_media_id(self):
        """Test case for delete_media_id

        Delete a medium  # noqa: E501
        """
        pass

    def test_get_locations_location_id_media(self):
        """Test case for get_locations_location_id_media

        List all media per location  # noqa: E501
        """
        pass

    def test_get_media(self):
        """Test case for get_media

        List all installation media  # noqa: E501
        """
        pass

    def test_get_media_id(self):
        """Test case for get_media_id

        Show a medium  # noqa: E501
        """
        pass

    def test_get_operatingsystems_operatingsystem_id_media(self):
        """Test case for get_operatingsystems_operatingsystem_id_media

        List all media for an operating system  # noqa: E501
        """
        pass

    def test_get_organizations_organization_id_media(self):
        """Test case for get_organizations_organization_id_media

        List all media per organization  # noqa: E501
        """
        pass

    def test_post_media(self):
        """Test case for post_media

        Create a medium  # noqa: E501
        """
        pass

    def test_put_media_id(self):
        """Test case for put_media_id

        Update a medium  # noqa: E501
        """
        pass


if __name__ == "__main__":
    unittest.main()
