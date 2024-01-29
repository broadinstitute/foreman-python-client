# coding: utf-8

"""
    Foreman (params in:formData)

     <p>Foreman API v2 is currently the default API version.</p> 

    The version of the OpenAPI document: v2
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from foreman.api.models_api import ModelsApi


class TestModelsApi(unittest.TestCase):
    """ModelsApi unit test stubs"""

    def setUp(self) -> None:
        self.api = ModelsApi()

    def tearDown(self) -> None:
        pass

    def test_delete_models_id(self) -> None:
        """Test case for delete_models_id

        Delete a hardware model
        """
        pass

    def test_get_models(self) -> None:
        """Test case for get_models

        List all hardware models
        """
        pass

    def test_get_models_id(self) -> None:
        """Test case for get_models_id

        Show a hardware model
        """
        pass

    def test_post_models(self) -> None:
        """Test case for post_models

        Create a hardware model
        """
        pass

    def test_put_models_id(self) -> None:
        """Test case for put_models_id

        Update a hardware model
        """
        pass


if __name__ == "__main__":
    unittest.main()