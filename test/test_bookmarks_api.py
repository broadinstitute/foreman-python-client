# coding: utf-8

"""
    Foreman (params in:formData)

     <p>Foreman API v2 is currently the default API version.</p> 

    The version of the OpenAPI document: v2
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from foreman.api.bookmarks_api import BookmarksApi


class TestBookmarksApi(unittest.TestCase):
    """BookmarksApi unit test stubs"""

    def setUp(self) -> None:
        self.api = BookmarksApi()

    def tearDown(self) -> None:
        pass

    def test_delete_bookmarks_id(self) -> None:
        """Test case for delete_bookmarks_id

        Delete a bookmark
        """
        pass

    def test_get_bookmarks(self) -> None:
        """Test case for get_bookmarks

        List all bookmarks
        """
        pass

    def test_get_bookmarks_id(self) -> None:
        """Test case for get_bookmarks_id

        Show a bookmark
        """
        pass

    def test_post_bookmarks(self) -> None:
        """Test case for post_bookmarks

        Create a bookmark
        """
        pass

    def test_put_bookmarks_id(self) -> None:
        """Test case for put_bookmarks_id

        Update a bookmark
        """
        pass


if __name__ == "__main__":
    unittest.main()
