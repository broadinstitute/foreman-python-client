# coding: utf-8

"""
    Foreman (params in:formData)

     <p>Foreman API v2 is currently the default API version.</p> 

    The version of the OpenAPI document: v2
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from foreman.api.filters_api import FiltersApi


class TestFiltersApi(unittest.TestCase):
    """FiltersApi unit test stubs"""

    def setUp(self) -> None:
        self.api = FiltersApi()

    def tearDown(self) -> None:
        pass

    def test_delete_filters_id(self) -> None:
        """Test case for delete_filters_id

        Delete a filter
        """
        pass

    def test_get_filters(self) -> None:
        """Test case for get_filters

        List all filters
        """
        pass

    def test_get_filters_id(self) -> None:
        """Test case for get_filters_id

        Show a filter
        """
        pass

    def test_post_filters(self) -> None:
        """Test case for post_filters

        Create a filter
        """
        pass

    def test_put_filters_id(self) -> None:
        """Test case for put_filters_id

        Update a filter
        """
        pass


if __name__ == "__main__":
    unittest.main()
