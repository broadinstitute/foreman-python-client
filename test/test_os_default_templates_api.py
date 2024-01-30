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
from pyforeman.api.os_default_templates_api import OsDefaultTemplatesApi  # noqa: E501
from pyforeman.rest import ApiException


class TestOsDefaultTemplatesApi(unittest.TestCase):
    """OsDefaultTemplatesApi unit test stubs"""

    def setUp(self):
        self.api = (
            pyforeman.api.os_default_templates_api.OsDefaultTemplatesApi()
        )  # noqa: E501

    def tearDown(self):
        pass

    def test_delete_operatingsystems_operatingsystem_id_os_default_templates_id(self):
        """Test case for delete_operatingsystems_operatingsystem_id_os_default_templates_id

        Delete a default template combination for an operating system  # noqa: E501
        """
        pass

    def test_get_operatingsystems_operatingsystem_id_os_default_templates(self):
        """Test case for get_operatingsystems_operatingsystem_id_os_default_templates

        List default templates combinations for an operating system  # noqa: E501
        """
        pass

    def test_get_operatingsystems_operatingsystem_id_os_default_templates_id(self):
        """Test case for get_operatingsystems_operatingsystem_id_os_default_templates_id

        Show a default template combination for an operating system  # noqa: E501
        """
        pass

    def test_get_provisioning_templates_provisioning_template_id_os_default_templates(
        self,
    ):
        """Test case for get_provisioning_templates_provisioning_template_id_os_default_templates

        List operating systems where this template is set as a default  # noqa: E501
        """
        pass

    def test_post_operatingsystems_operatingsystem_id_os_default_templates(self):
        """Test case for post_operatingsystems_operatingsystem_id_os_default_templates

        Create a default template combination for an operating system  # noqa: E501
        """
        pass

    def test_put_operatingsystems_operatingsystem_id_os_default_templates_id(self):
        """Test case for put_operatingsystems_operatingsystem_id_os_default_templates_id

        Update a default template combination for an operating system  # noqa: E501
        """
        pass


if __name__ == "__main__":
    unittest.main()
