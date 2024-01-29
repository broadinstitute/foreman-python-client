# coding: utf-8

"""
    Foreman (params in:formData)

     <p>Foreman API v2 is currently the default API version.</p> 

    The version of the OpenAPI document: v2
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from foreman.api.repository_sets_api import RepositorySetsApi


class TestRepositorySetsApi(unittest.TestCase):
    """RepositorySetsApi unit test stubs"""

    def setUp(self) -> None:
        self.api = RepositorySetsApi()

    def tearDown(self) -> None:
        pass

    def test_get_products_product_id_repository_sets(self) -> None:
        """Test case for get_products_product_id_repository_sets

        List repository sets for a product.
        """
        pass

    def test_get_products_product_id_repository_sets_id(self) -> None:
        """Test case for get_products_product_id_repository_sets_id

        Get info about a repository set
        """
        pass

    def test_get_products_product_id_repository_sets_id_available_repositories(
        self,
    ) -> None:
        """Test case for get_products_product_id_repository_sets_id_available_repositories

        Get list of available repositories for the repository set
        """
        pass

    def test_get_repository_sets(self) -> None:
        """Test case for get_repository_sets

        List repository sets.
        """
        pass

    def test_get_repository_sets_id(self) -> None:
        """Test case for get_repository_sets_id

        Get info about a repository set
        """
        pass

    def test_get_repository_sets_id_available_repositories(self) -> None:
        """Test case for get_repository_sets_id_available_repositories

        Get list of available repositories for the repository set
        """
        pass

    def test_put_products_product_id_repository_sets_id_disable(self) -> None:
        """Test case for put_products_product_id_repository_sets_id_disable

        Disable a repository from the set
        """
        pass

    def test_put_products_product_id_repository_sets_id_enable(self) -> None:
        """Test case for put_products_product_id_repository_sets_id_enable

        Enable a repository from the set
        """
        pass

    def test_put_repository_sets_id_disable(self) -> None:
        """Test case for put_repository_sets_id_disable

        Disable a repository from the set
        """
        pass

    def test_put_repository_sets_id_enable(self) -> None:
        """Test case for put_repository_sets_id_enable

        Enable a repository from the set
        """
        pass


if __name__ == "__main__":
    unittest.main()
