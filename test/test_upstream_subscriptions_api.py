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
from pyforeman.api.upstream_subscriptions_api import (
    UpstreamSubscriptionsApi,
)  # noqa: E501
from pyforeman.rest import ApiException


class TestUpstreamSubscriptionsApi(unittest.TestCase):
    """UpstreamSubscriptionsApi unit test stubs"""

    def setUp(self):
        self.api = (
            pyforeman.api.upstream_subscriptions_api.UpstreamSubscriptionsApi()
        )  # noqa: E501

    def tearDown(self):
        pass

    def test_delete_organizations_organization_id_upstream_subscriptions(self):
        """Test case for delete_organizations_organization_id_upstream_subscriptions

        Remove one or more subscriptions from an upstream manifest  # noqa: E501
        """
        pass

    def test_get_organizations_organization_id_upstream_subscriptions(self):
        """Test case for get_organizations_organization_id_upstream_subscriptions

        List available subscriptions from Red Hat Subscription Management  # noqa: E501
        """
        pass

    def test_get_organizations_organization_id_upstream_subscriptions_ping(self):
        """Test case for get_organizations_organization_id_upstream_subscriptions_ping

        Check if a connection can be made to Red Hat Subscription Management.  # noqa: E501
        """
        pass

    def test_post_organizations_organization_id_upstream_subscriptions(self):
        """Test case for post_organizations_organization_id_upstream_subscriptions

        Add subscriptions consumed by a manifest from Red Hat Subscription Management  # noqa: E501
        """
        pass

    def test_put_organizations_organization_id_upstream_subscriptions(self):
        """Test case for put_organizations_organization_id_upstream_subscriptions

        Update the quantity of one or more subscriptions on an upstream allocation  # noqa: E501
        """
        pass


if __name__ == "__main__":
    unittest.main()
