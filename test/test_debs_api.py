# coding: utf-8

"""
    Foreman (params in:formData)

     <p>Foreman API v2 is currently the default API version.</p> 

    The version of the OpenAPI document: v2
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from foreman.api.debs_api import DebsApi


class TestDebsApi(unittest.TestCase):
    """DebsApi unit test stubs"""

    def setUp(self) -> None:
        self.api = DebsApi()

    def tearDown(self) -> None:
        pass

    def test_get_content_view_filters_content_view_filter_id_debs(self) -> None:
        """Test case for get_content_view_filters_content_view_filter_id_debs

        List deb packages
        """
        pass

    def test_get_content_views_content_view_id_filters_filter_id_debs(self) -> None:
        """Test case for get_content_views_content_view_id_filters_filter_id_debs

        List deb packages
        """
        pass

    def test_get_debs(self) -> None:
        """Test case for get_debs

        List deb packages
        """
        pass

    def test_get_debs_compare(self) -> None:
        """Test case for get_debs_compare

        List deb packages
        """
        pass

    def test_get_debs_id(self) -> None:
        """Test case for get_debs_id

        Show a deb package
        """
        pass

    def test_get_repositories_repository_id_debs(self) -> None:
        """Test case for get_repositories_repository_id_debs

        List deb packages
        """
        pass

    def test_get_repositories_repository_id_debs_id(self) -> None:
        """Test case for get_repositories_repository_id_debs_id

        Show a deb package
        """
        pass


if __name__ == "__main__":
    unittest.main()