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
from pyforeman.api.operatingsystems_api import OperatingsystemsApi  # noqa: E501
from pyforeman.rest import ApiException


class TestOperatingsystemsApi(unittest.TestCase):
    """OperatingsystemsApi unit test stubs"""

    def setUp(self):
        self.api = (
            pyforeman.api.operatingsystems_api.OperatingsystemsApi()
        )  # noqa: E501

    def tearDown(self):
        pass

    def test_delete_operatingsystems_id(self):
        """Test case for delete_operatingsystems_id

        Delete an operating system  # noqa: E501
        """
        pass

    def test_get_architectures_architecture_id_operatingsystems(self):
        """Test case for get_architectures_architecture_id_operatingsystems

        List all operating systems for nested architecture  # noqa: E501
        """
        pass

    def test_get_media_medium_id_operatingsystems(self):
        """Test case for get_media_medium_id_operatingsystems

        List all operating systems for nested medium  # noqa: E501
        """
        pass

    def test_get_operatingsystems(self):
        """Test case for get_operatingsystems

        List all operating systems  # noqa: E501
        """
        pass

    def test_get_operatingsystems_id(self):
        """Test case for get_operatingsystems_id

        Show an operating system  # noqa: E501
        """
        pass

    def test_get_operatingsystems_id_bootfiles(self):
        """Test case for get_operatingsystems_id_bootfiles

        List boot files for an operating system  # noqa: E501
        """
        pass

    def test_get_provisioning_templates_provisioning_template_id_operatingsystems(self):
        """Test case for get_provisioning_templates_provisioning_template_id_operatingsystems

        List all operating systems for nested provisioning template  # noqa: E501
        """
        pass

    def test_get_ptables_ptable_id_operatingsystems(self):
        """Test case for get_ptables_ptable_id_operatingsystems

        List all operating systems for nested partition table  # noqa: E501
        """
        pass

    def test_post_operatingsystems(self):
        """Test case for post_operatingsystems

        Create an operating system  # noqa: E501
        """
        pass

    def test_put_operatingsystems_id(self):
        """Test case for put_operatingsystems_id

        Update an operating system  # noqa: E501
        """
        pass


if __name__ == "__main__":
    unittest.main()
