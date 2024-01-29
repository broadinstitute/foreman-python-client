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


class ContentViewComponentsApi(object):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    Ref: https://github.com/swagger-api/swagger-codegen
    """

    def __init__(self, api_client=None):
        if api_client is None:
            api_client = ApiClient()
        self.api_client = api_client

    def get_content_views_composite_content_view_id_content_view_components(
        self, composite_content_view_id, **kwargs
    ):  # noqa: E501
        """List components attached to this content view  # noqa: E501

          # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_content_views_composite_content_view_id_content_view_components(composite_content_view_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param float composite_content_view_id: composite content view identifier (required)
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs["_return_http_data_only"] = True
        if kwargs.get("async_req"):
            return self.get_content_views_composite_content_view_id_content_view_components_with_http_info(
                composite_content_view_id, **kwargs
            )  # noqa: E501
        else:
            (
                data
            ) = self.get_content_views_composite_content_view_id_content_view_components_with_http_info(
                composite_content_view_id, **kwargs
            )  # noqa: E501
            return data

    def get_content_views_composite_content_view_id_content_view_components_with_http_info(
        self, composite_content_view_id, **kwargs
    ):  # noqa: E501
        """List components attached to this content view  # noqa: E501

          # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_content_views_composite_content_view_id_content_view_components_with_http_info(composite_content_view_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param float composite_content_view_id: composite content view identifier (required)
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ["composite_content_view_id"]  # noqa: E501
        all_params.append("async_req")
        all_params.append("_return_http_data_only")
        all_params.append("_preload_content")
        all_params.append("_request_timeout")

        params = locals()
        for key, val in six.iteritems(params["kwargs"]):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method get_content_views_composite_content_view_id_content_view_components"
                    % key
                )
            params[key] = val
        del params["kwargs"]
        # verify the required parameter 'composite_content_view_id' is set
        if self.api_client.client_side_validation and (
            "composite_content_view_id" not in params
            or params["composite_content_view_id"] is None
        ):  # noqa: E501
            raise ValueError(
                "Missing the required parameter `composite_content_view_id` when calling `get_content_views_composite_content_view_id_content_view_components`"
            )  # noqa: E501

        collection_formats = {}

        path_params = {}
        if "composite_content_view_id" in params:
            path_params["composite_content_view_id"] = params[
                "composite_content_view_id"
            ]  # noqa: E501

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
            "/content_views/{composite_content_view_id}/content_view_components",
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

    def get_content_views_composite_content_view_id_content_view_components_id(
        self, composite_content_view_id, id, **kwargs
    ):  # noqa: E501
        """Show a content view component  # noqa: E501

          # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_content_views_composite_content_view_id_content_view_components_id(composite_content_view_id, id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param float composite_content_view_id: composite content view numeric identifier (required)
        :param float id: content view component ID. Identifier of the component association (required)
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs["_return_http_data_only"] = True
        if kwargs.get("async_req"):
            return self.get_content_views_composite_content_view_id_content_view_components_id_with_http_info(
                composite_content_view_id, id, **kwargs
            )  # noqa: E501
        else:
            (
                data
            ) = self.get_content_views_composite_content_view_id_content_view_components_id_with_http_info(
                composite_content_view_id, id, **kwargs
            )  # noqa: E501
            return data

    def get_content_views_composite_content_view_id_content_view_components_id_with_http_info(
        self, composite_content_view_id, id, **kwargs
    ):  # noqa: E501
        """Show a content view component  # noqa: E501

          # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_content_views_composite_content_view_id_content_view_components_id_with_http_info(composite_content_view_id, id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param float composite_content_view_id: composite content view numeric identifier (required)
        :param float id: content view component ID. Identifier of the component association (required)
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ["composite_content_view_id", "id"]  # noqa: E501
        all_params.append("async_req")
        all_params.append("_return_http_data_only")
        all_params.append("_preload_content")
        all_params.append("_request_timeout")

        params = locals()
        for key, val in six.iteritems(params["kwargs"]):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method get_content_views_composite_content_view_id_content_view_components_id"
                    % key
                )
            params[key] = val
        del params["kwargs"]
        # verify the required parameter 'composite_content_view_id' is set
        if self.api_client.client_side_validation and (
            "composite_content_view_id" not in params
            or params["composite_content_view_id"] is None
        ):  # noqa: E501
            raise ValueError(
                "Missing the required parameter `composite_content_view_id` when calling `get_content_views_composite_content_view_id_content_view_components_id`"
            )  # noqa: E501
        # verify the required parameter 'id' is set
        if self.api_client.client_side_validation and (
            "id" not in params or params["id"] is None
        ):  # noqa: E501
            raise ValueError(
                "Missing the required parameter `id` when calling `get_content_views_composite_content_view_id_content_view_components_id`"
            )  # noqa: E501

        collection_formats = {}

        path_params = {}
        if "composite_content_view_id" in params:
            path_params["composite_content_view_id"] = params[
                "composite_content_view_id"
            ]  # noqa: E501
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
            "/content_views/{composite_content_view_id}/content_view_components/{id}",
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

    def put_content_views_composite_content_view_id_content_view_components_add(
        self, composite_content_view_id, components, **kwargs
    ):  # noqa: E501
        """Add components to the content view  # noqa: E501

          # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.put_content_views_composite_content_view_id_content_view_components_add(composite_content_view_id, components, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param float composite_content_view_id: composite content view identifier (required)
        :param list[str] components: Array of components to add (required)
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs["_return_http_data_only"] = True
        if kwargs.get("async_req"):
            return self.put_content_views_composite_content_view_id_content_view_components_add_with_http_info(
                composite_content_view_id, components, **kwargs
            )  # noqa: E501
        else:
            (
                data
            ) = self.put_content_views_composite_content_view_id_content_view_components_add_with_http_info(
                composite_content_view_id, components, **kwargs
            )  # noqa: E501
            return data

    def put_content_views_composite_content_view_id_content_view_components_add_with_http_info(
        self, composite_content_view_id, components, **kwargs
    ):  # noqa: E501
        """Add components to the content view  # noqa: E501

          # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.put_content_views_composite_content_view_id_content_view_components_add_with_http_info(composite_content_view_id, components, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param float composite_content_view_id: composite content view identifier (required)
        :param list[str] components: Array of components to add (required)
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ["composite_content_view_id", "components"]  # noqa: E501
        all_params.append("async_req")
        all_params.append("_return_http_data_only")
        all_params.append("_preload_content")
        all_params.append("_request_timeout")

        params = locals()
        for key, val in six.iteritems(params["kwargs"]):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method put_content_views_composite_content_view_id_content_view_components_add"
                    % key
                )
            params[key] = val
        del params["kwargs"]
        # verify the required parameter 'composite_content_view_id' is set
        if self.api_client.client_side_validation and (
            "composite_content_view_id" not in params
            or params["composite_content_view_id"] is None
        ):  # noqa: E501
            raise ValueError(
                "Missing the required parameter `composite_content_view_id` when calling `put_content_views_composite_content_view_id_content_view_components_add`"
            )  # noqa: E501
        # verify the required parameter 'components' is set
        if self.api_client.client_side_validation and (
            "components" not in params or params["components"] is None
        ):  # noqa: E501
            raise ValueError(
                "Missing the required parameter `components` when calling `put_content_views_composite_content_view_id_content_view_components_add`"
            )  # noqa: E501

        collection_formats = {}

        path_params = {}
        if "composite_content_view_id" in params:
            path_params["composite_content_view_id"] = params[
                "composite_content_view_id"
            ]  # noqa: E501

        query_params = []

        header_params = {}

        form_params = []
        local_var_files = {}
        if "components" in params:
            form_params.append(("components", params["components"]))  # noqa: E501
            collection_formats["components"] = "csv"  # noqa: E501

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
            "/content_views/{composite_content_view_id}/content_view_components/add",
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

    def put_content_views_composite_content_view_id_content_view_components_id(
        self, composite_content_view_id, id, **kwargs
    ):  # noqa: E501
        """Update a component associated with the content view  # noqa: E501

          # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.put_content_views_composite_content_view_id_content_view_components_id(composite_content_view_id, id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param float composite_content_view_id: composite content view identifier (required)
        :param float id: content view component ID. Identifier of the component association (required)
        :param float content_view_version_id: identifier of the version of the component content view
        :param bool latest: true if the latest version of the components content view is desired
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs["_return_http_data_only"] = True
        if kwargs.get("async_req"):
            return self.put_content_views_composite_content_view_id_content_view_components_id_with_http_info(
                composite_content_view_id, id, **kwargs
            )  # noqa: E501
        else:
            (
                data
            ) = self.put_content_views_composite_content_view_id_content_view_components_id_with_http_info(
                composite_content_view_id, id, **kwargs
            )  # noqa: E501
            return data

    def put_content_views_composite_content_view_id_content_view_components_id_with_http_info(
        self, composite_content_view_id, id, **kwargs
    ):  # noqa: E501
        """Update a component associated with the content view  # noqa: E501

          # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.put_content_views_composite_content_view_id_content_view_components_id_with_http_info(composite_content_view_id, id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param float composite_content_view_id: composite content view identifier (required)
        :param float id: content view component ID. Identifier of the component association (required)
        :param float content_view_version_id: identifier of the version of the component content view
        :param bool latest: true if the latest version of the components content view is desired
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = [
            "composite_content_view_id",
            "id",
            "content_view_version_id",
            "latest",
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
                    " to method put_content_views_composite_content_view_id_content_view_components_id"
                    % key
                )
            params[key] = val
        del params["kwargs"]
        # verify the required parameter 'composite_content_view_id' is set
        if self.api_client.client_side_validation and (
            "composite_content_view_id" not in params
            or params["composite_content_view_id"] is None
        ):  # noqa: E501
            raise ValueError(
                "Missing the required parameter `composite_content_view_id` when calling `put_content_views_composite_content_view_id_content_view_components_id`"
            )  # noqa: E501
        # verify the required parameter 'id' is set
        if self.api_client.client_side_validation and (
            "id" not in params or params["id"] is None
        ):  # noqa: E501
            raise ValueError(
                "Missing the required parameter `id` when calling `put_content_views_composite_content_view_id_content_view_components_id`"
            )  # noqa: E501

        collection_formats = {}

        path_params = {}
        if "composite_content_view_id" in params:
            path_params["composite_content_view_id"] = params[
                "composite_content_view_id"
            ]  # noqa: E501
        if "id" in params:
            path_params["id"] = params["id"]  # noqa: E501

        query_params = []

        header_params = {}

        form_params = []
        local_var_files = {}
        if "content_view_version_id" in params:
            form_params.append(
                ("content_view_version_id", params["content_view_version_id"])
            )  # noqa: E501
        if "latest" in params:
            form_params.append(("latest", params["latest"]))  # noqa: E501

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
            "/content_views/{composite_content_view_id}/content_view_components/{id}",
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

    def put_content_views_composite_content_view_id_content_view_components_remove(
        self, composite_content_view_id, component_ids, **kwargs
    ):  # noqa: E501
        """Remove components from the content view  # noqa: E501

          # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.put_content_views_composite_content_view_id_content_view_components_remove(composite_content_view_id, component_ids, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param float composite_content_view_id: composite content view identifier (required)
        :param list[str] component_ids: Array of content view component IDs to remove. Identifier of the component association (required)
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs["_return_http_data_only"] = True
        if kwargs.get("async_req"):
            return self.put_content_views_composite_content_view_id_content_view_components_remove_with_http_info(
                composite_content_view_id, component_ids, **kwargs
            )  # noqa: E501
        else:
            (
                data
            ) = self.put_content_views_composite_content_view_id_content_view_components_remove_with_http_info(
                composite_content_view_id, component_ids, **kwargs
            )  # noqa: E501
            return data

    def put_content_views_composite_content_view_id_content_view_components_remove_with_http_info(
        self, composite_content_view_id, component_ids, **kwargs
    ):  # noqa: E501
        """Remove components from the content view  # noqa: E501

          # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.put_content_views_composite_content_view_id_content_view_components_remove_with_http_info(composite_content_view_id, component_ids, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param float composite_content_view_id: composite content view identifier (required)
        :param list[str] component_ids: Array of content view component IDs to remove. Identifier of the component association (required)
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ["composite_content_view_id", "component_ids"]  # noqa: E501
        all_params.append("async_req")
        all_params.append("_return_http_data_only")
        all_params.append("_preload_content")
        all_params.append("_request_timeout")

        params = locals()
        for key, val in six.iteritems(params["kwargs"]):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method put_content_views_composite_content_view_id_content_view_components_remove"
                    % key
                )
            params[key] = val
        del params["kwargs"]
        # verify the required parameter 'composite_content_view_id' is set
        if self.api_client.client_side_validation and (
            "composite_content_view_id" not in params
            or params["composite_content_view_id"] is None
        ):  # noqa: E501
            raise ValueError(
                "Missing the required parameter `composite_content_view_id` when calling `put_content_views_composite_content_view_id_content_view_components_remove`"
            )  # noqa: E501
        # verify the required parameter 'component_ids' is set
        if self.api_client.client_side_validation and (
            "component_ids" not in params or params["component_ids"] is None
        ):  # noqa: E501
            raise ValueError(
                "Missing the required parameter `component_ids` when calling `put_content_views_composite_content_view_id_content_view_components_remove`"
            )  # noqa: E501

        collection_formats = {}

        path_params = {}
        if "composite_content_view_id" in params:
            path_params["composite_content_view_id"] = params[
                "composite_content_view_id"
            ]  # noqa: E501

        query_params = []

        header_params = {}

        form_params = []
        local_var_files = {}
        if "component_ids" in params:
            form_params.append(("component_ids", params["component_ids"]))  # noqa: E501
            collection_formats["component_ids"] = "csv"  # noqa: E501

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
            "/content_views/{composite_content_view_id}/content_view_components/remove",
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