# coding: utf-8

"""
    Foreman (params in:formData)

     <p>Foreman API v2 is currently the default API version.</p> 

    The version of the OpenAPI document: v2
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from foreman.api.docker_tags_api import DockerTagsApi


class TestDockerTagsApi(unittest.TestCase):
    """DockerTagsApi unit test stubs"""

    def setUp(self) -> None:
        self.api = DockerTagsApi()

    def tearDown(self) -> None:
        pass

    def test_get_content_view_filters_content_view_filter_id_docker_tags(self) -> None:
        """Test case for get_content_view_filters_content_view_filter_id_docker_tags

        List docker_tags
        """
        pass

    def test_get_content_views_content_view_id_filters_filter_id_docker_tags(
        self,
    ) -> None:
        """Test case for get_content_views_content_view_id_filters_filter_id_docker_tags

        List docker_tags
        """
        pass

    def test_get_docker_tags(self) -> None:
        """Test case for get_docker_tags

        List docker_tags
        """
        pass

    def test_get_docker_tags_compare(self) -> None:
        """Test case for get_docker_tags_compare

        List docker_tags
        """
        pass

    def test_get_docker_tags_id(self) -> None:
        """Test case for get_docker_tags_id

        Show a docker tag
        """
        pass

    def test_get_docker_tags_id_repositories(self) -> None:
        """Test case for get_docker_tags_id_repositories

        List of repositories for a docker meta tag
        """
        pass

    def test_get_repositories_repository_id_docker_tags(self) -> None:
        """Test case for get_repositories_repository_id_docker_tags

        List docker_tags
        """
        pass

    def test_get_repositories_repository_id_docker_tags_id(self) -> None:
        """Test case for get_repositories_repository_id_docker_tags_id

        Show a docker tag
        """
        pass


if __name__ == "__main__":
    unittest.main()