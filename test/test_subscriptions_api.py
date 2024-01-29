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
from pyforeman.api.subscriptions_api import SubscriptionsApi  # noqa: E501
from pyforeman.rest import ApiException


class TestSubscriptionsApi(unittest.TestCase):
    """SubscriptionsApi unit test stubs"""

    def setUp(self):
        self.api = pyforeman.api.subscriptions_api.SubscriptionsApi()  # noqa: E501

    def tearDown(self):
        pass

    def test_get_activation_keys_activation_key_id_subscriptions(self):
        """Test case for get_activation_keys_activation_key_id_subscriptions

        List an activation key's subscriptions  # noqa: E501
        """
        pass

    def test_get_organizations_organization_id_subscriptions(self):
        """Test case for get_organizations_organization_id_subscriptions

        List organization subscriptions  # noqa: E501
        """
        pass

    def test_get_organizations_organization_id_subscriptions_id(self):
        """Test case for get_organizations_organization_id_subscriptions_id

        Show a subscription  # noqa: E501
        """
        pass

    def test_get_organizations_organization_id_subscriptions_manifest_history(self):
        """Test case for get_organizations_organization_id_subscriptions_manifest_history

        obtain manifest history for subscriptions  # noqa: E501
        """
        pass

    def test_get_subscriptions(self):
        """Test case for get_subscriptions

        List subscriptions  # noqa: E501
        """
        pass

    def test_get_subscriptions_id(self):
        """Test case for get_subscriptions_id

        Show a subscription  # noqa: E501
        """
        pass

    def test_post_organizations_organization_id_subscriptions_delete_manifest(self):
        """Test case for post_organizations_organization_id_subscriptions_delete_manifest

        Delete manifest from Red Hat provider  # noqa: E501
        """
        pass

    def test_post_organizations_organization_id_subscriptions_upload(self):
        """Test case for post_organizations_organization_id_subscriptions_upload

        Upload a subscription manifest  # noqa: E501
        """
        pass

    def test_put_organizations_organization_id_subscriptions_refresh_manifest(self):
        """Test case for put_organizations_organization_id_subscriptions_refresh_manifest

        Refresh previously imported manifest for Red Hat provider  # noqa: E501
        """
        pass


if __name__ == "__main__":
    unittest.main()
