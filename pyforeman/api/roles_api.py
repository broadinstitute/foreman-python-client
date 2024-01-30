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


class RolesApi(object):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    Ref: https://github.com/swagger-api/swagger-codegen
    """

    def __init__(self, api_client=None):
        if api_client is None:
            api_client = ApiClient()
        self.api_client = api_client

    def delete_roles_id(self, id, **kwargs):  # noqa: E501
        """Delete a role  # noqa: E501

          # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.delete_roles_id(id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str id: (required)
        :param float location_id: Set the current location context for the request
        :param float organization_id: Set the current organization context for the request
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs["_return_http_data_only"] = True
        if kwargs.get("async_req"):
            return self.delete_roles_id_with_http_info(id, **kwargs)  # noqa: E501
        else:
            (data) = self.delete_roles_id_with_http_info(id, **kwargs)  # noqa: E501
            return data

    def delete_roles_id_with_http_info(self, id, **kwargs):  # noqa: E501
        """Delete a role  # noqa: E501

          # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.delete_roles_id_with_http_info(id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str id: (required)
        :param float location_id: Set the current location context for the request
        :param float organization_id: Set the current organization context for the request
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ["id", "location_id", "organization_id"]  # noqa: E501
        all_params.append("async_req")
        all_params.append("_return_http_data_only")
        all_params.append("_preload_content")
        all_params.append("_request_timeout")

        params = locals()
        for key, val in six.iteritems(params["kwargs"]):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method delete_roles_id" % key
                )
            params[key] = val
        del params["kwargs"]
        # verify the required parameter 'id' is set
        if self.api_client.client_side_validation and (
            "id" not in params or params["id"] is None
        ):  # noqa: E501
            raise ValueError(
                "Missing the required parameter `id` when calling `delete_roles_id`"
            )  # noqa: E501

        collection_formats = {}

        path_params = {}
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
            "/roles/{id}",
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

    def get_roles(self, **kwargs):  # noqa: E501
        """List all roles  # noqa: E501

          # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_roles(async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param float location_id: Set the current location context for the request
        :param float organization_id: Set the current organization context for the request
        :param str search: filter results
        :param str order: Sort and order by a searchable field, e.g. '<field> DESC'
        :param float page: Page number, starting at 1
        :param str per_page: Number of results per page to return, 'all' to return all results
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs["_return_http_data_only"] = True
        if kwargs.get("async_req"):
            return self.get_roles_with_http_info(**kwargs)  # noqa: E501
        else:
            (data) = self.get_roles_with_http_info(**kwargs)  # noqa: E501
            return data

    def get_roles_with_http_info(self, **kwargs):  # noqa: E501
        """List all roles  # noqa: E501

          # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_roles_with_http_info(async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param float location_id: Set the current location context for the request
        :param float organization_id: Set the current organization context for the request
        :param str search: filter results
        :param str order: Sort and order by a searchable field, e.g. '<field> DESC'
        :param float page: Page number, starting at 1
        :param str per_page: Number of results per page to return, 'all' to return all results
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = [
            "location_id",
            "organization_id",
            "search",
            "order",
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
                    " to method get_roles" % key
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
        if "search" in params:
            query_params.append(("search", params["search"]))  # noqa: E501
        if "order" in params:
            query_params.append(("order", params["order"]))  # noqa: E501
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
            "/roles",
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

    def get_roles_id(self, id, **kwargs):  # noqa: E501
        """Show a role  # noqa: E501

          # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_roles_id(id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str id: (required)
        :param float location_id: Set the current location context for the request
        :param float organization_id: Set the current organization context for the request
        :param str description:
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs["_return_http_data_only"] = True
        if kwargs.get("async_req"):
            return self.get_roles_id_with_http_info(id, **kwargs)  # noqa: E501
        else:
            (data) = self.get_roles_id_with_http_info(id, **kwargs)  # noqa: E501
            return data

    def get_roles_id_with_http_info(self, id, **kwargs):  # noqa: E501
        """Show a role  # noqa: E501

          # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_roles_id_with_http_info(id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str id: (required)
        :param float location_id: Set the current location context for the request
        :param float organization_id: Set the current organization context for the request
        :param str description:
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = [
            "id",
            "location_id",
            "organization_id",
            "description",
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
                    " to method get_roles_id" % key
                )
            params[key] = val
        del params["kwargs"]
        # verify the required parameter 'id' is set
        if self.api_client.client_side_validation and (
            "id" not in params or params["id"] is None
        ):  # noqa: E501
            raise ValueError(
                "Missing the required parameter `id` when calling `get_roles_id`"
            )  # noqa: E501

        collection_formats = {}

        path_params = {}
        if "id" in params:
            path_params["id"] = params["id"]  # noqa: E501

        query_params = []
        if "location_id" in params:
            query_params.append(("location_id", params["location_id"]))  # noqa: E501
        if "organization_id" in params:
            query_params.append(
                ("organization_id", params["organization_id"])
            )  # noqa: E501
        if "description" in params:
            query_params.append(("description", params["description"]))  # noqa: E501

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
            "/roles/{id}",
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

    def post_roles(self, role_name, **kwargs):  # noqa: E501
        """Create a role  # noqa: E501

          # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.post_roles(role_name, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str role_name: (required)
        :param float location_id: Set the current location context for the request
        :param float organization_id: Set the current organization context for the request
        :param str role_description: Role description
        :param list[str] role_location_ids: REPLACE locations with given ids
        :param list[str] role_organization_ids: REPLACE organizations with given ids.
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs["_return_http_data_only"] = True
        if kwargs.get("async_req"):
            return self.post_roles_with_http_info(role_name, **kwargs)  # noqa: E501
        else:
            (data) = self.post_roles_with_http_info(role_name, **kwargs)  # noqa: E501
            return data

    def post_roles_with_http_info(self, role_name, **kwargs):  # noqa: E501
        """Create a role  # noqa: E501

          # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.post_roles_with_http_info(role_name, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str role_name: (required)
        :param float location_id: Set the current location context for the request
        :param float organization_id: Set the current organization context for the request
        :param str role_description: Role description
        :param list[str] role_location_ids: REPLACE locations with given ids
        :param list[str] role_organization_ids: REPLACE organizations with given ids.
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = [
            "role_name",
            "location_id",
            "organization_id",
            "role_description",
            "role_location_ids",
            "role_organization_ids",
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
                    " to method post_roles" % key
                )
            params[key] = val
        del params["kwargs"]
        # verify the required parameter 'role_name' is set
        if self.api_client.client_side_validation and (
            "role_name" not in params or params["role_name"] is None
        ):  # noqa: E501
            raise ValueError(
                "Missing the required parameter `role_name` when calling `post_roles`"
            )  # noqa: E501

        collection_formats = {}

        path_params = {}

        query_params = []

        header_params = {}

        form_params = []
        local_var_files = {}
        if "role_name" in params:
            form_params.append(("role[name]", params["role_name"]))  # noqa: E501
        if "location_id" in params:
            form_params.append(("location_id", params["location_id"]))  # noqa: E501
        if "organization_id" in params:
            form_params.append(
                ("organization_id", params["organization_id"])
            )  # noqa: E501
        if "role_description" in params:
            form_params.append(
                ("role[description]", params["role_description"])
            )  # noqa: E501
        if "role_location_ids" in params:
            form_params.append(
                ("role[location_ids]", params["role_location_ids"])
            )  # noqa: E501
            collection_formats["role[location_ids]"] = "csv"  # noqa: E501
        if "role_organization_ids" in params:
            form_params.append(
                ("role[organization_ids]", params["role_organization_ids"])
            )  # noqa: E501
            collection_formats["role[organization_ids]"] = "csv"  # noqa: E501

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
            "/roles",
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

    def post_roles_id_clone(self, id, **kwargs):  # noqa: E501
        """Clone a role  # noqa: E501

          # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.post_roles_id_clone(id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str id: (required)
        :param float location_id: Set the current location context for the request
        :param float organization_id: Set the current organization context for the request
        :param str role_name:
        :param str role_description: Role description
        :param list[str] role_location_ids: REPLACE locations with given ids
        :param list[str] role_organization_ids: REPLACE organizations with given ids.
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs["_return_http_data_only"] = True
        if kwargs.get("async_req"):
            return self.post_roles_id_clone_with_http_info(id, **kwargs)  # noqa: E501
        else:
            (data) = self.post_roles_id_clone_with_http_info(id, **kwargs)  # noqa: E501
            return data

    def post_roles_id_clone_with_http_info(self, id, **kwargs):  # noqa: E501
        """Clone a role  # noqa: E501

          # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.post_roles_id_clone_with_http_info(id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str id: (required)
        :param float location_id: Set the current location context for the request
        :param float organization_id: Set the current organization context for the request
        :param str role_name:
        :param str role_description: Role description
        :param list[str] role_location_ids: REPLACE locations with given ids
        :param list[str] role_organization_ids: REPLACE organizations with given ids.
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = [
            "id",
            "location_id",
            "organization_id",
            "role_name",
            "role_description",
            "role_location_ids",
            "role_organization_ids",
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
                    " to method post_roles_id_clone" % key
                )
            params[key] = val
        del params["kwargs"]
        # verify the required parameter 'id' is set
        if self.api_client.client_side_validation and (
            "id" not in params or params["id"] is None
        ):  # noqa: E501
            raise ValueError(
                "Missing the required parameter `id` when calling `post_roles_id_clone`"
            )  # noqa: E501

        collection_formats = {}

        path_params = {}
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
        if "role_name" in params:
            form_params.append(("role[name]", params["role_name"]))  # noqa: E501
        if "role_description" in params:
            form_params.append(
                ("role[description]", params["role_description"])
            )  # noqa: E501
        if "role_location_ids" in params:
            form_params.append(
                ("role[location_ids]", params["role_location_ids"])
            )  # noqa: E501
            collection_formats["role[location_ids]"] = "csv"  # noqa: E501
        if "role_organization_ids" in params:
            form_params.append(
                ("role[organization_ids]", params["role_organization_ids"])
            )  # noqa: E501
            collection_formats["role[organization_ids]"] = "csv"  # noqa: E501

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
            "/roles/{id}/clone",
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

    def put_roles_id(self, id, **kwargs):  # noqa: E501
        """Update a role  # noqa: E501

          # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.put_roles_id(id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str id: (required)
        :param float location_id: Set the current location context for the request
        :param float organization_id: Set the current organization context for the request
        :param str role_name:
        :param str role_description: Role description
        :param list[str] role_location_ids: REPLACE locations with given ids
        :param list[str] role_organization_ids: REPLACE organizations with given ids.
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs["_return_http_data_only"] = True
        if kwargs.get("async_req"):
            return self.put_roles_id_with_http_info(id, **kwargs)  # noqa: E501
        else:
            (data) = self.put_roles_id_with_http_info(id, **kwargs)  # noqa: E501
            return data

    def put_roles_id_with_http_info(self, id, **kwargs):  # noqa: E501
        """Update a role  # noqa: E501

          # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.put_roles_id_with_http_info(id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str id: (required)
        :param float location_id: Set the current location context for the request
        :param float organization_id: Set the current organization context for the request
        :param str role_name:
        :param str role_description: Role description
        :param list[str] role_location_ids: REPLACE locations with given ids
        :param list[str] role_organization_ids: REPLACE organizations with given ids.
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = [
            "id",
            "location_id",
            "organization_id",
            "role_name",
            "role_description",
            "role_location_ids",
            "role_organization_ids",
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
                    " to method put_roles_id" % key
                )
            params[key] = val
        del params["kwargs"]
        # verify the required parameter 'id' is set
        if self.api_client.client_side_validation and (
            "id" not in params or params["id"] is None
        ):  # noqa: E501
            raise ValueError(
                "Missing the required parameter `id` when calling `put_roles_id`"
            )  # noqa: E501

        collection_formats = {}

        path_params = {}
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
        if "role_name" in params:
            form_params.append(("role[name]", params["role_name"]))  # noqa: E501
        if "role_description" in params:
            form_params.append(
                ("role[description]", params["role_description"])
            )  # noqa: E501
        if "role_location_ids" in params:
            form_params.append(
                ("role[location_ids]", params["role_location_ids"])
            )  # noqa: E501
            collection_formats["role[location_ids]"] = "csv"  # noqa: E501
        if "role_organization_ids" in params:
            form_params.append(
                ("role[organization_ids]", params["role_organization_ids"])
            )  # noqa: E501
            collection_formats["role[organization_ids]"] = "csv"  # noqa: E501

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
            "/roles/{id}",
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
