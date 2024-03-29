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


class AlternateContentSourcesBulkActionsApi(object):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    Ref: https://github.com/swagger-api/swagger-codegen
    """

    def __init__(self, api_client=None):
        if api_client is None:
            api_client = ApiClient()
        self.api_client = api_client

    def post_alternate_content_sources_bulk_refresh(self, ids, **kwargs):  # noqa: E501
        """Refresh alternate content sources  # noqa: E501

          # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.post_alternate_content_sources_bulk_refresh(ids, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param list[str] ids: List of alternate content source IDs (required)
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs["_return_http_data_only"] = True
        if kwargs.get("async_req"):
            return self.post_alternate_content_sources_bulk_refresh_with_http_info(
                ids, **kwargs
            )  # noqa: E501
        else:
            (data) = self.post_alternate_content_sources_bulk_refresh_with_http_info(
                ids, **kwargs
            )  # noqa: E501
            return data

    def post_alternate_content_sources_bulk_refresh_with_http_info(
        self, ids, **kwargs
    ):  # noqa: E501
        """Refresh alternate content sources  # noqa: E501

          # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.post_alternate_content_sources_bulk_refresh_with_http_info(ids, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param list[str] ids: List of alternate content source IDs (required)
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ["ids"]  # noqa: E501
        all_params.append("async_req")
        all_params.append("_return_http_data_only")
        all_params.append("_preload_content")
        all_params.append("_request_timeout")

        params = locals()
        for key, val in six.iteritems(params["kwargs"]):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method post_alternate_content_sources_bulk_refresh" % key
                )
            params[key] = val
        del params["kwargs"]
        # verify the required parameter 'ids' is set
        if self.api_client.client_side_validation and (
            "ids" not in params or params["ids"] is None
        ):  # noqa: E501
            raise ValueError(
                "Missing the required parameter `ids` when calling `post_alternate_content_sources_bulk_refresh`"
            )  # noqa: E501

        collection_formats = {}

        path_params = {}

        query_params = []

        header_params = {}

        form_params = []
        local_var_files = {}
        if "ids" in params:
            form_params.append(("ids", params["ids"]))  # noqa: E501
            collection_formats["ids"] = "csv"  # noqa: E501

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
            "/alternate_content_sources/bulk/refresh",
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

    def post_alternate_content_sources_bulk_refresh_all(self, **kwargs):  # noqa: E501
        """Refresh all alternate content sources  # noqa: E501

          # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.post_alternate_content_sources_bulk_refresh_all(async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs["_return_http_data_only"] = True
        if kwargs.get("async_req"):
            return self.post_alternate_content_sources_bulk_refresh_all_with_http_info(
                **kwargs
            )  # noqa: E501
        else:
            (
                data
            ) = self.post_alternate_content_sources_bulk_refresh_all_with_http_info(
                **kwargs
            )  # noqa: E501
            return data

    def post_alternate_content_sources_bulk_refresh_all_with_http_info(
        self, **kwargs
    ):  # noqa: E501
        """Refresh all alternate content sources  # noqa: E501

          # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.post_alternate_content_sources_bulk_refresh_all_with_http_info(async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = []  # noqa: E501
        all_params.append("async_req")
        all_params.append("_return_http_data_only")
        all_params.append("_preload_content")
        all_params.append("_request_timeout")

        params = locals()
        for key, val in six.iteritems(params["kwargs"]):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method post_alternate_content_sources_bulk_refresh_all" % key
                )
            params[key] = val
        del params["kwargs"]

        collection_formats = {}

        path_params = {}

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
            "/alternate_content_sources/bulk/refresh_all",
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

    def put_alternate_content_sources_bulk_destroy(self, ids, **kwargs):  # noqa: E501
        """Destroy one or more alternate content sources  # noqa: E501

          # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.put_alternate_content_sources_bulk_destroy(ids, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param list[str] ids: List of alternate content source IDs (required)
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs["_return_http_data_only"] = True
        if kwargs.get("async_req"):
            return self.put_alternate_content_sources_bulk_destroy_with_http_info(
                ids, **kwargs
            )  # noqa: E501
        else:
            (data) = self.put_alternate_content_sources_bulk_destroy_with_http_info(
                ids, **kwargs
            )  # noqa: E501
            return data

    def put_alternate_content_sources_bulk_destroy_with_http_info(
        self, ids, **kwargs
    ):  # noqa: E501
        """Destroy one or more alternate content sources  # noqa: E501

          # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.put_alternate_content_sources_bulk_destroy_with_http_info(ids, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param list[str] ids: List of alternate content source IDs (required)
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ["ids"]  # noqa: E501
        all_params.append("async_req")
        all_params.append("_return_http_data_only")
        all_params.append("_preload_content")
        all_params.append("_request_timeout")

        params = locals()
        for key, val in six.iteritems(params["kwargs"]):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method put_alternate_content_sources_bulk_destroy" % key
                )
            params[key] = val
        del params["kwargs"]
        # verify the required parameter 'ids' is set
        if self.api_client.client_side_validation and (
            "ids" not in params or params["ids"] is None
        ):  # noqa: E501
            raise ValueError(
                "Missing the required parameter `ids` when calling `put_alternate_content_sources_bulk_destroy`"
            )  # noqa: E501

        collection_formats = {}

        path_params = {}

        query_params = []

        header_params = {}

        form_params = []
        local_var_files = {}
        if "ids" in params:
            form_params.append(("ids", params["ids"]))  # noqa: E501
            collection_formats["ids"] = "csv"  # noqa: E501

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
            "/alternate_content_sources/bulk/destroy",
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
