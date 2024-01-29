# coding: utf-8

"""
    Foreman (params in:formData)

     <p>Foreman API v2 is currently the default API version.</p> 

    The version of the OpenAPI document: v2
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from foreman.api.os_default_templates_api import OsDefaultTemplatesApi


class TestOsDefaultTemplatesApi(unittest.TestCase):
    """OsDefaultTemplatesApi unit test stubs"""

    def setUp(self) -> None:
        self.api = OsDefaultTemplatesApi()

    def tearDown(self) -> None:
        pass

    def test_delete_operatingsystems_operatingsystem_id_os_default_templates_id(
        self,
    ) -> None:
        """Test case for delete_operatingsystems_operatingsystem_id_os_default_templates_id

        Delete a default template combination for an operating system
        """
        pass

    def test_get_operatingsystems_operatingsystem_id_os_default_templates(self) -> None:
        """Test case for get_operatingsystems_operatingsystem_id_os_default_templates

        List default templates combinations for an operating system
        """
        pass

    def test_get_operatingsystems_operatingsystem_id_os_default_templates_id(
        self,
    ) -> None:
        """Test case for get_operatingsystems_operatingsystem_id_os_default_templates_id

        Show a default template combination for an operating system
        """
        pass

    def test_get_provisioning_templates_provisioning_template_id_os_default_templates(
        self,
    ) -> None:
        """Test case for get_provisioning_templates_provisioning_template_id_os_default_templates

        List operating systems where this template is set as a default
        """
        pass

    def test_post_operatingsystems_operatingsystem_id_os_default_templates(
        self,
    ) -> None:
        """Test case for post_operatingsystems_operatingsystem_id_os_default_templates

        Create a default template combination for an operating system
        """
        pass

    def test_put_operatingsystems_operatingsystem_id_os_default_templates_id(
        self,
    ) -> None:
        """Test case for put_operatingsystems_operatingsystem_id_os_default_templates_id

        Update a default template combination for an operating system
        """
        pass


if __name__ == "__main__":
    unittest.main()