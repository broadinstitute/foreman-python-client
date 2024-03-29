# coding: utf-8

"""
    Foreman (params in:formData)

     <p>Foreman API v2 is currently the default API version.</p>   # noqa: E501

    OpenAPI spec version: v2

    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


from __future__ import absolute_import

import re  # noqa: F401

# python 2 and python 3 compatibility library
import six

from pyforeman.api_client import ApiClient


class ContentUploadsApi(object):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    Ref: https://github.com/swagger-api/swagger-codegen
    """

    def __init__(self, api_client=None):
        if api_client is None:
            api_client = ApiClient()
        self.api_client = api_client

    def delete_repositories_repository_id_content_uploads_id(
        self, repository_id, id, **kwargs
    ):  # noqa: E501
        """Delete an upload request  # noqa: E501

          # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.delete_repositories_repository_id_content_uploads_id(repository_id, id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param float repository_id: Repository id (required)
        :param str id: Upload request id (required)
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs["_return_http_data_only"] = True
        if kwargs.get("async_req"):
            return self.delete_repositories_repository_id_content_uploads_id_with_http_info(
                repository_id, id, **kwargs
            )  # noqa: E501
        else:
            (
                data
            ) = self.delete_repositories_repository_id_content_uploads_id_with_http_info(
                repository_id, id, **kwargs
            )  # noqa: E501
            return data

    def delete_repositories_repository_id_content_uploads_id_with_http_info(
        self, repository_id, id, **kwargs
    ):  # noqa: E501
        """Delete an upload request  # noqa: E501

          # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.delete_repositories_repository_id_content_uploads_id_with_http_info(repository_id, id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param float repository_id: Repository id (required)
        :param str id: Upload request id (required)
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ["repository_id", "id"]  # noqa: E501
        all_params.append("async_req")
        all_params.append("_return_http_data_only")
        all_params.append("_preload_content")
        all_params.append("_request_timeout")

        params = locals()
        for key, val in six.iteritems(params["kwargs"]):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method delete_repositories_repository_id_content_uploads_id"
                    % key
                )
            params[key] = val
        del params["kwargs"]
        # verify the required parameter 'repository_id' is set
        if self.api_client.client_side_validation and (
            "repository_id" not in params or params["repository_id"] is None
        ):  # noqa: E501
            raise ValueError(
                "Missing the required parameter `repository_id` when calling `delete_repositories_repository_id_content_uploads_id`"
            )  # noqa: E501
        # verify the required parameter 'id' is set
        if self.api_client.client_side_validation and (
            "id" not in params or params["id"] is None
        ):  # noqa: E501
            raise ValueError(
                "Missing the required parameter `id` when calling `delete_repositories_repository_id_content_uploads_id`"
            )  # noqa: E501

        collection_formats = {}

        path_params = {}
        if "repository_id" in params:
            path_params["repository_id"] = params["repository_id"]  # noqa: E501
        if "id" in params:
            path_params["id"] = params["id"]  # noqa: E501

        query_params = []

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # HTTP header `Content-Type`
        header_params[
            "Content-Type"
        ] = self.api_client.select_header_content_type(  # noqa: E501
            ["application/x-www-form-urlencoded", "multipart/form-data"]
        )  # noqa: E501

        # Authentication setting
        auth_settings = []  # noqa: E501

        return self.api_client.call_api(
            "/repositories/{repository_id}/content_uploads/{id}",
            "DELETE",
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type=None,  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get("async_req"),
            _return_http_data_only=params.get("_return_http_data_only"),
            _preload_content=params.get("_preload_content", True),
            _request_timeout=params.get("_request_timeout"),
            collection_formats=collection_formats,
        )

    def post_repositories_repository_id_content_uploads(
        self, repository_id, size, **kwargs
    ):  # noqa: E501
        """Create an upload request  # noqa: E501

          # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.post_repositories_repository_id_content_uploads(repository_id, size, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param float repository_id: repository id (required)
        :param float size: Size of file to upload (required)
        :param str checksum: Checksum of file to upload
        :param str content_type: content type ('deb', 'docker_manifest', 'file', 'ostree_ref', 'rpm', 'srpm')
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs["_return_http_data_only"] = True
        if kwargs.get("async_req"):
            return self.post_repositories_repository_id_content_uploads_with_http_info(
                repository_id, size, **kwargs
            )  # noqa: E501
        else:
            (
                data
            ) = self.post_repositories_repository_id_content_uploads_with_http_info(
                repository_id, size, **kwargs
            )  # noqa: E501
            return data

    def post_repositories_repository_id_content_uploads_with_http_info(
        self, repository_id, size, **kwargs
    ):  # noqa: E501
        """Create an upload request  # noqa: E501

          # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.post_repositories_repository_id_content_uploads_with_http_info(repository_id, size, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param float repository_id: repository id (required)
        :param float size: Size of file to upload (required)
        :param str checksum: Checksum of file to upload
        :param str content_type: content type ('deb', 'docker_manifest', 'file', 'ostree_ref', 'rpm', 'srpm')
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ["repository_id", "size", "checksum", "content_type"]  # noqa: E501
        all_params.append("async_req")
        all_params.append("_return_http_data_only")
        all_params.append("_preload_content")
        all_params.append("_request_timeout")

        params = locals()
        for key, val in six.iteritems(params["kwargs"]):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method post_repositories_repository_id_content_uploads" % key
                )
            params[key] = val
        del params["kwargs"]
        # verify the required parameter 'repository_id' is set
        if self.api_client.client_side_validation and (
            "repository_id" not in params or params["repository_id"] is None
        ):  # noqa: E501
            raise ValueError(
                "Missing the required parameter `repository_id` when calling `post_repositories_repository_id_content_uploads`"
            )  # noqa: E501
        # verify the required parameter 'size' is set
        if self.api_client.client_side_validation and (
            "size" not in params or params["size"] is None
        ):  # noqa: E501
            raise ValueError(
                "Missing the required parameter `size` when calling `post_repositories_repository_id_content_uploads`"
            )  # noqa: E501

        collection_formats = {}

        path_params = {}
        if "repository_id" in params:
            path_params["repository_id"] = params["repository_id"]  # noqa: E501

        query_params = []

        header_params = {}

        form_params = []
        local_var_files = {}
        if "size" in params:
            form_params.append(("size", params["size"]))  # noqa: E501
        if "checksum" in params:
            form_params.append(("checksum", params["checksum"]))  # noqa: E501
        if "content_type" in params:
            form_params.append(("content_type", params["content_type"]))  # noqa: E501

        body_params = None
        # HTTP header `Content-Type`
        header_params[
            "Content-Type"
        ] = self.api_client.select_header_content_type(  # noqa: E501
            ["application/x-www-form-urlencoded", "multipart/form-data"]
        )  # noqa: E501

        # Authentication setting
        auth_settings = []  # noqa: E501

        return self.api_client.call_api(
            "/repositories/{repository_id}/content_uploads",
            "POST",
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type=None,  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get("async_req"),
            _return_http_data_only=params.get("_return_http_data_only"),
            _preload_content=params.get("_preload_content", True),
            _request_timeout=params.get("_request_timeout"),
            collection_formats=collection_formats,
        )

    def put_repositories_repository_id_content_uploads_id(
        self, repository_id, id, size, offset, content, **kwargs
    ):  # noqa: E501
        """Upload a chunk of the file's content  # noqa: E501

          # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.put_repositories_repository_id_content_uploads_id(repository_id, id, size, offset, content, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param float repository_id: Repository id (required)
        :param str id: Upload request id (required)
        :param float size: Size of file to upload (required)
        :param float offset: The offset in the file where the content starts (required)
        :param file content: The actual file contents (required)
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs["_return_http_data_only"] = True
        if kwargs.get("async_req"):
            return (
                self.put_repositories_repository_id_content_uploads_id_with_http_info(
                    repository_id, id, size, offset, content, **kwargs
                )
            )  # noqa: E501
        else:
            (
                data
            ) = self.put_repositories_repository_id_content_uploads_id_with_http_info(
                repository_id, id, size, offset, content, **kwargs
            )  # noqa: E501
            return data

    def put_repositories_repository_id_content_uploads_id_with_http_info(
        self, repository_id, id, size, offset, content, **kwargs
    ):  # noqa: E501
        """Upload a chunk of the file's content  # noqa: E501

          # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.put_repositories_repository_id_content_uploads_id_with_http_info(repository_id, id, size, offset, content, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param float repository_id: Repository id (required)
        :param str id: Upload request id (required)
        :param float size: Size of file to upload (required)
        :param float offset: The offset in the file where the content starts (required)
        :param file content: The actual file contents (required)
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ["repository_id", "id", "size", "offset", "content"]  # noqa: E501
        all_params.append("async_req")
        all_params.append("_return_http_data_only")
        all_params.append("_preload_content")
        all_params.append("_request_timeout")

        params = locals()
        for key, val in six.iteritems(params["kwargs"]):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method put_repositories_repository_id_content_uploads_id" % key
                )
            params[key] = val
        del params["kwargs"]
        # verify the required parameter 'repository_id' is set
        if self.api_client.client_side_validation and (
            "repository_id" not in params or params["repository_id"] is None
        ):  # noqa: E501
            raise ValueError(
                "Missing the required parameter `repository_id` when calling `put_repositories_repository_id_content_uploads_id`"
            )  # noqa: E501
        # verify the required parameter 'id' is set
        if self.api_client.client_side_validation and (
            "id" not in params or params["id"] is None
        ):  # noqa: E501
            raise ValueError(
                "Missing the required parameter `id` when calling `put_repositories_repository_id_content_uploads_id`"
            )  # noqa: E501
        # verify the required parameter 'size' is set
        if self.api_client.client_side_validation and (
            "size" not in params or params["size"] is None
        ):  # noqa: E501
            raise ValueError(
                "Missing the required parameter `size` when calling `put_repositories_repository_id_content_uploads_id`"
            )  # noqa: E501
        # verify the required parameter 'offset' is set
        if self.api_client.client_side_validation and (
            "offset" not in params or params["offset"] is None
        ):  # noqa: E501
            raise ValueError(
                "Missing the required parameter `offset` when calling `put_repositories_repository_id_content_uploads_id`"
            )  # noqa: E501
        # verify the required parameter 'content' is set
        if self.api_client.client_side_validation and (
            "content" not in params or params["content"] is None
        ):  # noqa: E501
            raise ValueError(
                "Missing the required parameter `content` when calling `put_repositories_repository_id_content_uploads_id`"
            )  # noqa: E501

        collection_formats = {}

        path_params = {}
        if "repository_id" in params:
            path_params["repository_id"] = params["repository_id"]  # noqa: E501
        if "id" in params:
            path_params["id"] = params["id"]  # noqa: E501

        query_params = []

        header_params = {}

        form_params = []
        local_var_files = {}
        if "size" in params:
            form_params.append(("size", params["size"]))  # noqa: E501
        if "offset" in params:
            form_params.append(("offset", params["offset"]))  # noqa: E501
        if "content" in params:
            local_var_files["content"] = params["content"]  # noqa: E501

        body_params = None
        # HTTP header `Content-Type`
        header_params[
            "Content-Type"
        ] = self.api_client.select_header_content_type(  # noqa: E501
            ["application/x-www-form-urlencoded", "multipart/form-data"]
        )  # noqa: E501

        # Authentication setting
        auth_settings = []  # noqa: E501

        return self.api_client.call_api(
            "/repositories/{repository_id}/content_uploads/{id}",
            "PUT",
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type=None,  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get("async_req"),
            _return_http_data_only=params.get("_return_http_data_only"),
            _preload_content=params.get("_preload_content", True),
            _request_timeout=params.get("_request_timeout"),
            collection_formats=collection_formats,
        )
