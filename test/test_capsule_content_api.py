# coding: utf-8

"""
    Foreman (params in:formData)

     <p>Foreman API v2 is currently the default API version.</p> 

    The version of the OpenAPI document: v2
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from foreman.api.capsule_content_api import CapsuleContentApi


class TestCapsuleContentApi(unittest.TestCase):
    """CapsuleContentApi unit test stubs"""

    def setUp(self) -> None:
        self.api = CapsuleContentApi()

    def tearDown(self) -> None:
        pass

    def test_delete_capsules_id_content_lifecycle_environments_environment_id(
        self,
    ) -> None:
        """Test case for delete_capsules_id_content_lifecycle_environments_environment_id

        Remove lifecycle environments from the smart proxy
        """
        pass

    def test_delete_capsules_id_content_sync(self) -> None:
        """Test case for delete_capsules_id_content_sync

        Cancel running smart proxy synchronization
        """
        pass

    def test_get_capsules_id_content_available_lifecycle_environments(self) -> None:
        """Test case for get_capsules_id_content_available_lifecycle_environments

        List the lifecycle environments not attached to the smart proxy
        """
        pass

    def test_get_capsules_id_content_counts(self) -> None:
        """Test case for get_capsules_id_content_counts

        List content counts for the smart proxy
        """
        pass

    def test_get_capsules_id_content_lifecycle_environments(self) -> None:
        """Test case for get_capsules_id_content_lifecycle_environments

        List the lifecycle environments attached to the smart proxy
        """
        pass

    def test_get_capsules_id_content_sync(self) -> None:
        """Test case for get_capsules_id_content_sync

        Get current smart proxy synchronization status
        """
        pass

    def test_post_capsules_id_content_lifecycle_environments(self) -> None:
        """Test case for post_capsules_id_content_lifecycle_environments

        Add lifecycle environments to the smart proxy
        """
        pass

    def test_post_capsules_id_content_reclaim_space(self) -> None:
        """Test case for post_capsules_id_content_reclaim_space

        Reclaim space from all On Demand repositories on a smart proxy
        """
        pass

    def test_post_capsules_id_content_sync(self) -> None:
        """Test case for post_capsules_id_content_sync

        Synchronize the content to the smart proxy
        """
        pass

    def test_post_capsules_id_content_update_counts(self) -> None:
        """Test case for post_capsules_id_content_update_counts

        Update content counts for the smart proxy
        """
        pass


if __name__ == "__main__":
    unittest.main()
