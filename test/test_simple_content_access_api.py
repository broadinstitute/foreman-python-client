# coding: utf-8

"""
    Foreman (params in:formData)

     <p>Foreman API v2 is currently the default API version.</p> 

    The version of the OpenAPI document: v2
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from foreman.api.simple_content_access_api import SimpleContentAccessApi


class TestSimpleContentAccessApi(unittest.TestCase):
    """SimpleContentAccessApi unit test stubs"""

    def setUp(self) -> None:
        self.api = SimpleContentAccessApi()

    def tearDown(self) -> None:
        pass

    def test_get_organizations_organization_id_simple_content_access_eligible(
        self,
    ) -> None:
        """Test case for get_organizations_organization_id_simple_content_access_eligible

        Check if the specified organization is eligible for Simple Content Access. WARNING: Simple Content Access will be required for all organizations in Katello 4.12.
        """
        pass

    def test_get_organizations_organization_id_simple_content_access_status(
        self,
    ) -> None:
        """Test case for get_organizations_organization_id_simple_content_access_status

        Check if the specified organization has Simple Content Access enabled. WARNING: Simple Content Access will be required for all organizations in Katello 4.12.
        """
        pass

    def test_put_organizations_organization_id_simple_content_access_disable(
        self,
    ) -> None:
        """Test case for put_organizations_organization_id_simple_content_access_disable

        Disable simple content access for a manifest. WARNING: Simple Content Access will be required for all organizations in Katello 4.12.
        """
        pass

    def test_put_organizations_organization_id_simple_content_access_enable(
        self,
    ) -> None:
        """Test case for put_organizations_organization_id_simple_content_access_enable

        Enable simple content access for a manifest
        """
        pass


if __name__ == "__main__":
    unittest.main()