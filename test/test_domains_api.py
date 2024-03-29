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
from pyforeman.api.domains_api import DomainsApi  # noqa: E501
from pyforeman.rest import ApiException


class TestDomainsApi(unittest.TestCase):
    """DomainsApi unit test stubs"""

    def setUp(self):
        self.api = pyforeman.api.domains_api.DomainsApi()  # noqa: E501

    def tearDown(self):
        pass

    def test_delete_domains_id(self):
        """Test case for delete_domains_id

        Delete a domain  # noqa: E501
        """
        pass

    def test_get_domains(self):
        """Test case for get_domains

        List of domains  # noqa: E501
        """
        pass

    def test_get_domains_id(self):
        """Test case for get_domains_id

        Show a domain  # noqa: E501
        """
        pass

    def test_get_locations_location_id_domains(self):
        """Test case for get_locations_location_id_domains

        List of domains per location  # noqa: E501
        """
        pass

    def test_get_organizations_organization_id_domains(self):
        """Test case for get_organizations_organization_id_domains

        List of domains per organization  # noqa: E501
        """
        pass

    def test_get_subnets_subnet_id_domains(self):
        """Test case for get_subnets_subnet_id_domains

        List of domains per subnet  # noqa: E501
        """
        pass

    def test_post_domains(self):
        """Test case for post_domains

        Create a domain  # noqa: E501
        """
        pass

    def test_put_domains_id(self):
        """Test case for put_domains_id

        Update a domain  # noqa: E501
        """
        pass


if __name__ == "__main__":
    unittest.main()
