# coding: utf-8

"""
    Foreman (params in:formData)

     <p>Foreman API v2 is currently the default API version.</p> 

    The version of the OpenAPI document: v2
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from foreman.api.ptables_api import PtablesApi


class TestPtablesApi(unittest.TestCase):
    """PtablesApi unit test stubs"""

    def setUp(self) -> None:
        self.api = PtablesApi()

    def tearDown(self) -> None:
        pass

    def test_delete_ptables_id(self) -> None:
        """Test case for delete_ptables_id

        Delete a partition table
        """
        pass

    def test_get_locations_location_id_ptables(self) -> None:
        """Test case for get_locations_location_id_ptables

        List all partition tables per location
        """
        pass

    def test_get_operatingsystems_operatingsystem_id_ptables(self) -> None:
        """Test case for get_operatingsystems_operatingsystem_id_ptables

        List all partition tables for an operating system
        """
        pass

    def test_get_organizations_organization_id_ptables(self) -> None:
        """Test case for get_organizations_organization_id_ptables

        List all partition tables per organization
        """
        pass

    def test_get_ptables(self) -> None:
        """Test case for get_ptables

        List all partition tables
        """
        pass

    def test_get_ptables_id(self) -> None:
        """Test case for get_ptables_id

        Show a partition table
        """
        pass

    def test_get_ptables_id_export(self) -> None:
        """Test case for get_ptables_id_export

        Export a partition template to ERB
        """
        pass

    def test_get_ptables_revision(self) -> None:
        """Test case for get_ptables_revision"""
        pass

    def test_post_ptables(self) -> None:
        """Test case for post_ptables

        Create a partition table
        """
        pass

    def test_post_ptables_id_clone(self) -> None:
        """Test case for post_ptables_id_clone

        Clone a template
        """
        pass

    def test_post_ptables_import(self) -> None:
        """Test case for post_ptables_import

        Import a partition table
        """
        pass

    def test_put_ptables_id(self) -> None:
        """Test case for put_ptables_id

        Update a partition table
        """
        pass


if __name__ == "__main__":
    unittest.main()
