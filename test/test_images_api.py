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
from pyforeman.api.images_api import ImagesApi  # noqa: E501
from pyforeman.rest import ApiException


class TestImagesApi(unittest.TestCase):
    """ImagesApi unit test stubs"""

    def setUp(self):
        self.api = pyforeman.api.images_api.ImagesApi()  # noqa: E501

    def tearDown(self):
        pass

    def test_delete_compute_resources_compute_resource_id_images_id(self):
        """Test case for delete_compute_resources_compute_resource_id_images_id

        Delete an image  # noqa: E501
        """
        pass

    def test_get_architectures_architecture_id_images(self):
        """Test case for get_architectures_architecture_id_images

        List all images for architecture  # noqa: E501
        """
        pass

    def test_get_architectures_architecture_id_images_id(self):
        """Test case for get_architectures_architecture_id_images_id

        Show an image  # noqa: E501
        """
        pass

    def test_get_compute_resources_compute_resource_id_images(self):
        """Test case for get_compute_resources_compute_resource_id_images

        List all images for a compute resource  # noqa: E501
        """
        pass

    def test_get_compute_resources_compute_resource_id_images_id(self):
        """Test case for get_compute_resources_compute_resource_id_images_id

        Show an image  # noqa: E501
        """
        pass

    def test_get_operatingsystems_operatingsystem_id_images(self):
        """Test case for get_operatingsystems_operatingsystem_id_images

        List all images for operating system  # noqa: E501
        """
        pass

    def test_get_operatingsystems_operatingsystem_id_images_id(self):
        """Test case for get_operatingsystems_operatingsystem_id_images_id

        Show an image  # noqa: E501
        """
        pass

    def test_post_compute_resources_compute_resource_id_images(self):
        """Test case for post_compute_resources_compute_resource_id_images

        Create an image  # noqa: E501
        """
        pass

    def test_put_compute_resources_compute_resource_id_images_id(self):
        """Test case for put_compute_resources_compute_resource_id_images_id

        Update an image  # noqa: E501
        """
        pass


if __name__ == "__main__":
    unittest.main()
