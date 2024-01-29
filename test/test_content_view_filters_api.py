# coding: utf-8

"""
    Foreman (params in:formData)

     <p>Foreman API v2 is currently the default API version.</p> 

    The version of the OpenAPI document: v2
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from foreman.api.content_view_filters_api import ContentViewFiltersApi


class TestContentViewFiltersApi(unittest.TestCase):
    """ContentViewFiltersApi unit test stubs"""

    def setUp(self) -> None:
        self.api = ContentViewFiltersApi()

    def tearDown(self) -> None:
        pass

    def test_delete_content_view_filters_id(self) -> None:
        """Test case for delete_content_view_filters_id

        delete a filter
        """
        pass

    def test_delete_content_views_content_view_id_filters_id(self) -> None:
        """Test case for delete_content_views_content_view_id_filters_id

        delete a filter
        """
        pass

    def test_get_content_view_filters(self) -> None:
        """Test case for get_content_view_filters

        list filters
        """
        pass

    def test_get_content_view_filters_id(self) -> None:
        """Test case for get_content_view_filters_id

        show filter info
        """
        pass

    def test_get_content_views_content_view_id_filters(self) -> None:
        """Test case for get_content_views_content_view_id_filters

        list filters
        """
        pass

    def test_get_content_views_content_view_id_filters_id(self) -> None:
        """Test case for get_content_views_content_view_id_filters_id

        show filter info
        """
        pass

    def test_post_content_view_filters(self) -> None:
        """Test case for post_content_view_filters

        create a filter for a content view
        """
        pass

    def test_post_content_views_content_view_id_filters(self) -> None:
        """Test case for post_content_views_content_view_id_filters

        create a filter for a content view
        """
        pass

    def test_put_content_view_filters_id(self) -> None:
        """Test case for put_content_view_filters_id

        update a filter
        """
        pass

    def test_put_content_view_filters_id_add_filter_rules(self) -> None:
        """Test case for put_content_view_filters_id_add_filter_rules

        bulk add filter rules
        """
        pass

    def test_put_content_view_filters_id_remove_filter_rules(self) -> None:
        """Test case for put_content_view_filters_id_remove_filter_rules

        bulk delete filter rules
        """
        pass

    def test_put_content_views_content_view_id_filters_id(self) -> None:
        """Test case for put_content_views_content_view_id_filters_id

        update a filter
        """
        pass

    def test_put_content_views_content_view_id_filters_id_add_filter_rules(
        self,
    ) -> None:
        """Test case for put_content_views_content_view_id_filters_id_add_filter_rules

        bulk add filter rules
        """
        pass

    def test_put_content_views_content_view_id_filters_id_remove_filter_rules(
        self,
    ) -> None:
        """Test case for put_content_views_content_view_id_filters_id_remove_filter_rules

        bulk delete filter rules
        """
        pass


if __name__ == "__main__":
    unittest.main()
