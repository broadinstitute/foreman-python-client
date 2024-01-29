# coding: utf-8

"""
    Foreman (params in:formData)

     <p>Foreman API v2 is currently the default API version.</p> 

    The version of the OpenAPI document: v2
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from foreman.api.activation_keys_api import ActivationKeysApi


class TestActivationKeysApi(unittest.TestCase):
    """ActivationKeysApi unit test stubs"""

    def setUp(self) -> None:
        self.api = ActivationKeysApi()

    def tearDown(self) -> None:
        pass

    def test_delete_activation_keys_id(self) -> None:
        """Test case for delete_activation_keys_id

        Destroy an activation key
        """
        pass

    def test_get_activation_keys(self) -> None:
        """Test case for get_activation_keys

        List activation keys
        """
        pass

    def test_get_activation_keys_id(self) -> None:
        """Test case for get_activation_keys_id

        Show an activation key
        """
        pass

    def test_get_activation_keys_id_host_collections_available(self) -> None:
        """Test case for get_activation_keys_id_host_collections_available

        List host collections the activation key does not belong to
        """
        pass

    def test_get_activation_keys_id_product_content(self) -> None:
        """Test case for get_activation_keys_id_product_content

        Show content available for an activation key
        """
        pass

    def test_get_activation_keys_id_releases(self) -> None:
        """Test case for get_activation_keys_id_releases

        Show release versions available for an activation key
        """
        pass

    def test_get_environments_environment_id_activation_keys(self) -> None:
        """Test case for get_environments_environment_id_activation_keys"""
        pass

    def test_get_organizations_organization_id_activation_keys(self) -> None:
        """Test case for get_organizations_organization_id_activation_keys"""
        pass

    def test_post_activation_keys(self) -> None:
        """Test case for post_activation_keys

        Create an activation key
        """
        pass

    def test_post_activation_keys_id_copy(self) -> None:
        """Test case for post_activation_keys_id_copy

        Copy an activation key
        """
        pass

    def test_post_activation_keys_id_host_collections(self) -> None:
        """Test case for post_activation_keys_id_host_collections"""
        pass

    def test_put_activation_keys_id(self) -> None:
        """Test case for put_activation_keys_id

        Update an activation key
        """
        pass

    def test_put_activation_keys_id_add_subscriptions(self) -> None:
        """Test case for put_activation_keys_id_add_subscriptions

        Attach a subscription
        """
        pass

    def test_put_activation_keys_id_content_override(self) -> None:
        """Test case for put_activation_keys_id_content_override

        Override content for activation_key
        """
        pass

    def test_put_activation_keys_id_host_collections(self) -> None:
        """Test case for put_activation_keys_id_host_collections"""
        pass

    def test_put_activation_keys_id_remove_subscriptions(self) -> None:
        """Test case for put_activation_keys_id_remove_subscriptions

        Unattach a subscription
        """
        pass


if __name__ == "__main__":
    unittest.main()
