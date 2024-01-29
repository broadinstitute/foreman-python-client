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


class PluginsApi(object):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    Ref: https://github.com/swagger-api/swagger-codegen
    """

    def __init__(self, api_client=None):
        if api_client is None:
            api_client = ApiClient()
        self.api_client = api_client

    def get_plugins(self, **kwargs):  # noqa: E501
        """List installed plugins  # noqa: E501

          # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_plugins(async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param float location_id: Set the current location context for the request
        :param float organization_id: Set the current organization context for the request
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs["_return_http_data_only"] = True
        if kwargs.get("async_req"):
            return self.get_plugins_with_http_info(**kwargs)  # noqa: E501
        else:
            (data) = self.get_plugins_with_http_info(**kwargs)  # noqa: E501
            return data

    def get_plugins_with_http_info(self, **kwargs):  # noqa: E501
        """List installed plugins  # noqa: E501

          # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_plugins_with_http_info(async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param float location_id: Set the current location context for the request
        :param float organization_id: Set the current organization context for the request
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ["location_id", "organization_id"]  # noqa: E501
        all_params.append("async_req")
        all_params.append("_return_http_data_only")
        all_params.append("_preload_content")
        all_params.append("_request_timeout")

        params = locals()
        for key, val in six.iteritems(params["kwargs"]):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method get_plugins" % key
                )
            params[key] = val
        del params["kwargs"]

        collection_formats = {}

        path_params = {}

        query_params = []
        if "location_id" in params:
            query_params.append(("location_id", params["location_id"]))  # noqa: E501
        if "organization_id" in params:
            query_params.append(
                ("organization_id", params["organization_id"])
            )  # noqa: E501

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
            "/plugins",
            "GET",
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