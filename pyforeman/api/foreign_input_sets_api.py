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


class ForeignInputSetsApi(object):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    Ref: https://github.com/swagger-api/swagger-codegen
    """

    def __init__(self, api_client=None):
        if api_client is None:
            api_client = ApiClient()
        self.api_client = api_client

    def delete_templates_template_id_foreign_input_sets_id(
        self, template_id, id, **kwargs
    ):  # noqa: E501
        """Delete a foreign input set  # noqa: E501

          # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.delete_templates_template_id_foreign_input_sets_id(template_id, id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str template_id: (required)
        :param str id: (required)
        :param float location_id: Set the current location context for the request
        :param float organization_id: Set the current organization context for the request
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs["_return_http_data_only"] = True
        if kwargs.get("async_req"):
            return (
                self.delete_templates_template_id_foreign_input_sets_id_with_http_info(
                    template_id, id, **kwargs
                )
            )  # noqa: E501
        else:
            (
                data
            ) = self.delete_templates_template_id_foreign_input_sets_id_with_http_info(
                template_id, id, **kwargs
            )  # noqa: E501
            return data

    def delete_templates_template_id_foreign_input_sets_id_with_http_info(
        self, template_id, id, **kwargs
    ):  # noqa: E501
        """Delete a foreign input set  # noqa: E501

          # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.delete_templates_template_id_foreign_input_sets_id_with_http_info(template_id, id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str template_id: (required)
        :param str id: (required)
        :param float location_id: Set the current location context for the request
        :param float organization_id: Set the current organization context for the request
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = [
            "template_id",
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
                    " to method delete_templates_template_id_foreign_input_sets_id"
                    % key
                )
            params[key] = val
        del params["kwargs"]
        # verify the required parameter 'template_id' is set
        if self.api_client.client_side_validation and (
            "template_id" not in params or params["template_id"] is None
        ):  # noqa: E501
            raise ValueError(
                "Missing the required parameter `template_id` when calling `delete_templates_template_id_foreign_input_sets_id`"
            )  # noqa: E501
        # verify the required parameter 'id' is set
        if self.api_client.client_side_validation and (
            "id" not in params or params["id"] is None
        ):  # noqa: E501
            raise ValueError(
                "Missing the required parameter `id` when calling `delete_templates_template_id_foreign_input_sets_id`"
            )  # noqa: E501

        collection_formats = {}

        path_params = {}
        if "template_id" in params:
            path_params["template_id"] = params["template_id"]  # noqa: E501
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
            "/templates/{template_id}/foreign_input_sets/{id}",
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

    def get_templates_template_id_foreign_input_sets(
        self, template_id, **kwargs
    ):  # noqa: E501
        """List foreign input sets  # noqa: E501

          # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_templates_template_id_foreign_input_sets(template_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str template_id: (required)
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
            return self.get_templates_template_id_foreign_input_sets_with_http_info(
                template_id, **kwargs
            )  # noqa: E501
        else:
            (data) = self.get_templates_template_id_foreign_input_sets_with_http_info(
                template_id, **kwargs
            )  # noqa: E501
            return data

    def get_templates_template_id_foreign_input_sets_with_http_info(
        self, template_id, **kwargs
    ):  # noqa: E501
        """List foreign input sets  # noqa: E501

          # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_templates_template_id_foreign_input_sets_with_http_info(template_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str template_id: (required)
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
            "template_id",
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
                    " to method get_templates_template_id_foreign_input_sets" % key
                )
            params[key] = val
        del params["kwargs"]
        # verify the required parameter 'template_id' is set
        if self.api_client.client_side_validation and (
            "template_id" not in params or params["template_id"] is None
        ):  # noqa: E501
            raise ValueError(
                "Missing the required parameter `template_id` when calling `get_templates_template_id_foreign_input_sets`"
            )  # noqa: E501

        collection_formats = {}

        path_params = {}
        if "template_id" in params:
            path_params["template_id"] = params["template_id"]  # noqa: E501

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
            "/templates/{template_id}/foreign_input_sets",
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

    def get_templates_template_id_foreign_input_sets_id(
        self, template_id, id, **kwargs
    ):  # noqa: E501
        """Show foreign input set details  # noqa: E501

          # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_templates_template_id_foreign_input_sets_id(template_id, id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str template_id: (required)
        :param str id: (required)
        :param float location_id: Set the current location context for the request
        :param float organization_id: Set the current organization context for the request
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs["_return_http_data_only"] = True
        if kwargs.get("async_req"):
            return self.get_templates_template_id_foreign_input_sets_id_with_http_info(
                template_id, id, **kwargs
            )  # noqa: E501
        else:
            (
                data
            ) = self.get_templates_template_id_foreign_input_sets_id_with_http_info(
                template_id, id, **kwargs
            )  # noqa: E501
            return data

    def get_templates_template_id_foreign_input_sets_id_with_http_info(
        self, template_id, id, **kwargs
    ):  # noqa: E501
        """Show foreign input set details  # noqa: E501

          # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_templates_template_id_foreign_input_sets_id_with_http_info(template_id, id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str template_id: (required)
        :param str id: (required)
        :param float location_id: Set the current location context for the request
        :param float organization_id: Set the current organization context for the request
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = [
            "template_id",
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
                    " to method get_templates_template_id_foreign_input_sets_id" % key
                )
            params[key] = val
        del params["kwargs"]
        # verify the required parameter 'template_id' is set
        if self.api_client.client_side_validation and (
            "template_id" not in params or params["template_id"] is None
        ):  # noqa: E501
            raise ValueError(
                "Missing the required parameter `template_id` when calling `get_templates_template_id_foreign_input_sets_id`"
            )  # noqa: E501
        # verify the required parameter 'id' is set
        if self.api_client.client_side_validation and (
            "id" not in params or params["id"] is None
        ):  # noqa: E501
            raise ValueError(
                "Missing the required parameter `id` when calling `get_templates_template_id_foreign_input_sets_id`"
            )  # noqa: E501

        collection_formats = {}

        path_params = {}
        if "template_id" in params:
            path_params["template_id"] = params["template_id"]  # noqa: E501
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
            "/templates/{template_id}/foreign_input_sets/{id}",
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

    def post_templates_template_id_foreign_input_sets(
        self, template_id, foreign_input_set_target_template_id, **kwargs
    ):  # noqa: E501
        """Create a foreign input set  # noqa: E501

          # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.post_templates_template_id_foreign_input_sets(template_id, foreign_input_set_target_template_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str template_id: (required)
        :param str foreign_input_set_target_template_id: Target template ID (required)
        :param float location_id: Set the current location context for the request
        :param float organization_id: Set the current organization context for the request
        :param bool foreign_input_set_include_all: Include all inputs from the foreign template
        :param str foreign_input_set_include: A comma separated list of input names to be included from the foreign template.
        :param str foreign_input_set_exclude: A comma separated list of input names to be included from the foreign template.
        :param str foreign_input_set_description: Input set description
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs["_return_http_data_only"] = True
        if kwargs.get("async_req"):
            return self.post_templates_template_id_foreign_input_sets_with_http_info(
                template_id, foreign_input_set_target_template_id, **kwargs
            )  # noqa: E501
        else:
            (data) = self.post_templates_template_id_foreign_input_sets_with_http_info(
                template_id, foreign_input_set_target_template_id, **kwargs
            )  # noqa: E501
            return data

    def post_templates_template_id_foreign_input_sets_with_http_info(
        self, template_id, foreign_input_set_target_template_id, **kwargs
    ):  # noqa: E501
        """Create a foreign input set  # noqa: E501

          # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.post_templates_template_id_foreign_input_sets_with_http_info(template_id, foreign_input_set_target_template_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str template_id: (required)
        :param str foreign_input_set_target_template_id: Target template ID (required)
        :param float location_id: Set the current location context for the request
        :param float organization_id: Set the current organization context for the request
        :param bool foreign_input_set_include_all: Include all inputs from the foreign template
        :param str foreign_input_set_include: A comma separated list of input names to be included from the foreign template.
        :param str foreign_input_set_exclude: A comma separated list of input names to be included from the foreign template.
        :param str foreign_input_set_description: Input set description
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = [
            "template_id",
            "foreign_input_set_target_template_id",
            "location_id",
            "organization_id",
            "foreign_input_set_include_all",
            "foreign_input_set_include",
            "foreign_input_set_exclude",
            "foreign_input_set_description",
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
                    " to method post_templates_template_id_foreign_input_sets" % key
                )
            params[key] = val
        del params["kwargs"]
        # verify the required parameter 'template_id' is set
        if self.api_client.client_side_validation and (
            "template_id" not in params or params["template_id"] is None
        ):  # noqa: E501
            raise ValueError(
                "Missing the required parameter `template_id` when calling `post_templates_template_id_foreign_input_sets`"
            )  # noqa: E501
        # verify the required parameter 'foreign_input_set_target_template_id' is set
        if self.api_client.client_side_validation and (
            "foreign_input_set_target_template_id" not in params
            or params["foreign_input_set_target_template_id"] is None
        ):  # noqa: E501
            raise ValueError(
                "Missing the required parameter `foreign_input_set_target_template_id` when calling `post_templates_template_id_foreign_input_sets`"
            )  # noqa: E501

        collection_formats = {}

        path_params = {}
        if "template_id" in params:
            path_params["template_id"] = params["template_id"]  # noqa: E501

        query_params = []

        header_params = {}

        form_params = []
        local_var_files = {}
        if "foreign_input_set_target_template_id" in params:
            form_params.append(
                (
                    "foreign_input_set[target_template_id]",
                    params["foreign_input_set_target_template_id"],
                )
            )  # noqa: E501
        if "location_id" in params:
            form_params.append(("location_id", params["location_id"]))  # noqa: E501
        if "organization_id" in params:
            form_params.append(
                ("organization_id", params["organization_id"])
            )  # noqa: E501
        if "foreign_input_set_include_all" in params:
            form_params.append(
                (
                    "foreign_input_set[include_all]",
                    params["foreign_input_set_include_all"],
                )
            )  # noqa: E501
        if "foreign_input_set_include" in params:
            form_params.append(
                ("foreign_input_set[include]", params["foreign_input_set_include"])
            )  # noqa: E501
        if "foreign_input_set_exclude" in params:
            form_params.append(
                ("foreign_input_set[exclude]", params["foreign_input_set_exclude"])
            )  # noqa: E501
        if "foreign_input_set_description" in params:
            form_params.append(
                (
                    "foreign_input_set[description]",
                    params["foreign_input_set_description"],
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
            "/templates/{template_id}/foreign_input_sets",
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

    def put_templates_template_id_foreign_input_sets_id(
        self, template_id, id, **kwargs
    ):  # noqa: E501
        """Update a foreign input set  # noqa: E501

          # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.put_templates_template_id_foreign_input_sets_id(template_id, id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str template_id: (required)
        :param str id: (required)
        :param float location_id: Set the current location context for the request
        :param float organization_id: Set the current organization context for the request
        :param str foreign_input_set_target_template_id: Target template ID
        :param bool foreign_input_set_include_all: Include all inputs from the foreign template
        :param str foreign_input_set_include: A comma separated list of input names to be included from the foreign template.
        :param str foreign_input_set_exclude: A comma separated list of input names to be included from the foreign template.
        :param str foreign_input_set_description: Input set description
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs["_return_http_data_only"] = True
        if kwargs.get("async_req"):
            return self.put_templates_template_id_foreign_input_sets_id_with_http_info(
                template_id, id, **kwargs
            )  # noqa: E501
        else:
            (
                data
            ) = self.put_templates_template_id_foreign_input_sets_id_with_http_info(
                template_id, id, **kwargs
            )  # noqa: E501
            return data

    def put_templates_template_id_foreign_input_sets_id_with_http_info(
        self, template_id, id, **kwargs
    ):  # noqa: E501
        """Update a foreign input set  # noqa: E501

          # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.put_templates_template_id_foreign_input_sets_id_with_http_info(template_id, id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str template_id: (required)
        :param str id: (required)
        :param float location_id: Set the current location context for the request
        :param float organization_id: Set the current organization context for the request
        :param str foreign_input_set_target_template_id: Target template ID
        :param bool foreign_input_set_include_all: Include all inputs from the foreign template
        :param str foreign_input_set_include: A comma separated list of input names to be included from the foreign template.
        :param str foreign_input_set_exclude: A comma separated list of input names to be included from the foreign template.
        :param str foreign_input_set_description: Input set description
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = [
            "template_id",
            "id",
            "location_id",
            "organization_id",
            "foreign_input_set_target_template_id",
            "foreign_input_set_include_all",
            "foreign_input_set_include",
            "foreign_input_set_exclude",
            "foreign_input_set_description",
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
                    " to method put_templates_template_id_foreign_input_sets_id" % key
                )
            params[key] = val
        del params["kwargs"]
        # verify the required parameter 'template_id' is set
        if self.api_client.client_side_validation and (
            "template_id" not in params or params["template_id"] is None
        ):  # noqa: E501
            raise ValueError(
                "Missing the required parameter `template_id` when calling `put_templates_template_id_foreign_input_sets_id`"
            )  # noqa: E501
        # verify the required parameter 'id' is set
        if self.api_client.client_side_validation and (
            "id" not in params or params["id"] is None
        ):  # noqa: E501
            raise ValueError(
                "Missing the required parameter `id` when calling `put_templates_template_id_foreign_input_sets_id`"
            )  # noqa: E501

        collection_formats = {}

        path_params = {}
        if "template_id" in params:
            path_params["template_id"] = params["template_id"]  # noqa: E501
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
        if "foreign_input_set_target_template_id" in params:
            form_params.append(
                (
                    "foreign_input_set[target_template_id]",
                    params["foreign_input_set_target_template_id"],
                )
            )  # noqa: E501
        if "foreign_input_set_include_all" in params:
            form_params.append(
                (
                    "foreign_input_set[include_all]",
                    params["foreign_input_set_include_all"],
                )
            )  # noqa: E501
        if "foreign_input_set_include" in params:
            form_params.append(
                ("foreign_input_set[include]", params["foreign_input_set_include"])
            )  # noqa: E501
        if "foreign_input_set_exclude" in params:
            form_params.append(
                ("foreign_input_set[exclude]", params["foreign_input_set_exclude"])
            )  # noqa: E501
        if "foreign_input_set_description" in params:
            form_params.append(
                (
                    "foreign_input_set[description]",
                    params["foreign_input_set_description"],
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
            "/templates/{template_id}/foreign_input_sets/{id}",
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
