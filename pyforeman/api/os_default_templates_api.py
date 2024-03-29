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


class OsDefaultTemplatesApi(object):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    Ref: https://github.com/swagger-api/swagger-codegen
    """

    def __init__(self, api_client=None):
        if api_client is None:
            api_client = ApiClient()
        self.api_client = api_client

    def delete_operatingsystems_operatingsystem_id_os_default_templates_id(
        self, operatingsystem_id, id, **kwargs
    ):  # noqa: E501
        """Delete a default template combination for an operating system  # noqa: E501

          # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.delete_operatingsystems_operatingsystem_id_os_default_templates_id(operatingsystem_id, id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param float operatingsystem_id: ID of operating system (required)
        :param str id: (required)
        :param float location_id: Set the current location context for the request
        :param float organization_id: Set the current organization context for the request
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs["_return_http_data_only"] = True
        if kwargs.get("async_req"):
            return self.delete_operatingsystems_operatingsystem_id_os_default_templates_id_with_http_info(
                operatingsystem_id, id, **kwargs
            )  # noqa: E501
        else:
            (
                data
            ) = self.delete_operatingsystems_operatingsystem_id_os_default_templates_id_with_http_info(
                operatingsystem_id, id, **kwargs
            )  # noqa: E501
            return data

    def delete_operatingsystems_operatingsystem_id_os_default_templates_id_with_http_info(
        self, operatingsystem_id, id, **kwargs
    ):  # noqa: E501
        """Delete a default template combination for an operating system  # noqa: E501

          # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.delete_operatingsystems_operatingsystem_id_os_default_templates_id_with_http_info(operatingsystem_id, id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param float operatingsystem_id: ID of operating system (required)
        :param str id: (required)
        :param float location_id: Set the current location context for the request
        :param float organization_id: Set the current organization context for the request
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = [
            "operatingsystem_id",
            "id",
            "location_id",
            "organization_id",
        ]  # noqa: E501
        all_params.append("async_req")
        all_params.append("_return_http_data_only")
        all_params.append("_preload_content")
        all_params.append("_request_timeout")

        params = locals()
        for key, val in six.iteritems(params["kwargs"]):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method delete_operatingsystems_operatingsystem_id_os_default_templates_id"
                    % key
                )
            params[key] = val
        del params["kwargs"]
        # verify the required parameter 'operatingsystem_id' is set
        if self.api_client.client_side_validation and (
            "operatingsystem_id" not in params or params["operatingsystem_id"] is None
        ):  # noqa: E501
            raise ValueError(
                "Missing the required parameter `operatingsystem_id` when calling `delete_operatingsystems_operatingsystem_id_os_default_templates_id`"
            )  # noqa: E501
        # verify the required parameter 'id' is set
        if self.api_client.client_side_validation and (
            "id" not in params or params["id"] is None
        ):  # noqa: E501
            raise ValueError(
                "Missing the required parameter `id` when calling `delete_operatingsystems_operatingsystem_id_os_default_templates_id`"
            )  # noqa: E501

        collection_formats = {}

        path_params = {}
        if "operatingsystem_id" in params:
            path_params["operatingsystem_id"] = params[
                "operatingsystem_id"
            ]  # noqa: E501
        if "id" in params:
            path_params["id"] = params["id"]  # noqa: E501

        query_params = []

        header_params = {}

        form_params = []
        local_var_files = {}
        if "location_id" in params:
            form_params.append(("location_id", params["location_id"]))  # noqa: E501
        if "organization_id" in params:
            form_params.append(
                ("organization_id", params["organization_id"])
            )  # noqa: E501

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
            "/operatingsystems/{operatingsystem_id}/os_default_templates/{id}",
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

    def get_operatingsystems_operatingsystem_id_os_default_templates(
        self, operatingsystem_id, provisioning_template_id, **kwargs
    ):  # noqa: E501
        """List default templates combinations for an operating system  # noqa: E501

          # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_operatingsystems_operatingsystem_id_os_default_templates(operatingsystem_id, provisioning_template_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param float operatingsystem_id: ID of operating system (required)
        :param str provisioning_template_id: ID of provisioning template (required)
        :param float location_id: Set the current location context for the request
        :param float organization_id: Set the current organization context for the request
        :param float page: Page number, starting at 1
        :param str per_page: Number of results per page to return, 'all' to return all results
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs["_return_http_data_only"] = True
        if kwargs.get("async_req"):
            return self.get_operatingsystems_operatingsystem_id_os_default_templates_with_http_info(
                operatingsystem_id, provisioning_template_id, **kwargs
            )  # noqa: E501
        else:
            (
                data
            ) = self.get_operatingsystems_operatingsystem_id_os_default_templates_with_http_info(
                operatingsystem_id, provisioning_template_id, **kwargs
            )  # noqa: E501
            return data

    def get_operatingsystems_operatingsystem_id_os_default_templates_with_http_info(
        self, operatingsystem_id, provisioning_template_id, **kwargs
    ):  # noqa: E501
        """List default templates combinations for an operating system  # noqa: E501

          # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_operatingsystems_operatingsystem_id_os_default_templates_with_http_info(operatingsystem_id, provisioning_template_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param float operatingsystem_id: ID of operating system (required)
        :param str provisioning_template_id: ID of provisioning template (required)
        :param float location_id: Set the current location context for the request
        :param float organization_id: Set the current organization context for the request
        :param float page: Page number, starting at 1
        :param str per_page: Number of results per page to return, 'all' to return all results
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = [
            "operatingsystem_id",
            "provisioning_template_id",
            "location_id",
            "organization_id",
            "page",
            "per_page",
        ]  # noqa: E501
        all_params.append("async_req")
        all_params.append("_return_http_data_only")
        all_params.append("_preload_content")
        all_params.append("_request_timeout")

        params = locals()
        for key, val in six.iteritems(params["kwargs"]):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method get_operatingsystems_operatingsystem_id_os_default_templates"
                    % key
                )
            params[key] = val
        del params["kwargs"]
        # verify the required parameter 'operatingsystem_id' is set
        if self.api_client.client_side_validation and (
            "operatingsystem_id" not in params or params["operatingsystem_id"] is None
        ):  # noqa: E501
            raise ValueError(
                "Missing the required parameter `operatingsystem_id` when calling `get_operatingsystems_operatingsystem_id_os_default_templates`"
            )  # noqa: E501
        # verify the required parameter 'provisioning_template_id' is set
        if self.api_client.client_side_validation and (
            "provisioning_template_id" not in params
            or params["provisioning_template_id"] is None
        ):  # noqa: E501
            raise ValueError(
                "Missing the required parameter `provisioning_template_id` when calling `get_operatingsystems_operatingsystem_id_os_default_templates`"
            )  # noqa: E501

        collection_formats = {}

        path_params = {}
        if "operatingsystem_id" in params:
            path_params["operatingsystem_id"] = params[
                "operatingsystem_id"
            ]  # noqa: E501

        query_params = []
        if "provisioning_template_id" in params:
            query_params.append(
                ("provisioning_template_id", params["provisioning_template_id"])
            )  # noqa: E501
        if "location_id" in params:
            query_params.append(("location_id", params["location_id"]))  # noqa: E501
        if "organization_id" in params:
            query_params.append(
                ("organization_id", params["organization_id"])
            )  # noqa: E501
        if "page" in params:
            query_params.append(("page", params["page"]))  # noqa: E501
        if "per_page" in params:
            query_params.append(("per_page", params["per_page"]))  # noqa: E501

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
            "/operatingsystems/{operatingsystem_id}/os_default_templates",
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

    def get_operatingsystems_operatingsystem_id_os_default_templates_id(
        self, operatingsystem_id, id, **kwargs
    ):  # noqa: E501
        """Show a default template combination for an operating system  # noqa: E501

          # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_operatingsystems_operatingsystem_id_os_default_templates_id(operatingsystem_id, id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param float operatingsystem_id: ID of operating system (required)
        :param float id: (required)
        :param float location_id: Set the current location context for the request
        :param float organization_id: Set the current organization context for the request
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs["_return_http_data_only"] = True
        if kwargs.get("async_req"):
            return self.get_operatingsystems_operatingsystem_id_os_default_templates_id_with_http_info(
                operatingsystem_id, id, **kwargs
            )  # noqa: E501
        else:
            (
                data
            ) = self.get_operatingsystems_operatingsystem_id_os_default_templates_id_with_http_info(
                operatingsystem_id, id, **kwargs
            )  # noqa: E501
            return data

    def get_operatingsystems_operatingsystem_id_os_default_templates_id_with_http_info(
        self, operatingsystem_id, id, **kwargs
    ):  # noqa: E501
        """Show a default template combination for an operating system  # noqa: E501

          # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_operatingsystems_operatingsystem_id_os_default_templates_id_with_http_info(operatingsystem_id, id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param float operatingsystem_id: ID of operating system (required)
        :param float id: (required)
        :param float location_id: Set the current location context for the request
        :param float organization_id: Set the current organization context for the request
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = [
            "operatingsystem_id",
            "id",
            "location_id",
            "organization_id",
        ]  # noqa: E501
        all_params.append("async_req")
        all_params.append("_return_http_data_only")
        all_params.append("_preload_content")
        all_params.append("_request_timeout")

        params = locals()
        for key, val in six.iteritems(params["kwargs"]):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method get_operatingsystems_operatingsystem_id_os_default_templates_id"
                    % key
                )
            params[key] = val
        del params["kwargs"]
        # verify the required parameter 'operatingsystem_id' is set
        if self.api_client.client_side_validation and (
            "operatingsystem_id" not in params or params["operatingsystem_id"] is None
        ):  # noqa: E501
            raise ValueError(
                "Missing the required parameter `operatingsystem_id` when calling `get_operatingsystems_operatingsystem_id_os_default_templates_id`"
            )  # noqa: E501
        # verify the required parameter 'id' is set
        if self.api_client.client_side_validation and (
            "id" not in params or params["id"] is None
        ):  # noqa: E501
            raise ValueError(
                "Missing the required parameter `id` when calling `get_operatingsystems_operatingsystem_id_os_default_templates_id`"
            )  # noqa: E501

        collection_formats = {}

        path_params = {}
        if "operatingsystem_id" in params:
            path_params["operatingsystem_id"] = params[
                "operatingsystem_id"
            ]  # noqa: E501
        if "id" in params:
            path_params["id"] = params["id"]  # noqa: E501

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
            "/operatingsystems/{operatingsystem_id}/os_default_templates/{id}",
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

    def get_provisioning_templates_provisioning_template_id_os_default_templates(
        self, provisioning_template_id, operatingsystem_id, **kwargs
    ):  # noqa: E501
        """List operating systems where this template is set as a default  # noqa: E501

          # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_provisioning_templates_provisioning_template_id_os_default_templates(provisioning_template_id, operatingsystem_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str provisioning_template_id: ID of provisioning template (required)
        :param float operatingsystem_id: ID of operating system (required)
        :param float location_id: Set the current location context for the request
        :param float organization_id: Set the current organization context for the request
        :param float page: Page number, starting at 1
        :param str per_page: Number of results per page to return, 'all' to return all results
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs["_return_http_data_only"] = True
        if kwargs.get("async_req"):
            return self.get_provisioning_templates_provisioning_template_id_os_default_templates_with_http_info(
                provisioning_template_id, operatingsystem_id, **kwargs
            )  # noqa: E501
        else:
            (
                data
            ) = self.get_provisioning_templates_provisioning_template_id_os_default_templates_with_http_info(
                provisioning_template_id, operatingsystem_id, **kwargs
            )  # noqa: E501
            return data

    def get_provisioning_templates_provisioning_template_id_os_default_templates_with_http_info(
        self, provisioning_template_id, operatingsystem_id, **kwargs
    ):  # noqa: E501
        """List operating systems where this template is set as a default  # noqa: E501

          # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_provisioning_templates_provisioning_template_id_os_default_templates_with_http_info(provisioning_template_id, operatingsystem_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str provisioning_template_id: ID of provisioning template (required)
        :param float operatingsystem_id: ID of operating system (required)
        :param float location_id: Set the current location context for the request
        :param float organization_id: Set the current organization context for the request
        :param float page: Page number, starting at 1
        :param str per_page: Number of results per page to return, 'all' to return all results
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = [
            "provisioning_template_id",
            "operatingsystem_id",
            "location_id",
            "organization_id",
            "page",
            "per_page",
        ]  # noqa: E501
        all_params.append("async_req")
        all_params.append("_return_http_data_only")
        all_params.append("_preload_content")
        all_params.append("_request_timeout")

        params = locals()
        for key, val in six.iteritems(params["kwargs"]):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method get_provisioning_templates_provisioning_template_id_os_default_templates"
                    % key
                )
            params[key] = val
        del params["kwargs"]
        # verify the required parameter 'provisioning_template_id' is set
        if self.api_client.client_side_validation and (
            "provisioning_template_id" not in params
            or params["provisioning_template_id"] is None
        ):  # noqa: E501
            raise ValueError(
                "Missing the required parameter `provisioning_template_id` when calling `get_provisioning_templates_provisioning_template_id_os_default_templates`"
            )  # noqa: E501
        # verify the required parameter 'operatingsystem_id' is set
        if self.api_client.client_side_validation and (
            "operatingsystem_id" not in params or params["operatingsystem_id"] is None
        ):  # noqa: E501
            raise ValueError(
                "Missing the required parameter `operatingsystem_id` when calling `get_provisioning_templates_provisioning_template_id_os_default_templates`"
            )  # noqa: E501

        collection_formats = {}

        path_params = {}
        if "provisioning_template_id" in params:
            path_params["provisioning_template_id"] = params[
                "provisioning_template_id"
            ]  # noqa: E501

        query_params = []
        if "operatingsystem_id" in params:
            query_params.append(
                ("operatingsystem_id", params["operatingsystem_id"])
            )  # noqa: E501
        if "location_id" in params:
            query_params.append(("location_id", params["location_id"]))  # noqa: E501
        if "organization_id" in params:
            query_params.append(
                ("organization_id", params["organization_id"])
            )  # noqa: E501
        if "page" in params:
            query_params.append(("page", params["page"]))  # noqa: E501
        if "per_page" in params:
            query_params.append(("per_page", params["per_page"]))  # noqa: E501

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
            "/provisioning_templates/{provisioning_template_id}/os_default_templates",
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

    def post_operatingsystems_operatingsystem_id_os_default_templates(
        self, operatingsystem_id, **kwargs
    ):  # noqa: E501
        """Create a default template combination for an operating system  # noqa: E501

          # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.post_operatingsystems_operatingsystem_id_os_default_templates(operatingsystem_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param float operatingsystem_id: ID of operating system (required)
        :param float location_id: Set the current location context for the request
        :param float organization_id: Set the current organization context for the request
        :param float os_default_template_template_kind_id:
        :param float os_default_template_provisioning_template_id: ID of provisioning template
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs["_return_http_data_only"] = True
        if kwargs.get("async_req"):
            return self.post_operatingsystems_operatingsystem_id_os_default_templates_with_http_info(
                operatingsystem_id, **kwargs
            )  # noqa: E501
        else:
            (
                data
            ) = self.post_operatingsystems_operatingsystem_id_os_default_templates_with_http_info(
                operatingsystem_id, **kwargs
            )  # noqa: E501
            return data

    def post_operatingsystems_operatingsystem_id_os_default_templates_with_http_info(
        self, operatingsystem_id, **kwargs
    ):  # noqa: E501
        """Create a default template combination for an operating system  # noqa: E501

          # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.post_operatingsystems_operatingsystem_id_os_default_templates_with_http_info(operatingsystem_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param float operatingsystem_id: ID of operating system (required)
        :param float location_id: Set the current location context for the request
        :param float organization_id: Set the current organization context for the request
        :param float os_default_template_template_kind_id:
        :param float os_default_template_provisioning_template_id: ID of provisioning template
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = [
            "operatingsystem_id",
            "location_id",
            "organization_id",
            "os_default_template_template_kind_id",
            "os_default_template_provisioning_template_id",
        ]  # noqa: E501
        all_params.append("async_req")
        all_params.append("_return_http_data_only")
        all_params.append("_preload_content")
        all_params.append("_request_timeout")

        params = locals()
        for key, val in six.iteritems(params["kwargs"]):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method post_operatingsystems_operatingsystem_id_os_default_templates"
                    % key
                )
            params[key] = val
        del params["kwargs"]
        # verify the required parameter 'operatingsystem_id' is set
        if self.api_client.client_side_validation and (
            "operatingsystem_id" not in params or params["operatingsystem_id"] is None
        ):  # noqa: E501
            raise ValueError(
                "Missing the required parameter `operatingsystem_id` when calling `post_operatingsystems_operatingsystem_id_os_default_templates`"
            )  # noqa: E501

        collection_formats = {}

        path_params = {}
        if "operatingsystem_id" in params:
            path_params["operatingsystem_id"] = params[
                "operatingsystem_id"
            ]  # noqa: E501

        query_params = []

        header_params = {}

        form_params = []
        local_var_files = {}
        if "location_id" in params:
            form_params.append(("location_id", params["location_id"]))  # noqa: E501
        if "organization_id" in params:
            form_params.append(
                ("organization_id", params["organization_id"])
            )  # noqa: E501
        if "os_default_template_template_kind_id" in params:
            form_params.append(
                (
                    "os_default_template[template_kind_id]",
                    params["os_default_template_template_kind_id"],
                )
            )  # noqa: E501
        if "os_default_template_provisioning_template_id" in params:
            form_params.append(
                (
                    "os_default_template[provisioning_template_id]",
                    params["os_default_template_provisioning_template_id"],
                )
            )  # noqa: E501

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
            "/operatingsystems/{operatingsystem_id}/os_default_templates",
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

    def put_operatingsystems_operatingsystem_id_os_default_templates_id(
        self, operatingsystem_id, id, **kwargs
    ):  # noqa: E501
        """Update a default template combination for an operating system  # noqa: E501

          # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.put_operatingsystems_operatingsystem_id_os_default_templates_id(operatingsystem_id, id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param float operatingsystem_id: ID of operating system (required)
        :param str id: (required)
        :param float location_id: Set the current location context for the request
        :param float organization_id: Set the current organization context for the request
        :param float os_default_template_template_kind_id:
        :param float os_default_template_provisioning_template_id: ID of provisioning template
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs["_return_http_data_only"] = True
        if kwargs.get("async_req"):
            return self.put_operatingsystems_operatingsystem_id_os_default_templates_id_with_http_info(
                operatingsystem_id, id, **kwargs
            )  # noqa: E501
        else:
            (
                data
            ) = self.put_operatingsystems_operatingsystem_id_os_default_templates_id_with_http_info(
                operatingsystem_id, id, **kwargs
            )  # noqa: E501
            return data

    def put_operatingsystems_operatingsystem_id_os_default_templates_id_with_http_info(
        self, operatingsystem_id, id, **kwargs
    ):  # noqa: E501
        """Update a default template combination for an operating system  # noqa: E501

          # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.put_operatingsystems_operatingsystem_id_os_default_templates_id_with_http_info(operatingsystem_id, id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param float operatingsystem_id: ID of operating system (required)
        :param str id: (required)
        :param float location_id: Set the current location context for the request
        :param float organization_id: Set the current organization context for the request
        :param float os_default_template_template_kind_id:
        :param float os_default_template_provisioning_template_id: ID of provisioning template
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = [
            "operatingsystem_id",
            "id",
            "location_id",
            "organization_id",
            "os_default_template_template_kind_id",
            "os_default_template_provisioning_template_id",
        ]  # noqa: E501
        all_params.append("async_req")
        all_params.append("_return_http_data_only")
        all_params.append("_preload_content")
        all_params.append("_request_timeout")

        params = locals()
        for key, val in six.iteritems(params["kwargs"]):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method put_operatingsystems_operatingsystem_id_os_default_templates_id"
                    % key
                )
            params[key] = val
        del params["kwargs"]
        # verify the required parameter 'operatingsystem_id' is set
        if self.api_client.client_side_validation and (
            "operatingsystem_id" not in params or params["operatingsystem_id"] is None
        ):  # noqa: E501
            raise ValueError(
                "Missing the required parameter `operatingsystem_id` when calling `put_operatingsystems_operatingsystem_id_os_default_templates_id`"
            )  # noqa: E501
        # verify the required parameter 'id' is set
        if self.api_client.client_side_validation and (
            "id" not in params or params["id"] is None
        ):  # noqa: E501
            raise ValueError(
                "Missing the required parameter `id` when calling `put_operatingsystems_operatingsystem_id_os_default_templates_id`"
            )  # noqa: E501

        collection_formats = {}

        path_params = {}
        if "operatingsystem_id" in params:
            path_params["operatingsystem_id"] = params[
                "operatingsystem_id"
            ]  # noqa: E501
        if "id" in params:
            path_params["id"] = params["id"]  # noqa: E501

        query_params = []

        header_params = {}

        form_params = []
        local_var_files = {}
        if "location_id" in params:
            form_params.append(("location_id", params["location_id"]))  # noqa: E501
        if "organization_id" in params:
            form_params.append(
                ("organization_id", params["organization_id"])
            )  # noqa: E501
        if "os_default_template_template_kind_id" in params:
            form_params.append(
                (
                    "os_default_template[template_kind_id]",
                    params["os_default_template_template_kind_id"],
                )
            )  # noqa: E501
        if "os_default_template_provisioning_template_id" in params:
            form_params.append(
                (
                    "os_default_template[provisioning_template_id]",
                    params["os_default_template_provisioning_template_id"],
                )
            )  # noqa: E501

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
            "/operatingsystems/{operatingsystem_id}/os_default_templates/{id}",
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
